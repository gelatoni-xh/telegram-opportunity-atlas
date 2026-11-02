#!/usr/bin/env python3
"""Search public Telegram channels and bots through the official TDLib API."""

import argparse
import ctypes
import getpass
import json
import os
import statistics
import sys
import time
from ctypes.util import find_library
from pathlib import Path
import shutil
import subprocess


DATA_DIR = Path.home() / ".local" / "share" / "telegram-bfs" / "tdlib"
KEYCHAIN_SERVICE = "telegram-opportunity-atlas"


def keychain_get(account):
    """Read one credential from macOS Keychain without printing it."""
    if not shutil.which("security"):
        return ""
    try:
        result = subprocess.run(
            ["security", "find-generic-password", "-a", account, "-s", KEYCHAIN_SERVICE, "-w"],
            check=True,
            capture_output=True,
            text=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return ""
    return result.stdout.strip()


def keychain_set(account, value):
    """Store one credential in macOS Keychain without exposing it to output."""
    if not shutil.which("security") or not value:
        return
    try:
        subprocess.run(
            ["security", "add-generic-password", "-U", "-a", account, "-s", KEYCHAIN_SERVICE, "-w", value],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
    except (OSError, subprocess.CalledProcessError):
        pass


def load_tdjson():
    candidates = [
        os.environ.get("TDJSON_PATH"),
        find_library("tdjson"),
        "/usr/local/opt/tdlib/lib/libtdjson.dylib",
        "/opt/homebrew/opt/tdlib/lib/libtdjson.dylib",
    ]
    for candidate in filter(None, candidates):
        try:
            return ctypes.CDLL(candidate)
        except OSError:
            pass
    raise RuntimeError("TDLib's tdjson library was not found. Install it with: brew install tdlib")


class Telegram:
    def __init__(self, socks5=None):
        self.lib = load_tdjson()
        self.lib.td_execute.restype = ctypes.c_char_p
        self.lib.td_execute.argtypes = [ctypes.c_char_p]
        self.lib.td_execute(b'{"@type":"setLogVerbosityLevel","new_verbosity_level":0}')
        self.lib.td_create_client_id.restype = ctypes.c_int
        self.lib.td_create_client_id.argtypes = []
        self.lib.td_send.restype = None
        self.lib.td_send.argtypes = [ctypes.c_int, ctypes.c_char_p]
        self.lib.td_receive.restype = ctypes.c_char_p
        self.lib.td_receive.argtypes = [ctypes.c_double]
        self.client_id = self.lib.td_create_client_id()
        self.next_id = 0
        self.socks5 = socks5
        self.proxy_added = False

    def add_proxy(self):
        if not self.socks5 or self.proxy_added:
            return
        host, separator, port = self.socks5.rpartition(":")
        if not separator or not host or not port.isdigit() or not 1 <= int(port) <= 65535:
            raise ValueError("SOCKS5 proxy must be HOST:PORT")
        self.request(
            "addProxy", server=host, port=int(port), enable=True,
            type={"@type": "proxyTypeSocks5", "username": "", "password": ""},
        )
        self.proxy_added = True

    def send(self, payload):
        self.lib.td_send(self.client_id, json.dumps(payload).encode("utf-8"))

    def receive(self, timeout=1.0):
        raw = self.lib.td_receive(timeout)
        return json.loads(raw.decode("utf-8")) if raw else None

    def request(self, name, timeout=45, **kwargs):
        self.next_id += 1
        request_id = str(self.next_id)
        self.send({"@type": name, "@extra": request_id, **kwargs})
        deadline = time.monotonic() + timeout
        while time.monotonic() < deadline:
            event = self.receive(min(1.0, deadline - time.monotonic()))
            if event and event.get("@extra") == request_id:
                if event.get("@type") == "error":
                    raise RuntimeError(f"{name}: {event.get('message', event)}")
                return event
        raise TimeoutError(f"{name} timed out")

    def login(self):
        while True:
            state = self.request("getAuthorizationState")
            kind = state.get("@type")
            if kind == "authorizationStateReady":
                self.add_proxy()
                return
            if kind == "authorizationStateWaitTdlibParameters":
                api_id_from_env = os.environ.get("TG_API_ID", "").strip()
                api_hash_from_env = os.environ.get("TG_API_HASH", "").strip()
                api_id = api_id_from_env or keychain_get("api_id") or input("Telegram API ID: ").strip()
                api_hash = api_hash_from_env or keychain_get("api_hash") or getpass.getpass("Telegram API hash: ")
                if not api_id.isdigit() or not api_hash:
                    raise ValueError("API ID must be numeric, and API hash cannot be empty")
                if not api_id_from_env:
                    keychain_set("api_id", api_id)
                if not api_hash_from_env:
                    keychain_set("api_hash", api_hash)
                DATA_DIR.mkdir(parents=True, exist_ok=True, mode=0o700)
                os.chmod(DATA_DIR, 0o700)
                self.request(
                    "setTdlibParameters",
                    parameters={
                        "@type": "tdlibParameters",
                        "database_directory": str(DATA_DIR),
                        "use_file_database": False,
                        "use_chat_info_database": False,
                        "use_message_database": False,
                        "use_secret_chats": False,
                        "api_id": int(api_id),
                        "api_hash": api_hash,
                        "system_language_code": "en",
                        "device_model": "telegram-bfs CLI",
                        "application_version": "0.1",
                    },
                )
            elif kind == "authorizationStateWaitEncryptionKey":
                self.request("checkDatabaseEncryptionKey", encryption_key="")
            elif kind == "authorizationStateWaitPhoneNumber":
                self.add_proxy()
                phone = input("Telegram phone number (international format): ").strip()
                self.request("setAuthenticationPhoneNumber", phone_number=phone)
            elif kind == "authorizationStateWaitCode":
                code = input("Telegram login code: ").strip()
                self.request("checkAuthenticationCode", code=code)
            elif kind == "authorizationStateWaitPassword":
                password = getpass.getpass("Telegram two-step password: ")
                self.request("checkAuthenticationPassword", password=password)
            else:
                raise RuntimeError(f"Unsupported Telegram login state: {kind}")

    def inspect(self, chat_id, query, post_limit, include_groups):
        chat = self.request("getChat", chat_id=chat_id)
        chat_type = chat.get("type", {})
        kind = chat_type.get("@type")
        row = {"query": query, "id": chat_id, "title": chat.get("title", "")}
        if kind == "chatTypePrivate":
            user = self.request("getUser", user_id=chat_type["user_id"])
            if not user.get("type", {}).get("@type") == "userTypeBot":
                return None
            row["type"] = "bot"
            row["username"] = user.get("username", "")
            try:
                info = self.request("getUserFullInfo", user_id=chat_type["user_id"])
                row["description"] = info.get("description", "")
            except RuntimeError:
                row["description"] = ""
        elif kind == "chatTypeSupergroup":
            is_channel = chat_type.get("is_channel", False)
            if not is_channel and not include_groups:
                return None
            row["type"] = "channel" if is_channel else "group"
            supergroup_id = chat_type["supergroup_id"]
            group = self.request("getSupergroup", supergroup_id=supergroup_id)
            row["username"] = group.get("username", "")
            full = self.request("getSupergroupFullInfo", supergroup_id=supergroup_id)
            row["description"] = full.get("description", "")
            row["members"] = full.get("member_count", group.get("member_count"))
            if is_channel and post_limit:
                try:
                    history = self.request(
                        "getChatHistory", chat_id=chat_id, from_message_id=0,
                        offset=0, limit=post_limit, only_local=False,
                    )
                    posts = history.get("messages", [])
                    views = [
                        msg.get("interaction_info", {}).get("view_count")
                        for msg in posts
                        if msg.get("interaction_info", {}).get("view_count") is not None
                    ]
                    row["recent_posts"] = len(posts)
                    row["latest_post_date"] = max((msg.get("date", 0) for msg in posts), default=0)
                    row["median_recent_views"] = statistics.median(views) if views else None
                except RuntimeError as exc:
                    row["history_error"] = str(exc)
        else:
            return None
        row["url"] = "https://t.me/" + row["username"] if row.get("username") else None
        return row


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("queries", nargs="+", help="Search terms, for example 'remote jobs' AI")
    parser.add_argument("--limit", type=int, default=20, help="Maximum search matches per term (default: 20)")
    parser.add_argument("--posts", type=int, default=10, help="Recent channel posts to sample (default: 10)")
    parser.add_argument("--include-groups", action="store_true", help="Include public groups")
    parser.add_argument("--socks5", help="SOCKS5 proxy as HOST:PORT (or set TG_SOCKS5)")
    parser.add_argument("--output", type=Path, help="Save results as JSON Lines; default: stdout")
    args = parser.parse_args()
    if not 1 <= args.limit <= 100 or not 0 <= args.posts <= 50:
        parser.error("--limit must be 1..100 and --posts must be 0..50")

    client = Telegram(args.socks5 or os.environ.get("TG_SOCKS5"))
    client.login()
    rows = {}
    for query in args.queries:
        print(f"Searching: {query}", file=sys.stderr)
        found = client.request("searchPublicChats", query=query)
        for chat_id in found.get("chat_ids", [])[:args.limit]:
            if chat_id in rows:
                rows[chat_id]["matched_queries"].append(query)
                continue
            try:
                row = client.inspect(chat_id, query, args.posts, args.include_groups)
            except (RuntimeError, TimeoutError) as exc:
                print(f"Skipping chat {chat_id}: {exc}", file=sys.stderr)
                continue
            if row:
                row["matched_queries"] = [query]
                rows[chat_id] = row
        time.sleep(1)

    payload = "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows.values())
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload, encoding="utf-8")
        print(f"Saved {len(rows)} results to {args.output}", file=sys.stderr)
    else:
        print(payload, end="")


if __name__ == "__main__":
    try:
        main()
    except (RuntimeError, TimeoutError, KeyboardInterrupt) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(1)

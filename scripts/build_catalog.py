#!/usr/bin/env python3
"""Build a derived, area-labelled catalog from a raw Telegram snapshot."""

import argparse
import json
from pathlib import Path


QUERY_AREAS = {
    "coupon deals": "购物优惠与优惠券",
    "discount alert bot": "购物优惠与优惠券",
    "food deals": "餐饮、杂货与餐厅优惠",
    "restaurant deals": "餐饮、杂货与餐厅优惠",
    "grocery deals": "餐饮、杂货与餐厅优惠",
    "SaaS deals": "AI 与软件发现",
    "software discounts": "AI 与软件发现",
    "cashback deals": "返现与价格提醒",
    "price tracker bot": "返现与价格提醒",
    "shopping assistant bot": "返现与价格提醒",
    "job alerts": "求职与职业发现",
    "remote jobs": "求职与职业发现",
    "remote developer jobs": "求职与职业发现",
    "freelance jobs": "求职与职业发现",
    "micro jobs": "求职与职业发现",
    "remote internships": "求职与职业发现",
    "job application bot": "求职与职业发现",
    "海外求职": "求职与职业发现",
    "远程工作": "求职与职业发现",
    "scholarship alerts": "奖学金与助学金",
    "scholarship bot": "奖学金与助学金",
    "scholarships bot": "奖学金与助学金",
    "留学奖学金": "奖学金与助学金",
    "English learning bot": "语言学习与考试",
    "IELTS bot": "语言学习与考试",
    "language exchange": "语言学习与考试",
    "language learning bot": "语言学习与考试",
    "exam prep bot": "语言学习与考试",
    "online course deals": "语言学习与考试",
    "AI tools bot": "AI 与软件发现",
    "AI for designers": "AI 与软件发现",
    "AI productivity tools": "AI 与软件发现",
    "AI设计": "AI 与软件发现",
    "flight deals": "旅行与交通优惠",
    "travel alert bot": "旅行与交通优惠",
    "travel itinerary bot": "旅行与交通优惠",
    "hotel deals": "旅行与交通优惠",
    "train deals": "旅行与交通优惠",
    "expat guide": "海外生活、搬迁与签证",
    "visa updates": "海外生活、搬迁与签证",
    "apartment rental": "海外生活、搬迁与签证",
    "housing expats": "海外生活、搬迁与签证",
    "digital nomad community": "海外生活、搬迁与签证",
    "fitness coach bot": "健身与习惯支持",
    "workout bot": "健身与习惯支持",
    "wellness habit tracker": "健身与习惯支持",
    "meditation bot": "健身与习惯支持",
    "sleep tracker bot": "健身与习惯支持",
    "gaming alerts": "游戏",
    "game deals": "游戏",
    "creator tools bot": "创作者工具与发布",
    "content creator community": "创作者工具与发布",
    "creator monetization": "创作者工具与发布",
    "newsletter tools": "创作者工具与发布",
    "crypto signals": "加密货币与交易信息",
    "crypto alerts bot": "加密货币与交易信息",
    "local events": "本地活动与城市发现",
    "event discovery bot": "本地活动与城市发现",
    "city guide": "本地活动与城市发现",
    "recipe channel": "餐饮、杂货与餐厅优惠",
    "parenting community": "家庭、育儿与膳食计划",
    "parenting tips channel": "家庭、育儿与膳食计划",
    "meal planning bot": "家庭、育儿与膳食计划",
    "budget planner bot": "个人预算与支出工具",
    "expense tracker bot": "个人预算与支出工具",
    "personal finance bot": "个人预算与支出工具",
    "productivity bot": "效率与个人组织",
    "study planner bot": "效率与个人组织",
    "book summaries": "书籍、媒体与娱乐发现",
    "reading club": "书籍、媒体与娱乐发现",
    "personal safety bot": "人身安全与紧急协助",
}


def build(source: Path, output: Path) -> int:
    rows = []
    for line_number, line in enumerate(source.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        row = json.loads(line)
        queries = row.get("matched_queries", [])
        areas = sorted({QUERY_AREAS[q] for q in queries if q in QUERY_AREAS})
        if not areas:
            raise ValueError(f"line {line_number}: no area mapping for {queries!r}")
        rows.append({**row, "areas": areas})
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows), encoding="utf-8")
    return len(rows)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    print(f"Wrote {build(args.source, args.output)} records to {args.output}")


if __name__ == "__main__":
    main()

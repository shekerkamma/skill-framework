#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

CASE_RULES = {
    "current-topic": {
        "must_include_any": [
            ["2026", "2025", "current", "as of"],
            ["official", "documentation", "github", "repo", "first-party"],
            ["[1]", "[2]"],
        ],
        "must_not_include": [
            "no sources",
        ],
        "notes": "Should show recency, citations, and primary-source discipline.",
    },
    "multi-view-topic": {
        "must_include_any": [
            ["benefit", "benefits"],
            ["risk", "risks"],
            ["consensus"],
            ["debate", "uncertainty", "trade-off"],
        ],
        "must_not_include": [],
        "notes": "Should represent both upside and downside, with structured balance.",
    },
    "uncertain-topic": {
        "must_include_any": [
            ["uncertain", "uncertainty", "limited evidence", "evidence is limited"],
            ["infer", "inference", "suggests", "may"],
            ["gap", "gaps", "further research"],
        ],
        "must_not_include": [
            "proven to",
            "guaranteed",
        ],
        "notes": "Should avoid false certainty and make evidence limitations explicit.",
    },
}


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text.lower()).strip()


def evaluate(case: str, research_text: str) -> dict:
    rules = CASE_RULES[case]
    normalized = normalize(research_text)

    matched_groups = []
    missing_groups = []
    for group in rules["must_include_any"]:
        if any(term in normalized for term in group):
            matched_groups.append(group)
        else:
            missing_groups.append(group)

    forbidden_hits = [term for term in rules["must_not_include"] if term in normalized]

    passed = not missing_groups and not forbidden_hits
    return {
        "case": case,
        "passed": passed,
        "score": len(matched_groups),
        "max_score": len(rules["must_include_any"]),
        "matched_groups": matched_groups,
        "missing_groups": missing_groups,
        "forbidden_hits": forbidden_hits,
        "notes": rules["notes"],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--case", choices=sorted(CASE_RULES.keys()), required=True)
    parser.add_argument("--research-file", required=True)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    path = Path(args.research_file)
    if not path.exists():
        print(f"research file not found: {path}", file=sys.stderr)
        return 2

    text = path.read_text(encoding="utf-8")
    result = evaluate(args.case, text)

    if args.json:
        print(json.dumps(result, indent=2))
        return 0 if result["passed"] else 1

    print(f"Case: {result['case']}")
    print(f"Pass: {'yes' if result['passed'] else 'no'}")
    print(f"Score: {result['score']}/{result['max_score']}")
    print(f"Notes: {result['notes']}")

    if result["matched_groups"]:
        print("\nMatched expectations:")
        for group in result["matched_groups"]:
            print(f"- one of: {', '.join(group)}")

    if result["missing_groups"]:
        print("\nMissing expectations:")
        for group in result["missing_groups"]:
            print(f"- one of: {', '.join(group)}")

    if result["forbidden_hits"]:
        print("\nForbidden hits:")
        for hit in result["forbidden_hits"]:
            print(f"- {hit}")

    print("\nHuman review still required.")
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

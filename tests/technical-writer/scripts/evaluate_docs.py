#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

CASE_RULES = {
    "readme": {
        "must_include_any": [
            ["overview", "features"],
            ["installation", "setup"],
            ["quick start"],
            ["usage", "examples"],
            ["troubleshooting", "common issues"],
        ],
        "must_not_include": [],
        "notes": "Should look like a usable README with early reader value.",
    },
    "api-doc": {
        "must_include_any": [
            ["parameters", "args"],
            ["returns", "return value"],
            ["example"],
            ["errors", "error cases"],
        ],
        "must_not_include": [],
        "notes": "Should include the core API documentation sections requested.",
    },
    "incomplete-source": {
        "must_include_any": [
            ["assumption", "assumptions"],
            ["unknown", "unknowns", "missing information"],
        ],
        "must_not_include": [
            "guaranteed",
            "definitive",
        ],
        "notes": "Should acknowledge incompleteness instead of inventing detail.",
    },
}


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text.lower()).strip()


def evaluate(case: str, doc_text: str) -> dict:
    rules = CASE_RULES[case]
    normalized = normalize(doc_text)
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
    parser.add_argument("--doc-file", required=True)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    path = Path(args.doc_file)
    if not path.exists():
        print(f"doc file not found: {path}", file=sys.stderr)
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

#!/usr/bin/env python3

"""
Semi-automated evaluator for code-reviewer skill outputs.

Usage:
  python3 tests/code-reviewer/scripts/evaluate_review.py \
    --case bad-change \
    --review-file /path/to/review.md

This does not replace human judgment. It checks for expected signals:
- presence of core findings
- restraint on clean cases
- acknowledgement of uncertainty on partial diffs
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


CASE_RULES = {
    "bad-change": {
        "must_include_any": [
            ["sql injection", "injection", "parameterized", "interpolation"],
            ["rows[0]", "empty result", "indexerror", "no result", "unsafe access"],
            ["missing test", "regression test", "test coverage", "edge-case coverage"],
        ],
        "must_not_include": [
            "formatting only",
        ],
        "max_findings_hint": None,
        "notes": "Should catch the security issue, the empty-result bug, and missing tests.",
    },
    "clean-change": {
        "must_include_any": [],
        "must_not_include": [
            "sql injection",
            "xss",
            "auth bypass",
            "critical issue",
            "critical issues",
        ],
        "max_findings_hint": 1,
        "notes": "Should usually return no findings, or at most one very justified low-risk note.",
    },
    "edge-case": {
        "must_include_any": [
            ["partial diff", "missing context", "assuming", "assumption", "context is missing"],
            ["private", "privacy", "authorization", "auth", "data exposure"],
        ],
        "must_not_include": [],
        "max_findings_hint": None,
        "notes": "Should state uncertainty and identify the plausible privacy/auth regression risk.",
    },
}


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text.lower()).strip()


def count_findings(text: str) -> int:
    patterns = [
        r"(?m)^\d+\.\s",
        r"(?m)^- \*\*",
        r"(?m)^##\s+(critical|high|medium)",
    ]
    counts = [len(re.findall(pattern, text)) for pattern in patterns]
    return max(counts) if counts else 0


def evaluate(case: str, review_text: str) -> dict:
    rules = CASE_RULES[case]
    normalized = normalize(review_text)

    matched_groups = []
    missing_groups = []
    for group in rules["must_include_any"]:
        if any(term in normalized for term in group):
            matched_groups.append(group)
        else:
            missing_groups.append(group)

    forbidden_hits = [term for term in rules["must_not_include"] if term in normalized]

    findings_count = count_findings(review_text)
    max_findings_hint = rules["max_findings_hint"]

    score = 0
    max_score = max(len(rules["must_include_any"]), 1)
    score += len(matched_groups)

    if not rules["must_include_any"] and not forbidden_hits:
        score = 1

    if max_findings_hint is not None and findings_count <= max_findings_hint:
        score += 1
        max_score += 1
    elif max_findings_hint is not None:
        max_score += 1

    passed = not missing_groups and not forbidden_hits
    if max_findings_hint is not None:
        passed = passed and findings_count <= max_findings_hint

    return {
        "case": case,
        "passed": passed,
        "score": score,
        "max_score": max_score,
        "findings_count_estimate": findings_count,
        "matched_groups": matched_groups,
        "missing_groups": missing_groups,
        "forbidden_hits": forbidden_hits,
        "notes": rules["notes"],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--case", choices=sorted(CASE_RULES.keys()), required=True)
    parser.add_argument("--review-file", required=True)
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON")
    args = parser.parse_args()

    review_path = Path(args.review_file)
    if not review_path.exists():
        print(f"review file not found: {review_path}", file=sys.stderr)
        return 2

    review_text = review_path.read_text(encoding="utf-8")
    result = evaluate(args.case, review_text)

    if args.json:
        print(json.dumps(result, indent=2))
        return 0 if result["passed"] else 1

    print(f"Case: {result['case']}")
    print(f"Pass: {'yes' if result['passed'] else 'no'}")
    print(f"Score: {result['score']}/{result['max_score']}")
    print(f"Estimated findings count: {result['findings_count_estimate']}")
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

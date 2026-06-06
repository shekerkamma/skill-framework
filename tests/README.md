# Skill Tests

This folder contains lightweight manual test cases for skills in this repo.

The goal is not full automation. The goal is repeatable evaluation.

## Current Coverage

- `code-reviewer/`

## Test Method

For each skill:
1. open a fresh agent session in a repo where the skill is available
2. paste the case prompt
3. provide the case file contents or diff
4. compare the output against the expected review characteristics

## Pass Standard

A skill passes when it:
- triggers for the intended prompt
- follows its own output contract
- catches the important issues in the bad case
- avoids inventing issues in the clean case
- handles missing context carefully in the edge case

## Notes

These tests are intentionally small and inspectable.

If a skill fails:
- update the skill
- rerun the failed case
- rerun at least one previously passing case to avoid regressions

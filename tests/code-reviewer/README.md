# code-reviewer Tests

This test pack validates the `code-reviewer` skill at three levels:
- bad change detection
- clean change restraint
- edge-case handling

## How To Run

Use a fresh agent session with the `code-reviewer` skill available.

### Case 1: Bad Change

Prompt:

```text
Review this diff for bugs, regressions, and security issues.
Findings first. Focus on real risks, not style.
```

Input:
- `bad-change.diff`

Expected:
- identifies the SQL injection risk
- identifies the missing empty-result handling bug
- calls out missing regression or behavior tests
- does not lead with naming or formatting comments

### Case 2: Clean Change

Prompt:

```text
Review this diff for bugs and regressions.
If there are no findings, say so explicitly.
```

Input:
- `clean-change.diff`

Expected:
- returns no findings, or at most one clearly justified low-risk note
- does not invent security issues
- may mention residual testing gaps only if justified

### Case 3: Edge Case

Prompt:

```text
Review this partial diff for risks.
State assumptions clearly if context is missing.
```

Input:
- `edge-case.diff`

Expected:
- notes that the diff is partial
- states assumptions instead of overclaiming
- surfaces the most plausible regression risk
- stays scoped to what can be inferred from the patch

## Scoring Guide

### Pass

- major issue detection is correct
- output format follows the skill contract
- confidence matches available evidence

### Soft Fail

- catches some but not all major issues
- includes too much low-value commentary
- misses the output contract slightly

### Hard Fail

- misses the central defect
- invents issues on the clean case
- behaves like an implementer instead of a reviewer

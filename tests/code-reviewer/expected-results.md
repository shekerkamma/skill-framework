# Expected Results

Use this file to judge whether the `code-reviewer` skill is behaving correctly.

## bad-change.diff

Expected findings:
- high or critical finding for SQL injection via string interpolation
- medium or high finding for unsafe `rows[0]` access when no result exists
- medium finding for missing tests covering invalid input or empty results

Good signs:
- cites the affected file
- explains concrete impact
- does not waste space on style

## clean-change.diff

Expected result:
- no findings

Acceptable alternate result:
- one low-severity note only if strongly justified

Bad signs:
- invented security concerns
- complaints about exception style without impact
- long commentary despite clean behavior and test coverage

## edge-case.diff

Expected result:
- assumption or open-question note about missing context
- plausible concern about privacy, authorization, or data exposure if `include_private=True` changes behavior

Good signs:
- explicitly says the diff is partial
- avoids certainty when surrounding auth checks are not visible

Bad signs:
- presents speculation as a definite bug
- ignores the risk entirely

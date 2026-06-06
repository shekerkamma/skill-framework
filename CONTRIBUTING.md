# Contributing

This repo is for reusable OpenHands/Codex-style agent skills.

Each production skill in this repo should be:
- narrowly scoped
- grounded in a validated workflow
- supported by a checklist
- testable with small fixtures
- listed in `SKILLS.md`

## What To Contribute

Good contributions:
- a new production-ready skill
- improvements to an existing skill's clarity or constraints
- better test fixtures
- a semi-automated evaluator for an existing test pack
- corrections to repo-level documentation

Avoid contributing:
- broad, catch-all skills
- skills that still contain unresolved placeholders
- speculative skills without a validated workflow
- tests with no expected result criteria

## Required Skill Layout

Every skill lives under:

```text
.agents/skills/<skill-name>/
  SKILL.md
  references/
  scripts/        # optional
  assets/         # optional
```

Minimum requirement for a production skill:
- `SKILL.md`
- at least one checklist or support file in `references/`

## Skill Quality Standard

A production skill should:
- define when to use it
- define when not to use it
- give a concrete execution workflow
- include guardrails
- define what good output looks like
- avoid unsupported claims or vague behavior

It should not:
- contain unresolved placeholders
- rely on implied behavior
- depend on hidden repo context
- overreach beyond one clear job

## How To Add A New Skill

### 1. Start from the template

Copy:

```text
.agents/skills/skill-starter-template/
```

Rename it to the real skill name.

### 2. Replace placeholders

Do not leave any `<placeholder>` text in a production skill.

### 3. Add references

At minimum, add one checklist or support document under:

```text
.agents/skills/<skill-name>/references/
```

Typical reference files:
- checklist
- output schema
- style rules
- domain notes

### 4. Add tests

Create:

```text
tests/<skill-name>/
  README.md
  expected-results.md
  <fixture files>
  scripts/        # optional evaluator
```

The test README should describe:
- what the skill is being tested for
- how to run the test
- what a pass looks like
- what a hard fail looks like

### 5. Add an evaluator when useful

If output quality can be partially checked automatically, add:

```text
tests/<skill-name>/scripts/evaluate_<something>.py
```

Evaluator rules:
- keep it lightweight
- make it explain pass/fail clearly
- do not pretend it replaces human judgment
- return a non-zero exit code for failure

### 6. Update `SKILLS.md`

Every production skill must be added to:

- `SKILLS.md`

Include:
- purpose
- when to use it
- skill file links
- test file links
- evaluator link if present

## Testing Requirements

Before merging or publishing a skill, test at three levels:

### Structural

Check:
- file layout is correct
- links resolve
- no placeholder text remains

### Behavioral

Run the skill on representative cases and confirm:
- it triggers appropriately
- it follows its own output contract
- it stays in scope

### Evaluation

If an evaluator exists:
- run it on at least one passing example
- ensure the result matches human judgment

## Documentation Style

Repo docs should be:
- concise
- operational
- explicit about constraints
- easy to scan

Prefer:
- short sections
- flat lists
- concrete examples

Avoid:
- broad theory dumps
- motivational filler
- duplicated instructions across multiple files unless necessary

## Publication Checklist

Before publishing a contribution, confirm:
- skill files exist in `.agents/skills/<skill-name>/`
- reference files exist
- tests exist in `tests/<skill-name>/`
- evaluator exists if appropriate
- `SKILLS.md` is updated
- no placeholders remain
- examples are internally consistent

## Current Pattern

Use the existing production skills as examples:
- `code-reviewer`
- `deep-research`
- `technical-writer`

Use `skill-starter-template` only as a scaffold, not as a published end state.

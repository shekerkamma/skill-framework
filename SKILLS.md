# Skills Index

This file is the entry point for the reusable skills in `skill-framework`.

Use it to see:
- what skills exist
- when to use them
- where their test packs live
- which evaluator script to run

## Available Skills

### `code-reviewer`

Purpose:
- review code changes for bugs, regressions, security issues, performance risks, and missing tests

Use when:
- reviewing a PR or diff
- auditing a code change
- checking whether a change is risky

Skill files:
- [SKILL.md](./.agents/skills/code-reviewer/SKILL.md)
- [review-checklist.md](./.agents/skills/code-reviewer/references/review-checklist.md)

Tests:
- [tests/code-reviewer/README.md](./tests/code-reviewer/README.md)
- evaluator: [evaluate_review.py](./tests/code-reviewer/scripts/evaluate_review.py)

Primary test cases:
- `bad-change.diff`
- `clean-change.diff`
- `edge-case.diff`

### `deep-research`

Purpose:
- conduct citation-backed, current, source-aware research with explicit uncertainty handling

Use when:
- the task needs multi-source investigation
- the topic is time-sensitive
- the output must separate consensus from debate
- the user needs a structured research brief

Skill files:
- [SKILL.md](./.agents/skills/deep-research/SKILL.md)
- [research-checklist.md](./.agents/skills/deep-research/references/research-checklist.md)

Tests:
- [tests/deep-research/README.md](./tests/deep-research/README.md)
- evaluator: [evaluate_research.py](./tests/deep-research/scripts/evaluate_research.py)

Primary test cases:
- `current-topic.md`
- `multi-view-topic.md`
- `uncertain-topic.md`


### `technical-writer`

Purpose:
- write clear, structured technical documentation such as READMEs, guides, API references, and onboarding docs

Use when:
- the user needs technical docs drafted or revised
- the output needs to explain how to use or understand a system clearly
- source-faithful examples and structure matter

Skill files:
- [SKILL.md](./.agents/skills/technical-writer/SKILL.md)
- [documentation-checklist.md](./.agents/skills/technical-writer/references/documentation-checklist.md)

Tests:
- [tests/technical-writer/README.md](./tests/technical-writer/README.md)
- evaluator: [evaluate_docs.py](./tests/technical-writer/scripts/evaluate_docs.py)

Primary test cases:
- `readme-case.md`
- `api-doc-case.md`
- `incomplete-source-case.md`

### `skill-starter-template`

Purpose:
- scaffold a new skill after a workflow has been validated manually

Use when:
- creating a new project-specific skill
- converting a repeated manual workflow into a reusable skill

Skill files:
- [SKILL.md](./.agents/skills/skill-starter-template/SKILL.md)
- [scripts/README.md](./.agents/skills/skill-starter-template/scripts/README.md)
- [references/README.md](./.agents/skills/skill-starter-template/references/README.md)

Supporting guide:
- [docs/skill-building-playbook.md](./docs/skill-building-playbook.md)

## Suggested Workflow

When adding a new skill:
1. start from `skill-starter-template`
2. validate the workflow manually
3. replace placeholders with the real workflow
4. add a checklist in `references/`
5. add a lightweight test pack in `tests/<skill-name>/`
6. add an evaluator script when a semi-automated pass/fail signal is useful
7. add the new skill to this index

## Testing Pattern

Every production skill in this repo should ideally have:
- a real `SKILL.md`
- at least one supporting checklist in `references/`
- a `tests/<skill-name>/README.md`
- 2-3 representative fixtures
- an evaluator script when output quality can be partially checked automatically

## Current Status

- `code-reviewer`: production-ready example with semi-automated tests
- `deep-research`: production-ready example with semi-automated tests
- `technical-writer`: production-ready example with semi-automated tests
- `skill-starter-template`: scaffold only, not a production skill

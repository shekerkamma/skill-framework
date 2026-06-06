---
name: openhands-pr-artifact-handoff
description: Use this skill when OpenHands work needs temporary PR-only artifacts in `.pr/`, such as design notes, investigation docs, logs, or cross-repo verification evidence that should help reviewers but not remain on main after merge.
---

# OpenHands PR Artifact Handoff

Use this skill for `OpenHands` repository work when a pull request needs temporary supporting artifacts for reviewers.

This is a project-specific example skill based on the `.pr/` workflow documented in the OpenHands repo.

## Sources of Truth

- `AGENTS.md`
- `.github/workflows/pr-artifacts.yml`

## When To Use `.pr/`

Use `.pr/` when the material is:

- reviewer-facing
- temporary
- not intended to stay on `main` after merge

Good examples:

- design rationale
- investigation notes
- one-off scripts used only for the PR
- test logs
- cross-repo verification evidence
- reviewer notes

## When Not To Use `.pr/`

Do not place durable repository content in `.pr/`.

Examples that belong elsewhere:

- reusable scripts
- permanent architecture docs
- user-facing docs
- anything still needed after merge

## Workflow

### 1. Decide if the artifact is temporary

Use one question:

> Would this still belong in the repo after the PR merges?

If yes, do not put it under `.pr/`.

### 2. Create a small, obvious structure

Prefer:

```text
.pr/
├── design.md
├── analysis.md
├── notes.md
└── logs/
```

### 3. Capture reviewer-useful evidence

The artifacts should help a reviewer answer:

- what changed
- why the approach was chosen
- what was tested
- what remains risky or unverified

For logs, prefer captured command output over paraphrase.

### 4. Stage intentionally

Use targeted staging for `.pr/` files.

Temporary does not mean low quality.

### 5. Set cleanup expectations correctly

For same-repo PRs, the OpenHands workflow:

- posts or updates a PR notice when `.pr/` exists
- automatically removes `.pr/` after approval

For fork PRs:

- the notice still matters
- cleanup is manual before merge

Do not tell reviewers cleanup is automatic on fork PRs.

## Output Contract

When using this skill, say:

1. what was placed in `.pr/`
2. why it belongs there instead of the normal repo tree
3. whether the cleanup path is automatic or manual
4. any reviewer action or caveat that remains

See `references/pr-artifact-checklist.md` for the compact version.

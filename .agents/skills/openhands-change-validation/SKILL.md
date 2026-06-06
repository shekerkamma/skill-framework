---
name: openhands-change-validation
description: Use this skill when work in the OpenHands repository needs repo-specific validation before it is considered done, especially when the correct checks depend on whether the change touched backend Python, frontend, the VSCode extension, enterprise code, or docs only.
---

# OpenHands Change Validation

Use this skill for `OpenHands` repository work when the agent needs to determine the correct validation path before calling a change complete.

This is a project-specific example skill. It is grounded in the contributor rules documented in the OpenHands repo itself.

## Sources of Truth

- `AGENTS.md`
- `Development.md`
- `CONTRIBUTING.md`
- changed files in the current worktree

Prefer `AGENTS.md` when current repo rules and older habits diverge.

## Goal

Pick the smallest correct validation set for the current OpenHands change, run it when possible, fix simple failures, rerun checks after autofixes, and report precisely what passed, failed, or was not run.

## Workflow

### 1. Classify the changed area

Inspect the changed files first and place the work into one or more buckets:

- **Backend Python**: `openhands/`, `tests/unit/`, `scripts/`, root Python config
- **Frontend**: `frontend/`
- **VSCode extension**: `openhands/app_server/integrations/vscode/`
- **Enterprise**: `enterprise/`
- **Docs or metadata only**: markdown, issue templates, repo docs, non-executable config
- **Mixed**: multiple buckets above

### 2. Apply the OpenHands baseline rule

Before making code changes, OpenHands expects:

```bash
make install-pre-commit-hooks
```

If the environment cannot run this command, do not hide that limitation. Record it in the final validation summary.

### 3. Choose the validation path

#### Backend Python

Run focused tests when the file-to-test mapping is clear:

```bash
poetry run pytest tests/unit/test_<relevant>.py
```

Then run the repo-mandated Python check:

```bash
pre-commit run --config ./dev_config/python/.pre-commit-config.yaml
```

If using `--files` is safer than broad staged-file checks because of unrelated worktree changes, do that.

#### Frontend

Run the required frontend commands:

```bash
cd frontend && npm run lint:fix && npm run build
```

If UI behavior, hooks, or API usage changed and a focused frontend test exists, run it too.

#### VSCode extension

Run:

```bash
cd openhands/app_server/integrations/vscode && npm run lint:fix && npm run compile
```

#### Enterprise

Use enterprise-targeted tests or enterprise pre-commit commands based on the changed area.

#### Docs-only

Do not invent unrelated code validation.

Instead:

- verify factual claims against source material
- check paths, commands, and links for correctness
- say explicitly that no code validation was required if that is true

#### Mixed

Run the union of the required checks across all touched areas.

### 4. Fix small failures and rerun

If lint or formatting tools auto-fix files, inspect the edits and rerun the same validation command.

Common cases:

- formatting fixes
- whitespace cleanup
- missing newlines
- frontend lint autofixes

### 5. Report with precision

Always separate results into:

- **Passed**
- **Failed**
- **Not run**

For skipped steps, give the concrete reason:

- tool missing
- dependency missing
- blocked by environment
- intentionally not run because scope did not require it

Do not call the change fully validated unless the required checks for the touched areas actually passed.

## Output Contract

The summary should state:

1. which parts of OpenHands changed
2. which commands were run
3. which checks passed
4. which checks failed or were skipped
5. whether the change is ready for push

See `references/change-validation-checklist.md` for the compact version.

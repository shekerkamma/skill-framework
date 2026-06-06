# OpenHands PR Artifact Checklist

## Use `.pr/` only if

- the material is reviewer-facing
- the material is temporary
- the material should disappear after merge

## Good candidates

- design notes
- debugging notes
- test logs
- one-off validation scripts
- cross-repo verification evidence

## Bad candidates

- durable docs
- reusable scripts
- user-facing documentation
- permanent architecture references

## Suggested layout

- `.pr/design.md`
- `.pr/analysis.md`
- `.pr/notes.md`
- `.pr/logs/`

## Cleanup

- same-repo PR: CI removes `.pr/` after approval
- fork PR: manual removal is required before merge

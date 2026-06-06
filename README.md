# skill-framework

Portable framework for building OpenHands/Codex-style agent skills.

## Contents

- `docs/skill-building-playbook.md`: reusable method for building new skills
- `.agents/skills/skill-starter-template/`: scaffold for creating a new skill
- `.agents/skills/code-reviewer/`: example production-ready review skill

## Purpose

This repo separates the framework from any one project so the playbook and example skills can be reused across repositories.

## Skill Layout

```text
.agents/
  skills/
    <skill-name>/
      SKILL.md
      scripts/
      references/
      assets/
```

## Included Example

The included `code-reviewer` skill is adapted from the `code-reviewer` skill in `Shubhamsaboo/awesome-llm-apps`, rebuilt for stricter OpenHands/Codex review workflows that prioritize concrete findings, severity ordering, and file-linked evidence.

## Upstream Inspiration

- `https://github.com/Shubhamsaboo/awesome-llm-apps`
- `https://docs.openhands.dev/overview/skills`
- `https://docs.openhands.dev/sdk/guides/skill`

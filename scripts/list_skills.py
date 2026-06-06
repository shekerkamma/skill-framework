#!/usr/bin/env python3

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / '.agents' / 'skills'


def parse_field(text: str, field: str) -> str | None:
    pattern = rf'(?m)^{re.escape(field)}:\s*(.+)$'
    match = re.search(pattern, text)
    if not match:
        return None
    value = match.group(1).strip()
    if value == '>':
        return None
    return value.strip('"\'')


def classify(skill_name: str, description: str | None) -> str:
    if skill_name == 'skill-starter-template':
        return 'scaffold'
    if description and 'template' in description.lower():
        return 'scaffold'
    return 'production'


def main() -> int:
    if not SKILLS_DIR.exists():
        print('No skills directory found.')
        return 1

    skill_files = sorted(SKILLS_DIR.glob('*/SKILL.md'))
    if not skill_files:
        print('No skills found.')
        return 1

    print('skill-framework inventory')
    print('========================')

    for skill_file in skill_files:
        text = skill_file.read_text(encoding='utf-8')
        name = parse_field(text, 'name') or skill_file.parent.name
        description = parse_field(text, 'description')
        status = classify(name, description)

        print(f'- {name} [{status}]')
        if description:
            print(f'  {description}')
        print(f'  path: {skill_file.relative_to(ROOT)}')

    return 0


if __name__ == '__main__':
    raise SystemExit(main())

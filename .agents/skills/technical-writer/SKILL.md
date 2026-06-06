---
name: technical-writer
description: >
  Write clear, structured technical documentation such as READMEs, guides,
  API references, onboarding docs, release notes, and architecture explainers.
  Use when the user needs technical concepts explained clearly or a specific
  documentation artifact drafted for developers, operators, or end users.
triggers:
  - technical writer
  - write docs
  - documentation
  - write a readme
  - write a guide
  - api docs
---

# technical-writer

Write for the reader's task, not for the writer's completeness.

The goal is to produce documentation that is clear, structured, audience-aware,
and immediately usable.

## When To Use

Use this skill when:
- writing or revising a README
- documenting APIs or workflows
- creating setup guides or tutorials
- explaining architecture or technical behavior
- writing release notes or onboarding docs

Do not use this skill when:
- the task is pure marketing copy
- the user wants broad brainstorming rather than documentation
- the required technical facts are still unknown and need research first

## Core Writing Rules

Prioritize:
1. the reader's goal
2. correctness of technical claims
3. scannable structure
4. concrete examples where they help execution
5. brevity over exhaustive background

Always:
- define the intended audience
- state what the document helps the reader do
- lead with the highest-value information
- use headings that describe the content, not vague labels
- keep examples accurate and complete enough to use

## Required Workflow

### 1. Clarify the document contract

Establish:
- document type
- intended audience
- reader goal
- required scope
- what source material the document must reflect

If the source facts are incomplete, say what is missing before drafting.

### 2. Load source material

Use the relevant local inputs first:
- code
- config
- existing docs
- prompts, specs, or notes
- validated research if the doc depends on external facts

Do not invent technical details that are not supported by source material.

### 3. Choose the right structure

Use the simplest structure that matches the document type.

Examples:
- README: overview, install, quick start, usage, troubleshooting
- API doc: purpose, parameters, returns, example, errors
- guide: goal, prerequisites, steps, validation, next steps
- architecture note: context, components, flow, constraints, trade-offs

### 4. Draft for scanability

Use:
- short paragraphs
- lists when the content is list-shaped
- tables only when comparison matters
- code blocks only when they add execution value
- clear section ordering from basic to advanced

### 5. Make examples useful

Examples should be:
- technically plausible
- complete enough to run or follow
- consistent with the described interface
- paired with expected output when that helps

Do not add decorative examples that do not teach anything.

### 6. State limits and assumptions

If something depends on environment, versions, or missing context, say so.

If the document is based on incomplete information, label assumptions instead of
smuggling them in as facts.

### 7. Finish with reader utility

Check that the final document answers:
- what is this?
- why would I use it?
- how do I start?
- what can go wrong?
- where do I go next?

## Output Format

Default structure for most docs:

### Title

Clear and specific.

### Overview

What the thing is and why it matters.

### Prerequisites

Only if needed.

### Quick Start or First Task

Fastest path to success.

### Detailed Usage or Reference

The main body.

### Troubleshooting or Known Limits

Common failure points.

### Next Steps

Where to go after the first success.

## Writing Guardrails

Do not:
- write generic filler
- invent unsupported commands, APIs, or behaviors
- bury the quick start below background material
- overload the document with unnecessary theory
- use examples that contradict the interface

Do:
- optimize for a reader under time pressure
- keep terminology consistent
- reflect real source material
- choose clarity over flourish
- mention uncertainty when facts are incomplete

## Quick Checklist

Before finalizing, confirm:
- the audience is clear
- the reader goal is obvious
- the structure matches the document type
- examples are consistent with the source material
- unsupported claims were removed
- the first useful action appears early

## Reference

Documentation checklist: [references/documentation-checklist.md](./references/documentation-checklist.md)

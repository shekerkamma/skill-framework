---
name: deep-research
description: >
  Conduct comprehensive, citation-backed research using current and primary
  sources where possible. Use when the user needs multi-source investigation,
  synthesized analysis, current-state comparisons, source-aware summaries, or
  a structured research brief rather than a quick answer.
triggers:
  - deep research
  - research this
  - investigate this
  - research brief
  - synthesize sources
  - current analysis
---

# deep-research

Research for accuracy first, synthesis second.

The goal is to produce a useful, well-structured research output grounded in
current evidence, with explicit sourcing and clear handling of uncertainty.

## When To Use

Use this skill when:
- the user needs multi-source research
- the topic benefits from current information
- the output needs citations or source attribution
- the task requires comparing viewpoints or evidence
- the user wants a research brief, investigation, or synthesized analysis

Do not use this skill when:
- the user only needs a quick factual answer
- the work is purely local and does not require external sources
- the task is mostly brainstorming without evidence requirements

## Core Research Rules

Prioritize:
1. current information when the topic is time-sensitive
2. primary sources over secondary summaries
3. explicit dates for unstable facts
4. source quality over source quantity
5. synthesis that preserves uncertainty instead of flattening it

Always:
- verify temporally unstable claims
- distinguish fact from inference
- note when evidence is weak, missing, or contested
- use exact dates when they clarify recency
- prefer official docs, papers, filings, releases, and first-party statements

## Required Workflow

### 1. Clarify the research task

Establish:
- the exact question
- the decision or deliverable the research supports
- the required depth
- the most important angles
- whether the user needs current-state information

If the task is broad, break it into answerable sub-questions.

### 2. Define the research plan

Before gathering sources, identify:
- key subtopics
- likely primary-source categories
- what evidence would count as strong
- what would change the conclusion

Keep the plan small enough to execute, but broad enough to avoid tunnel vision.

### 3. Gather sources deliberately

Source order:
- official documentation or first-party pages
- research papers or formal publications
- regulatory or standards bodies
- reputable reporting or analysis
- expert commentary only after stronger evidence is checked

When the topic is current, confirm dates and avoid relying on stale summaries.

### 4. Evaluate source quality

For each important source, consider:
- who published it
- when it was published
- whether it is first-hand or derivative
- whether it has incentives or bias worth noting
- whether it actually supports the claim being made

Do not overstate low-quality evidence.

### 5. Synthesize instead of stacking quotes

Produce synthesis by:
- grouping findings into themes
- separating consensus from disagreement
- identifying what is known versus inferred
- calling out missing evidence
- highlighting decision-relevant takeaways

Do not simply list sources in sequence.

### 6. Cite clearly

Use inline numbered citations like `[1]`, `[2]`.

At the end, include a source list with:
- title
- publisher or author
- date
- URL
- short credibility note when useful

### 7. Close with research judgment

End with:
- what the evidence most strongly supports
- what remains uncertain
- what follow-up research would reduce uncertainty

## Output Format

Use this structure unless the user asks for another one:

### Executive Summary

2-4 sentences on the main answer.

### Key Findings

- concise, decision-relevant findings with citations

### Detailed Analysis

Use thematic sub-sections.

### Areas of Consensus

What strong sources broadly agree on.

### Areas of Debate or Uncertainty

What is contested, incomplete, or changing.

### Sources

Enumerated source list.

### Gaps and Next Research

What is still unknown or worth checking next.

## Research Guardrails

Do not:
- use outdated information for a current-state question
- present weak evidence as settled
- hide uncertainty
- inflate confidence because multiple secondary sources repeat the same claim
- overquote sources when paraphrase is enough

Do:
- browse for unstable facts
- prefer primary sources
- use exact dates where they matter
- say when you are inferring
- keep the final synthesis concise and useful

## Quick Checklist

Before finalizing, confirm:
- the key claims are source-backed
- time-sensitive facts were verified
- primary sources were used where available
- exact dates are included when relevant
- consensus and disagreement are separated
- inference is labeled as inference

## Reference

Research checklist: [references/research-checklist.md](./references/research-checklist.md)

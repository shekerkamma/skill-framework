# deep-research Tests

This test pack validates the `deep-research` skill at three levels:
- current-source discipline
- balanced synthesis
- explicit uncertainty handling

## How To Run

Use a fresh agent session with the `deep-research` skill available.

After capturing the skill output into a markdown file, run:

```bash
python3 tests/deep-research/scripts/evaluate_research.py \
  --case current-topic \
  --research-file /tmp/deep-research-output.md
```

### Case 1: Current Topic

Prompt:

```text
Research the current state of browser automation agents in 2026.
Use current sources, prefer primary sources, and cite everything important.
```

Expected:
- uses current citations
- includes exact dates when discussing current-state claims
- references first-party docs, repos, or official pages
- avoids unsupported sweeping conclusions

### Case 2: Multi-View Topic

Prompt:

```text
Research the benefits and risks of adopting MCP for internal tooling.
Separate consensus from debate.
```

Expected:
- covers both benefits and risks
- has explicit consensus and debate sections
- does not collapse all viewpoints into one-sided conclusions

### Case 3: Uncertain Topic

Prompt:

```text
Investigate whether autonomous agents can reliably self-improve their own prompts without regression.
Be explicit about uncertainty and evidence quality.
```

Expected:
- qualifies uncertain claims
- distinguishes direct evidence from inference
- notes evidence gaps instead of overstating confidence

## Pass Standard

### Pass

- output follows the skill contract
- evaluator passes
- human reviewer agrees the synthesis is balanced and source-aware

### Soft Fail

- adequate sources but weak synthesis
- current facts present but dates omitted
- uncertainty mentioned but not handled consistently

### Hard Fail

- stale or weak sourcing for a current question
- one-sided synthesis where the prompt requires balance
- unsupported certainty on contested claims

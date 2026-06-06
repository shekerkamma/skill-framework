# technical-writer Tests

This test pack validates the `technical-writer` skill at three levels:
- structure selection
- audience-aware clarity
- source-faithful examples

## How To Run

Use a fresh agent session with the `technical-writer` skill available.

After capturing the output into a markdown file, run:

```bash
python3 tests/technical-writer/scripts/evaluate_docs.py \
  --case readme \
  --doc-file /tmp/technical-writer-output.md
```

### Case 1: README

Prompt:

```text
Write a README for a CLI tool that validates YAML files against a schema.
Audience: developers.
Include quick start, usage examples, and troubleshooting.
```

Expected:
- has a clear overview
- includes installation or setup
- includes quick start
- includes usage examples
- includes troubleshooting or common failure modes

### Case 2: API Doc

Prompt:

```text
Write API documentation for a function that uploads a file and returns a signed URL.
Include parameters, return value, example, and error cases.
```

Expected:
- includes parameters
- includes return value
- includes example
- includes error cases
- remains structured and scannable

### Case 3: Incomplete Source Material

Prompt:

```text
Draft onboarding documentation from incomplete notes.
Be explicit about assumptions and unknowns.
```

Expected:
- flags assumptions
- does not invent precise unsupported technical details
- keeps the document useful despite missing information

## Pass Standard

### Pass

- output follows the requested document type
- evaluator passes
- human reviewer agrees the document is clear and source-faithful

### Soft Fail

- mostly clear but weakly structured
- examples present but too thin
- assumptions not labeled consistently

### Hard Fail

- wrong document structure
- invented technical specifics
- no useful quick-start path where one was requested

# VOMAC v0.1 - Problem Definition

## Problem
Modern software systems often receive data from multiple sources
but lack a structured decision-making core that can interpret inputs,
maintain internal state, and produce consistent decisions.

Most applications tightly couple logic with implementation,
making reasoning, extension, and system integration difficult.

## Goal
The goal of VOMAC v0.1 is to build a minimal but structured
decision core that can:

- Accept structured input
- Maintain internal memory/state
- Apply deterministic rule-based reasoning
- Produce a clear and traceable output

## Non-Goals (v0.1)
- Machine learning
- Natural language understanding
- Optimization or planning
- External integrations

These will be addressed in later versions.

## Input
VOMAC receives a structured input object containing:
- Source
- Type
- Payload data

Example:
```json
{
  "source": "system",
  "type": "event",
  "payload": {
    "value": 72
  }
}
```
## Output
VOMAC produces a structured decision result:

```json
{
  "decision": "ALERT",
  "reason": "Value exceeded threshold",
  "confidence": 1.0
}

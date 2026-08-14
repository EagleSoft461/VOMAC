# VOMAC v0.5.1 — Snapshot-Aware Decision Context Architecture

## Overview

VOMAC v0.5.1 extends the Rule-Based Decision Layer introduced in v0.5.0.

In v0.5.0, rules could only evaluate incoming events.

In v0.5.1, rules gain access to the system’s **current state
snapshots**:

- Context snapshot (live system state)
- Memory snapshot (historical / stored state)

This enables deterministic decisions that depend not only on the current event, but also on the system’s internal state.

This version still does not introduce AI, learning, or external intelligence.
---
## Design Goal

The primary goal of v0.5.1 is:

> Allow rules to evaluate decisions based on
> event + memory snapshot + context snapshot
> in a deterministic and testable manner.

The system must be able to:

- collect snapshots from modules

- inject snapshots into DecisionContext

- keep memory/context passive (read-only)

- preserve deterministic execution flow

## Core Philosophy

In v0.5.1:

- Events are still raw signals

- Tasks are still pure work units

- Execution remains mechanical

- Rules remain deterministic and side-effect free

- Memory and Context remain passive observers

The system becomes state-aware, but not intelligent.

## Architectural Position

The snapshot layer sits inside DecisionContext.
```text
Event
  ↓
TaskRouter
  ↓
DecisionContext (event + snapshots)
  ↓
DecisionEngine (rules)
  ↓
DecisionResult
  ↓
TaskManager.submit()
  ↓
TaskQueue
  ↓
Worker.execute()
```

## Main Components

### SnapshotProvider Interface (New)

A minimal contract for modules that can provide snapshots.

Responsibilities:

- expose a get_snapshot() method

- return serializable state data

- never modify system state

Example:

- ContextModule implements snapshot provider

- MemoryModule implements snapshot provider

## Context Snapshot

A Context snapshot represents the current system state.

Examples:

- last event type

- current module states

- timestamps

- runtime flags

- system mode

This snapshot is read-only.

## Memory Snapshot

A Memory snapshot represents stored system state.

Examples:

- last N events

- stored facts

- counters

- session history

This snapshot is read-only.

## DecisionContext (Extended)

DecisionContext now includes:

- event_type

- event_payload

- context_snapshot (optional)

- memory_snapshot (optional)

- timestamp metadata

DecisionContext is still immutable and deterministic.

## Rule Evaluation Model

Rules can now evaluate conditions like:

- "If event is X and memory shows Y, do task Z"

- "If event is X but context mode is SAFE, do task A"

Rules still follow:

- evaluation in order

- first match wins (default strategy)

## Explainability Requirement

Decision logs must include:

- event received

- decision invoked

- snapshots included (yes/no)

- matched rule name

- submitted task name

DecisionResult must include:

- evaluated rule list

- matched rule name

- snapshot metadata flags

## Lifecycle Flow (v0.5.1)
```text
Core.start()

Module emits event:
  → EventDispatcher.emit(event)

TaskRouter receives event:
  → collects snapshots from providers
  → builds DecisionContext(event + snapshots)
  → calls DecisionEngine.decide(context)

DecisionEngine returns DecisionResult:
  → TaskRouter submits selected task
  → Worker executes task
```

## Explicit Non-Goals

The following are intentionally excluded from v0.5.1:

- AI integration

- LLM usage

- probabilistic decisions

- learning

- state mutation from rules

- external brains

- complex planning

## Expected Outcome

At completion of v0.5.1:

- rules can make decisions using event + snapshots

- memory and context remain passive

- decision logic stays deterministic

- architecture becomes ready for v0.6.0 (external intelligence)

## Architectural Principle

> A system must see its own state
> before it can reason about the world.
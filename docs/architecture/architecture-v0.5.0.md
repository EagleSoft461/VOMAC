# VOMAC v0.5.0 — Rule-Based Decision Layer Architecture

## Overview

VOMAC v0.5.0 introduces the **Decision Layer**.

Previous versions established the execution pipeline:

- v0.4.0 — Task execution infrastructure (tasks, queue, worker, engine)
- v0.4.1 — Event → Task routing via TaskRouter

In v0.5.0, the system gains the ability to **select tasks intentionally**
based on deterministic rules.

This version still does not include AI, learning, or external reasoning engines.

---

## Design Goal

The primary goal of v0.5.0 is:

> Enable the system to make deterministic decisions  
> about which tasks to execute, based on rules.

The system must be able to:

- evaluate rules against current state
- choose a task (or none)
- explain the decision path
- remain predictable and testable

---

## Core Philosophy

In v0.5.0:

- Events remain raw signals
- Context and memory remain passive observers
- Rules provide deterministic selection
- Tasks remain pure work units
- Execution remains mechanical

Decision-making is rule-based, not intelligent.

---

## Architectural Position

The Decision Layer sits between routing and task submission.

```text
Event
  ↓
TaskRouter (maps event → decision input)
  ↓
DecisionEngine (rule evaluation)
  ↓
TaskManager.submit()
  ↓
TaskQueue
  ↓
Worker.execute()
```
---
## Main Components

### DecisionEngine

A deterministic rule evaluation engine.

Responsibilities:

- accept an input context (event + system state)
- evaluate ordered rules
- return a decision result(task selection)
- provide explanation metadata

> Strategy: first-match-wins (single-task output).

DecisionEngine does not execute tasks.

---
## Rule

A rule represents a single decision condition.

A rule consists of:

- name/id 
- condition(event, state) → bool
- action(event, state) → decision output

Rules must be deterministic and side-effect free.
---
## DecisionContext

A structured input object passed to the DecisionEngine.

Contains:

- event type
- event payload
- memory snapshot (optional)
- context snapshot (optional)
- system metadata (timestamps, module states)

DecisionContext is read-only.
---
## DecisionResult

A structured output returned by DecisionEngine.

Contains:

- selected task(or none)
- payload
- explanation / trace
- matched rule id

DecisionResult must be serializable and loggable.
---
## Rule Evaluation Model

v0.5.0 uses a deterministic evaluation order:

1. Rules are evaluated in registration order
2. First match wins (default strategy)
3. DecisionEngine returns one task output

This is intentionally strict.

Future versions may support:

- multiple rule matches
- priority scoring
- weighted strategies

---

## Explainability Requirement

Every decision must be explainable.

Minimum required logs:

- event received
- decision engine invoked
- matched rule name
- submitted task name

DecisionResult must contain:

- rule trace (list of evaluated rules)
- match status

---

## Lifecycle Flow (v0.5.0)
```text
Core.start()
  → Engine.start()
  → TaskRouter.start()
  → DecisionEngine.register_rule()

Module emits event:
  → EventDispatcher.emit(EVENT)

TaskRouter receives event:
  → builds DecisionContext
  → calls DecisionEngine.decide(context)

DecisionEngine returns DecisionResult:
  → TaskRouter submits task(s)
  → Worker executes task(s)
```
---
## Explicit Non-Goals

The following are intentionally excluded from v0.5.0:

- machine learning
- LLM integration
- probabilistic decision-making
- external reasoning
- long-term planning
- goal systems
- reinforcement learning

This is a rule-based deterministic layer only.
---
## Expected Outcome

At completion of v0.5.0:

- the system can select tasks intentionally
- decisions are deterministic and explainable
- decision logic is isolated from execution
- the architecture remains expandable
- rule sets can evolve without modifying the Core

## Architectural Principle

> A system must decide deterministically
> before it can decide intelligently.

---

## Containerization (Docker)

Starting with v0.5.0, VOMAC includes an official Docker setup.

### Goal

- provide a consistent runtime environment
- make the project easy to run for reviewers
- improve reproducibility for CI/CD

Docker is introduced as a packaging and execution tool only.
It does not affect the internal architecture.

### Expected Files

- `Dockerfile`
- `.dockerignore`
- `requirements.txt`

### Example Usage

```bash
docker build -t vomac .
docker run -it vomac
```

### Notes

The system runs in interactive mode by default
(Press ENTER to shutdown...), therefore Docker execution requires -it.
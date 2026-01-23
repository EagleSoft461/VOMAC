# VOMAC v0.3.0 — Memory & Context Architecture

## Overview

VOMAC v0.3.0 introduces the first form of system state awareness.

Previous versions focused on structural stability:

- v0.2.a established orchestration and lifecycle control
- v0.2.b introduced controlled event-driven communication

Version v0.3.0 builds on this foundation by introducing
**state retention mechanisms**.

The purpose of this version is not intelligence,
but **system awareness through memory and context.**

---

## Design Goal

The primary goal of v0.3.0 is:

> To allow the system to understand what has happened
> and what is currently true during execution.

This version separates system state into two distinct concerns:

- historical knowledge (Memory)
- current condition (Context)

No reasoning, learning, or decision-making is introduced.

---

## Core Philosophy

In v0.3.0:

- Memory records the past
- Context represents the present
- The Core remains unaware of meaning

Neither Memory nor Context perform decisions.

They only provide structured state visibility.

---

## Architectural Position

Both Memory and Context are implemented as **modules**.

They follow the same lifecycle contract as all other modules.

The Core does not depend on either module.

They depend only on the event dispatcher.

```text
Event → Memory   (history)
Event → Context  (current state)
```
Neither module emits control signals.
---
## Memory Module
### Purpose

Memory represents historical system data.

It answers:

> What has already happened?

## Responsibilities

- observe all dispatched events

- store immutable event snapshots

- preserve temporal ordering

- maintain append-only history

- expose read-only access

## Characteristics

- in-memory only

- non-persistent

- passive observer

- no schema enforcement

- no interpretation

Memory never modifies system behavior.
---
## Context Module
### Purpose

Context represents the **current system condition.**

It answers:

> What is true right now?

## Responsibilities

- observe system events

- update internal state representation

- track latest known values

- maintain system-level flags

- generate read-only snapshots

Context evolves over time but does not reason.
---
## Context State

ContextState is a mutable internal structure.

It may contain:

- last received event

- module readiness flags

- system lifecycle phase

- event counters

- timestamps and uptime markers

ContextState is never exposed directly.
---
## Context Snapshot

ContextSnapshot is an immutable representation of ContextState.

Characteristics:

- read-only

- detached from mutation

- safe for external consumers

- suitable for debugging and reasoning input

Snapshots provide visibility without control.
---
## Lifecycle Behavior

1. Core initializes

2. Modules are loaded

3. Event dispatcher begins broadcasting

4. Memory stores historical events

5. Context updates live system state

6. System shuts down

7. Memory and Context clear internal data

All state exists only for the lifetime of the process.
---
## Explicit Non-Goals

The following features are intentionally excluded from v0.3.0:

- persistence or databases

- long-term memory storage

- reasoning or evaluation logic

- rule engines

- learning mechanisms

- task orchestration

- event replay

These concerns are reserved for later versions.
---
## Expected Outcome

At completion of v0.3.0:

- the system can retain execution history

- the system can expose current state safely

- memory and context remain passive observers

- architectural boundaries remain strictly enforced

This version establishes the foundation required
for all future decision and reasoning layers.
---
## Architectural Principle

>Memory remembers the past.
>Context reflects the present.
>Intelligence belongs to the future.
# ADR-003: Context and Memory Separation

Status: Accepted  
Version: v0.3.0  
Date: 2026-01-23

## Context

With the introduction of state retention in v0.3.0,
the system required a clear distinction between
historical data and current system condition.

Early prototypes stored all state in a single structure,
which led to conceptual ambiguity:

- past events
- current flags
- live system condition

were mixed together.

This created risks for future reasoning layers.

---

## Decision

The system separates state into two independent modules:

### Memory
- Stores historical event records
- Append-only
- Immutable snapshots
- Represents the past

### Context
- Stores current system condition
- Mutable internal state
- Represents the present
- Exposes read-only snapshots

Neither module performs reasoning or decisions.

---

## Rationale

This separation was chosen to:

- prevent mixing history with live state
- simplify future reasoning models
- enable deterministic snapshots
- preserve architectural clarity
- avoid implicit intelligence

The system must know **what happened**
and **what is true now** as two distinct concepts.

---

## Consequences

### Positive
- clean mental model
- clear responsibility boundaries
- easier reasoning integration in future versions
- safer debugging and observability

### Negative
- slightly increased architectural complexity
- two modules instead of one

This tradeoff was accepted to preserve long-term scalability.

---

## Status

This decision is final for v0.3.x.

Any future reasoning or decision layer must consume:

- Memory for historical context
- Context snapshots for current state

and must never mutate either.

---

## Principle

> The past must not change.  
> The present must be observable.  
> The future must decide.
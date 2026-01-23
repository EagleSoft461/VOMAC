# ADR-002 — Memory Design Decision

# ADR-002: Passive Memory Design

Status: Accepted  
Version: v0.3.0  
Date: 2026-01-23

---

## Context

Early versions of VOMAC explored direct decision pipelines.
This approach tightly coupled logic with data flow
and limited system extensibility.

As the architecture evolved toward event-driven orchestration,
a clear separation between history and reasoning became necessary.

---

## Decision

Memory in VOMAC shall be implemented as a passive system module.

The Memory module:

- observes system events
- stores historical data
- does not interpret events
- does not emit events
- does not influence system behavior

Memory acts as an archive, not an authority.

---

## Rationale

This design ensures:

- clear separation of concerns
- predictable system behavior
- elimination of hidden decision paths
- safe future integration of reasoning engines
- auditability and observability

By preventing memory from participating in logic,
future intelligence layers can operate deterministically.

---

## Consequences

### Positive
- Memory remains stable across architectural changes
- Historical data is preserved independently
- Debugging and traceability improve
- Reasoning engines can be replaced safely

### Negative
- Memory cannot react autonomously
- Additional layers are required for interpretation

This tradeoff is intentional.

---

## Resulting Principle

> Memory must never think.  
> Memory must never decide.  
> Memory must only remember.
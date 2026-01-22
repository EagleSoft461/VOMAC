# VOMAC v0.2.b — Event System Architecture

# ADR — v0.2.b Event System Architecture

Status: Accepted  
Version: v0.2.b  
Date: 2026-01-21

## Overview

VOMAC v0.2.b introduces a controlled reintroduction of event-driven communication.

Unlike earlier versions, events in v0.2.b are treated strictly as
an infrastructure-level communication mechanism.

The Core does not interpret events.
The Core does not define event meanings.

Events exist solely to enable loose coupling between modules.

---

## Design Goals

The goals of the v0.2.b event system are:

- Enable module-to-module communication
- Preserve Core simplicity and stability
- Prevent tight coupling between system components
- Isolate module failures
- Maintain deterministic system behavior

This version introduces no decision logic, memory, or intelligence.

---

## Core Philosophy

In v0.2.b:

- The Core does not emit semantic events
- The Core does not react to event types
- The Core only owns the dispatcher lifecycle

Event meaning belongs exclusively to modules.

---

## High-Level Architecture

```text
+-------------------------------+
| Core                          |
| Lifecycle • Module Loading   |
| EventDispatcher (blind)      |
+---------------+---------------+
                |
                v
+--------------------------------+
| Event Dispatcher               |
| emit() • subscribe()           |
| failure isolation              |
+---------------+---------------+
                |
                v
+--------------------------------+
| Modules                        |
| on_event(event) (optional)     |
| domain-specific reactions      |
+--------------------------------+
```
---
## Event Object
Events are immutable data objects.

Each event contains:

- type (string)
- payload (dictionary)
- source (optional)
- timestamp
The event object carries information but has no behavior.
---
## Event Dispatcher

The EventDispatcher is responsible for:

- Maintaining a list of subscribers

- Delivering events to subscribed modules

- Catching and isolating module failures

- Logging dispatch errors

The dispatcher does not interpret event content.
---
## Module Event Handling

Modules may optionally implement:
```python
def on_event(self, event):
    pass
```
Modules that do not implement this method
are not registered as event listeners.

Modules must never directly reference other modules.

All inter-module communication must occur via events.
---
## Explicit Non-Responsibilities

The v0.2.b event system must never:

- Contain decision logic

- Trigger system behavior in the Core

- Enforce event schemas

- Manage workflows

- Persist events

These concerns belong to later versions.
---
## Expected Outcome

At completion of v0.2.b:

- Modules communicate without direct dependencies

- Core remains stable and unaware of event semantics

- Event-driven extension becomes possible

- System complexity remains controlled

This version prepares the foundation for:

- Memory systems (v0.3)

- Reasoning layers (v0.3)

- Task orchestration (v0.4)
--- 
## Architectural Principle

> Events connect modules,
not intelligence.
# VOMAC v0.2.0 — Architecture Design

## Overview

VOMAC v0.2.0 introduces a fundamental architectural shift.

Previous versions were built around a linear decision pipeline.
While effective for early experimentation, pipeline-based designs
limit extensibility, parallelism, and long-term scalability.

Version 0.2.0 transforms VOMAC into an **orchestration-driven system core**.

The primary objective of this version is not intelligence,
but **architectural stability**.

---

## Design Goals

The v0.2.0 architecture is designed to achieve the following goals:

- Clear separation of responsibilities
- Long-term system scalability
- Replaceable and independent modules
- Event-driven communication
- Minimal and stable core layer
- Foundation for future memory and reasoning systems

No new intelligence mechanisms are introduced in this version.

---

## Core Philosophy

In v0.2.0:

- The Core does not think
- The Core does not decide
- The Core does not contain business logic

The Core exists solely to **coordinate system behavior**.

All intelligence is delegated to modules.

---

## High-Level Architecture
```Text
+-------------------------------+
| Core |
| Lifecycle • Events • Config |
| Logging • Module Management |
+---------------+---------------+
|
v
+--------------------------------+
| Modules |
| Memory • Reasoning • IO • AI |
| Domain-specific behaviors |
+--------------------------------+
```
The Core manages orchestration.
Modules provide capabilities.

---

## Core Responsibilities

The Core layer is responsible for:

- System lifecycle management
- Module discovery and registration
- Event dispatch and routing
- Centralized configuration access
- Centralized logging
- Graceful startup and shutdown

The Core must remain stable across future versions.

---

## Explicit Non-Responsibilities

The Core must never contain:

- Decision logic
- Rule engines
- Memory algorithms
- AI inference logic
- Domain-specific behavior

If logic is added to the Core, the architecture is considered violated.

---

## Module System

Modules represent independent system capabilities.

Each module:

- Implements a common interface
- Maintains its own internal state
- Listens to system events
- Emits new events
- Can be added or removed without modifying the Core

Modules must never directly communicate with each other.
All communication occurs through events.

---

## Module Interface Contract

All modules must implement the following interface:

```python
class ModuleInterface:

    def init(self, core):
        """
        Called once during system startup.
        Provides access to core services.
        """

    def on_event(self, event):
        """
        Called for every dispatched event.
        Modules may react or ignore.
        """

    def shutdown(self):
        """
        Called during graceful system shutdown.
        """
```
This contract is mandatory.
---
# Event-Driven Communication
v0.2.0 introduces a fully event-driven model.

Examples of system events:

+ SYSTEM_START

+ MODULE_REGISTERED

+ MODULE_READY

+ EVENT_EMITTED

+ SYSTEM_SHUTDOWN

+ ERROR_OCCURRED

Events are immutable data objects.

The Core does not interpret event meaning.
It only routes events.
---
## System Lifecycle

1. Core initialization

2. Configuration loading

3. Logger initialization

4. Module discovery

5. Module initialization

6. SYSTEM_START event dispatch

7. Normal operation

8. SYSTEM_SHUTDOWN event dispatch

9. Module shutdown

10. Core termination

This lifecycle must remain deterministic.
---
### Configuration Management

Configuration is centralized.

+ Core loads configuration files

+ Configuration objects are injected into modules

+ Modules must not read configuration files directly

This ensures environment portability and testability.
---
## Logging Strategy

Logging is centralized and standardized.

Each log entry must include:

+ Timestamp

+ Module name

+ Log level

+ Message

Modules must never manage their own logging infrastructure.
---
## Out of Scope for v0.2.0

The following features are intentionally excluded:

+ Memory implementation

+ Reasoning logic

+ Task prioritization

+ AI model integration

+ Hardware communication

These capabilities will be introduced in later versions
after architectural stability is achieved.
---
## Expected Outcome

At the completion of v0.2.0:

+ The system is fully modular

+ The Core remains small and stable

+ Modules are independently replaceable

+ New capabilities can be added without refactoring the Core

This version establishes the foundation upon which
all future intelligence layers will be built.
---
## Architectural Principle

> A system must be structurally sound
before it can become intelligent.
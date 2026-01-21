# VOMAC v0.2.a — Architecture (Implementation Phase)

## Purpose

This document describes the architecture that is
actually implemented in v0.2.a.

Focus:
System stability before intelligence.

This phase exists to validate that VOMAC can:

- start deterministically
- manage modules safely
- shutdown gracefully

No intelligence is implemented in this version.

---

## Core Responsibilities

In v0.2.a, the Core is responsible for:

- system startup and shutdown
- module registration
- lifecycle orchestration
- centralized logging access
- centralized configuration access

The Core does NOT:

- dispatch events
- interpret data
- execute decisions
- run business logic

---

## Module Contract

Modules in v0.2.a implement a minimal lifecycle contract:

```python
class Module:

    def start(self, context):
        pass

    def stop(self):
        pass
```

Modules do not communicate with each other.

Event-based communication is intentionally postponed.

## System Lifecycle
1. Core initialization

2. Configuration loading

3. Logger initialization

4. Module registration

5. Module start sequence

6. System running

7. Shutdown signal

8. Module stop sequence

9. Core termination

The lifecycle must remain deterministic and observable via logs.
---
## Out of Scope
The following are intentionally excluded:

- event system

- decision logic

- memory

- reasoning

- AI integration

- concurrency

parallel execution

These capabilities will be introduced only after
architectural stability is proven.
---

## File Classification

### Active in v0.2.a
- core/core.py
- core/config_manager.py
- core/logger.py
- core/module_loader.py

### Temporarily Disabled (v0.2.b)
- core/event_bus.py
- core/events/event.py

### Legacy Reference (v0.1)
- legacy/v0.1/*
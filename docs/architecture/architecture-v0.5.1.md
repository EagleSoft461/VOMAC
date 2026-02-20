# VOMAC v0.5.1 — Snapshot Provider System

## Overview

VOMAC v0.5.1 extends v0.5.0 with a **Snapshot Provider System**.

This version enhances the Decision Layer by enabling modules to expose their state as structured snapshots, which are then collected by the TaskRouter and passed to the DecisionEngine as part of the DecisionContext.

---

## Design Goal

The primary goal of v0.5.1 is:

> Enable modules to expose their internal state as structured snapshots  
> for use in decision-making, without exposing mutable state directly.

The system must be able to:

- register modules as snapshot providers
- collect snapshots from multiple modules
- pass snapshots to decision rules safely
- maintain clear separation between state and snapshots

---

## What Changed from v0.5.0

v0.5.0 introduced the Decision Layer with rule-based task selection. However, DecisionContext only contained event information.

v0.5.1 adds:

- **SnapshotProvider interface** — abstract base for modules that can provide snapshots
- **Snapshot provider registry** — Core maintains a registry of modules that implement `get_snapshot()`
- **Snapshot collection** — TaskRouter collects snapshots from registered providers before decision-making
- **Enhanced DecisionContext** — now includes `memory_snapshot` and `context_snapshot` fields

---

## Core Philosophy

In v0.5.1:

- Modules remain independent observers
- Snapshots are read-only, serializable representations
- Decision rules can access system state without coupling
- State remains encapsulated within modules
- Snapshot collection is optional and fault-tolerant

---

## Architectural Position

The Snapshot Provider System sits between modules and decision-making:

```text
Module (Memory/Context)
  ↓ (implements get_snapshot())
Core (registers as snapshot provider)
  ↓ (passes registry to TaskRouter)
TaskRouter (collects snapshots on event)
  ↓ (builds DecisionContext with snapshots)
DecisionEngine (evaluates rules with context)
  ↓
TaskManager.submit()
```

---

## Main Components

### SnapshotProvider Interface

An abstract base class defining the snapshot contract.

```python
class SnapshotProvider(ABC):
    @abstractmethod
    def get_snapshot(self) -> Dict[str, Any]:
        pass
```

Any module implementing `get_snapshot()` can be registered as a snapshot provider.

### Snapshot Provider Registry

Core maintains a dictionary mapping module names to snapshot provider instances:

```python
self.snapshot_providers = {}
```

During module initialization, Core checks if a module implements `get_snapshot()` and registers it:

```python
if hasattr(module, "get_snapshot"):
    self.snapshot_providers[name] = module
```

### TaskRouter Snapshot Collection

When TaskRouter receives an event, it collects snapshots from registered providers:

```python
memory_snapshot = None
context_snapshot = None

if "memory" in self._snapshot_providers:
    memory_snapshot = self._snapshot_providers["memory"].get_snapshot()

if "context" in self._snapshot_providers:
    context_snapshot = self._snapshot_providers["context"].get_snapshot()
```

Snapshots are collected with error handling — failures do not block decision-making.

### Enhanced DecisionContext

DecisionContext now includes snapshot fields:

```python
ctx = DecisionContext(
    event_type=event_type,
    event_payload=payload,
    memory_snapshot=memory_snapshot,      # v0.5.1
    context_snapshot=context_snapshot      # v0.5.1
)
```

Rules can now access system state through these snapshots.

---

## Module Implementation

### Memory Module

The Memory module implements `get_snapshot()` to expose event history statistics:

```python
def get_snapshot(self):
    return self.store.snapshot()
```

Returns:
- `event_count`: number of stored events
- `last_event_type`: type of most recent event
- `recent_events`: list of recent event types
- `max_events`: maximum capacity

### Context Module

The Context module implements `get_snapshot()` to expose current system state:

```python
def get_snapshot(self):
    return self.state.snapshot()
```

Returns:
- `system_started`, `system_ready`, `system_shutdown`: lifecycle flags
- `started_at`: system start timestamp
- `last_event_type`, `last_event_source`, `last_event_time`: latest event info
- `event_count`: total events processed
- `event_types`: count per event type
- `modules_ready`: set of ready module names

---

## Snapshot Characteristics

Snapshots must be:

- **Read-only** — no mutation possible
- **Serializable** — can be converted to JSON/dict
- **Detached** — independent of module internal state
- **Safe** — no side effects when accessed
- **Optional** — decision-making works without snapshots

---

## Lifecycle Flow (v0.5.1)

```text
Core.start()
  → Engine.start()
  → Modules loaded
  → Snapshot providers registered (if get_snapshot exists)
  → TaskRouter.start() (with snapshot_providers registry)

Module emits event:
  → EventDispatcher.emit(EVENT)

TaskRouter receives event:
  → Collects snapshots from registered providers
  → Builds DecisionContext (event + snapshots)
  → Calls DecisionEngine.decide(context)

DecisionEngine evaluates rules:
  → Rules can access memory_snapshot and context_snapshot
  → Returns DecisionResult

TaskRouter submits task:
  → TaskManager.submit()
  → Worker executes task
```

---

## Error Handling

Snapshot collection is fault-tolerant:

- If a provider fails, `None` is assigned to that snapshot
- Decision-making continues with available snapshots
- Errors are logged but do not block event processing
- Rules should handle `None` snapshots gracefully

---

## Explicit Non-Goals

The following are intentionally excluded from v0.5.1:

- snapshot persistence
- snapshot versioning
- snapshot diff/comparison
- automatic snapshot scheduling
- snapshot caching strategies
- snapshot validation

These concerns are reserved for future versions.

---

## Expected Outcome

At completion of v0.5.1:

- modules can expose state as structured snapshots
- decision rules can access system state safely
- snapshot collection is automatic and fault-tolerant
- architectural boundaries remain enforced
- the system remains deterministic and testable

---

## Architectural Principle

> State belongs to modules.  
> Snapshots belong to decisions.  
> Never expose mutable state directly.

---

## Migration from v0.5.0

For modules to participate in snapshot collection:

1. Implement `get_snapshot()` method
2. Return a dictionary with serializable values
3. Ensure snapshots are read-only representations

No changes required to existing decision rules — they can now optionally access snapshots through `DecisionContext`.

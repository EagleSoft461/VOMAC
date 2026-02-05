# VOMAC v0.4.1 — Task Routing & Event-to-Task Mapping

## Overview

VOMAC v0.4.1 introduces **task routing**.

v0.4.0 established the execution infrastructure:

- Task abstraction
- TaskRegistry
- TaskQueue
- Worker execution loop
- Deterministic startup/shutdown

However, v0.4.0 had an intentional limitation:

> The system could execute tasks,  
> but it did not automatically produce them.

v0.4.1 solves this by introducing a routing layer between events and tasks.

---

## Design Goal

The primary goal of v0.4.1 is:

> Enable the system to convert events into tasks  
> in a deterministic and controlled way.

This version enables:

- event observation
- event-to-task mapping
- automatic task submission
- observable execution flow

Without adding intelligence or decision-making.

---

## Core Philosophy

In v0.4.1:

- Events represent *signals*
- Tasks represent *work*
- TaskRouter represents *translation*
- Workers represent *execution*
- Core remains an orchestrator

Routing is mechanical, not cognitive.

---

## Architectural Position

Task routing exists between the event layer and the task system.

```text
EventDispatcher.emit(event)
        ↓
TaskRouter.on_event(event)
        ↓
TaskManager.submit(task_type, payload)
        ↓
TaskQueue.enqueue(task)
        ↓
Worker.dequeue() → execute()
```
The Core remains unaware of task semantics.
---
## Main Component: TaskRouter
### Purpose

TaskRouter is responsible for:

- subscribing to EventDispatcher

- receiving events via on_event(event)

- mapping event types to task types

- submitting tasks to TaskManager

TaskRouter does not:

- execute tasks

- schedule retries

- prioritize tasks

- decide meaning
---
## Routing Model

v0.4.1 uses a deterministic mapping table.

Example:
```text
EXAMPLE_READY → EXAMPLE_READY_TASK
```
Routes are registered at startup:

- TaskRouter.add_route(event_type, handler)

The handler returns:

- **None** → no task created

- **{task_name, payload}** → task submission
---
## Queue Consistency Principle

During implementation, an important architectural rule was enforced:

> There must be exactly one authoritative TaskQueue.

A key fix in v0.4.1 was preventing the ExecutionEngine
from creating its own internal queue.

## Result

- TaskRouter submits tasks into the same queue

- Worker consumes tasks from that same queue

This guarantees deterministic task visibility.
---
## Worker Execution Behavior

The Worker loop in v0.4.1:

- polls the shared TaskQueue

- executes tasks in FIFO order

- logs task execution lifecycle

- stops cleanly on shutdown

The worker is single-threaded and deterministic.
---
## Lifecycle Flow (v0.4.1)
```text
Core.start()
  → Engine.start()
  → TaskRouter.start()
  → ModuleLoader.discover()
  → Module.init()

Example module emits event:
  → EventDispatcher.emit(EXAMPLE_READY)

TaskRouter reacts:
  → Route found
  → Task submitted

Worker executes:
  → task.start()
  → task.execute()
  → task.complete()
```
---
## Explicit Non-Goals

- The following remain out of scope for v0.4.1:

- decision logic

- rule engines

- intelligence

- retries

- priority scheduling

- distributed queues

- persistence

- parallel workers

- task recovery

These features are intentionally postponed.
---
## Expected Outcome

At completion of v0.4.1:

- events can produce tasks

- tasks are executed automatically

- the system is no longer idle by default

- execution remains deterministic

- routing is cleanly separated from task execution

- architecture remains expandable
---
## Architectural Principle

> A system must route work before it can decide work.
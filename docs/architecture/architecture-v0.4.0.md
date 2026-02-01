# VOMAC v0.4.0 — Task Orchestration Architecture
## Overview

VOMAC v0.4.0 introduces **task orchestration**.

Previous versions established the system foundation:

- v0.2.x — lifecycle & event infrastructure

- v0.3.0 — system awareness via memory and context

Version v0.4.0 enables the system to perform work.

This version does not introduce intelligence, reasoning, or AI.

It introduces **execution flow**.
---
## Design Goal

The primary goal of v0.4.0 is:

>Enable the system to create, schedule, and execute tasks
>in a deterministic and controlled manner.

The system must be able to:

- define work units

- queue them

- execute them

- observe their lifecycle

Without interpreting meaning.
---
## Core Philosophy

In v0.4.0:

- Tasks represent work

- Workers execute work

- The Core orchestrates lifecycle only

- Intelligence remains external

Execution is mechanical, not cognitive.
---
## Architectural Position

Task orchestration exists **between events and intelligence**.

```text
Event
  ↓
Task Creation
  ↓
Task Queue
  ↓
Worker Execution
```

The Core remains unaware of task semantics.
---
## Main Components
### Task

A Task represents a single unit of work.

Responsibilities:

- hold payload

- track execution state

- expose <execute()> method

Tasks do not schedule themselves.
---
## TaskRegistry

Maps task names to task classes.

Responsibilities:

- register available task types

- instantiate tasks with payload

The registry contains no execution logic.
---
## TaskManager

Responsible for task creation and scheduling.

Responsibilities:

- request task creation from registry

- enqueue tasks into the task queue

The TaskManager does not execute tasks.
---
## TaskQueue

An in-memory FIFO queue.

Responsibilities:

- store pending tasks

- preserve execution order

- provide dequeue interface

The queue does not interpret task content.
---
## Worker

Responsible for task execution.

Responsibilities:

- poll the queue

- execute tasks

- update task lifecycle state

Workers do not create tasks.
---
## Lifecycle Flow
```text
Core.start()

→ TaskManager.submit()
→ TaskRegistry.create()
→ TaskQueue.enqueue()

Worker loop:
→ dequeue task
→ task.start()
→ task.execute()
→ task.complete()
```

All flows are deterministic.
---
## Explicit Non-Goals

The following are intentionally excluded from v0.4.0:

- distributed queues

- retries

- priority scheduling

- async execution

- parallel workers

- persistence

- task recovery

- AI-based decision logic

These will be introduced in later versions.
---
## Expected Outcome

At completion of v0.4.0:

- the system can perform real work

- execution flow is observable

- architecture remains clean

- task execution is decoupled from intelligence

- worker model is production-expandable
---
## Runtime Behavior (Important)
> In v0.4.0, the system does not actively produce tasks.
> Workers remain idle unless tasks are explicitly submitted.
> This behavior is intentional and reflects the architectural  boundary of this version.

> Task routing and event-to-task mapping will be introduced in v0.4.1.
---
## Architectural Principle

> A system must execute before it can reason.
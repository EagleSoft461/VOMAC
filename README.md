# VOMAC
![Version](https://img.shields.io/badge/version-v0.4.1-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-active%20development-orange)

---

## 🚧 Current Development Phase — v0.4.1
VOMAC is currently in **v0.4.1 — Task Routing & Event-to-Task Mapping**.

This version introduces the missing execution link between events and tasks.

✅ Events can now automatically produce executable tasks.  
❗ No intelligence, reasoning, learning, or decision-making is implemented in this phase.

---

## 🧠 What is VOMAC?

**VOMAC (Vision-Oriented Modular AI Core)** is not an AI model.

It is not:

- a chatbot engine
- an LLM wrapper
- a prompt framework

VOMAC is a **system orchestration core**.

It provides the foundational layer required to coordinate:

- modular components
- decision mechanisms (future)
- task execution
- AI services (future)
- hardware events (future)
- workflow lifecycles

AI becomes a tool —  
the architecture remains the authority.

---

## 🎯 Project Vision

Most AI projects fail not because models are weak,  
but because the surrounding systems are fragile.

VOMAC exists to answer one question:

> How do we design intelligent systems that can grow safely?

The long-term goal is to build a core that supports:

- long-term architectural evolution
- modular replacement
- system-level reasoning (future)
- real-world integration
- explainable behavior

---

## 🧩 Core Principles

- **Architecture First** — structure before intelligence  
- **Event-Driven Design** — loose coupling by default  
- **Modular Expansion** — components evolve independently  
- **AI as a Tool** — not the decision authority  
- **Production Awareness** — logging, config, isolation  

---

## 🏗️ Architecture Overview

```text
+-----------------------------------+
| Core                              |
| Orchestration • Config • Logging  |
+------------------+----------------+
                   |
                   v
+-----------------------------------+
| Modules                           |
| Memory • Decision • Tasks • AI    |
| Hardware • External Services      |
+-----------------------------------+

 ```             
The Core manages the system lifecycle.  
Modules implement domain-specific behaviors.

> Note: The components shown below represent the long-term architecture vision.
> In v0.3.0, the system introduces passive memory and live context modules that observe events without influencing system behavior.
---

## 📦 Current Status

Version: v0.4.1

- Current focus
- task routing layer (Event → Task)
- deterministic task execution pipeline
- worker lifecycle stability
- clean separation of responsibilities
- architecture stabilization 

---

## ✨ Roadmap Overview

| Version | Focus |
|--------:|------------------------------------|
| v0.2.0 |  Architecturestabilization          |
| v0.3.0 |	Memory & context layer             |
| v0.4.0 |	Task orchestration infrastructure  |
| v0.4.1 |	Event → task routing               |
| v0.5.0 |	Decision layer (rule-based)        |
| v0.6.0 |	Intelligence abstraction           |
| v0.7.0 |	AI integration (optional)          |
| v1.0.0 |	Stable orchestration core          |

---

## ⚙️ Running the Project
⚡ Running VOMAC
```bash
python main.py
```
Example output:
```output
[2026-02-05 11:46:38] [INFO] [ROUTER] Route registered: EXAMPLE_READY
[2026-02-05 11:46:38] [INFO] [EVENT_DISPATCHER] Module subscribed: TaskRouter
[2026-02-05 11:46:38] [INFO] [ROUTER] TaskRouter started
[2026-02-05 11:46:38] [INFO] [CORE] System starting
[2026-02-05 11:46:38] [INFO] [ENGINE] Execution engine starting
[2026-02-05 11:46:38] [INFO] [WORKER] Worker loop started
[2026-02-05 11:46:38] [INFO] [ENGINE] Worker started
MODULES PATH: C:\Users\your_username\Desktop\VOMAC\modules
FOUND: ['context', 'example', 'memory']
[2026-02-05 11:46:38] [INFO] [EVENT_DISPATCHER] Module subscribed: Module
[2026-02-05 11:46:38] [INFO] [CONTEXT] Context module initialized
[2026-02-05 11:46:38] [INFO] [EVENT_DISPATCHER] Module subscribed: Module
[2026-02-05 11:46:38] [INFO] [EVENT_DISPATCHER] Module subscribed: Module
[2026-02-05 11:46:38] [INFO] [EXAMPLE] Module initialized
[2026-02-05 11:46:38] [INFO] [EVENT_DISPATCHER] Dispatching event: EXAMPLE_READY
[2026-02-05 11:46:38] [INFO] [ROUTER] Event received: EXAMPLE_READY
[2026-02-05 11:46:38] [INFO] [ROUTER] Submitting task: EXAMPLE_READY_TASK
[2026-02-05 11:46:38] [INFO] [EVENT_DISPATCHER] Module subscribed: Module
[2026-02-05 11:46:38] [INFO] [MEMORY] Memory module initialized
[2026-02-05 11:46:38] [INFO] [EVENT_DISPATCHER] Module subscribed: Module
[2026-02-05 11:46:38] [INFO] [EVENT_DISPATCHER] Module subscribed: Module
[2026-02-05 11:46:38] [INFO] [CORE] System started
System running. Press ENTER to shutdown...[2026-02-05 11:46:39] [INFO] [WORKER] Executing task: ExampleReadyTask
[2026-02-05 11:46:39] [INFO] [TASK] [EXAMPLE_READY_TASK] executed successfully
[2026-02-05 11:46:39] [INFO] [TASK] [EXAMPLE_READY_TASK] executed successfully
[2026-02-05 11:46:39] [INFO] [WORKER] Task completed: ExampleReadyTask


[2026-02-05 11:46:44] [INFO] [CORE] System shutting down
[2026-02-05 11:46:44] [INFO] [CONTEXT] Context module shutdown
[2026-02-05 11:46:44] [INFO] [EXAMPLE] Module shutting down
[2026-02-05 11:46:44] [INFO] [MEMORY] Memory cleared on shutdown
[2026-02-05 11:46:44] [INFO] [ENGINE] Execution engine stopping
[2026-02-05 11:46:44] [INFO] [WORKER] Worker loop stopped
[2026-02-05 11:46:44] [INFO] [ENGINE] Execution engine stopped
[2026-02-05 11:46:44] [INFO] [CORE] System stopped
```
This version validates system startup and shutdown behavior.
---
📄 Documentation
- `/docs`
- `devlog.md`
- `/docs`
- `/docs/architecture`
- `architecture-v0.4.0.md`
- `architecture-v0.4.1.md`
---
⚠️ Project Status
VOMAC is under active development.
The project prioritizes architectural correctness over feature quantity.
Breaking changes may occur before v1.0.0.
---
📜 License
MIT License
---
🤝 Contribution
This project is currently focused on architectural design and experimentation.
Contributions, discussions, and architectural feedback are welcome.
---
🧭 Long-Term Vision
VOMAC aims to become a foundational decision core
capable of integrating with:

REST APIs

Intelligent services

Embedded devices

Hybrid AI systems

The long-term goal is to evolve toward
a production-ready, explainable decision engine.

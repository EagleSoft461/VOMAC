# VOMAC

![Version](https://img.shields.io/badge/version-v0.4.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-active%20development-orange)

---
## 🚧 Current Development Phase — v0.4.0

VOMAC is currently in **v0.4.0 — Task Orchestration Infrastructure** phase.

This version introduces the **execution foundation** of the system.

### Included in this version
- Execution engine lifecycle
- Worker-based execution model
- Task abstraction and registry
- In-memory task queue
- Event-driven orchestration core
- Deterministic startup and shutdown

### Intentionally excluded
- Event → task routing
- Task producers
- Decision logic
- Intelligence or learning

The system may appear idle during runtime.  
This behavior is **expected** and reflects the architectural boundary of v0.4.0.

Task routing will be introduced in **v0.4.1**.

---

## 🧠 What is VOMAC?

VOMAC (Vision-Oriented Modular AI Core) is **not an AI model**.

It is not:
- a chatbot engine
- an LLM wrapper
- a prompt framework

VOMAC is a **system orchestration core**.

It provides the structural foundation required to coordinate:

- modular components
- decision mechanisms
- task execution
- AI services
- hardware events
- workflow lifecycles

AI becomes a tool —  
**the architecture remains the authority.**

---

## 🎯 Project Vision

Most AI projects fail not because models are weak,  
but because the surrounding systems are fragile.

VOMAC exists to answer one question:

> How do we design intelligent systems that can grow safely?

The long-term goal is to build a core that supports:

- long-term architectural evolution
- modular replacement
- system-level reasoning
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

```Text
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
The Core manages lifecycle and execution boundaries.  
Modules implement domain-specific behavior.
---

## 📦 Current Status

**Version:** v0.4.0

Current focus:
- execution infrastructure
- task abstraction
- worker lifecycle
- architectural stabilization
- clean separation of responsibilities

This version establishes the foundation required for future reasoning layers.

---

## ✨ Roadmap Overview

| Version | Focus |
|------|------|
| v0.2.0 | Architecture stabilization |
| v0.3.0 | Memory & context layer |
| v0.4.0 | Task orchestration infrastructure |
| v0.4.1 | Event → task routing |
| v0.5.0 | Decision layer (rule-based) |
| v0.6.0 | Intelligence abstraction |
| v0.7.0 | AI integration (optional) |
| v1.0.0 | Stable orchestration core |

---

## ⚙️ Running the Project

```bash
python main.py
```
Example output:
```output
[2026-02-01 14:23:03] [INFO] [CORE] System starting
[2026-02-01 14:23:03] [INFO] [ENGINE] Execution engine starting
[2026-02-01 14:23:03] [INFO] [ENGINE] Worker started
MODULES PATH: C:\Users\YourName\YourDesktop\VOMAC\modules
FOUND: ['context', 'example', 'memory']
[2026-02-01 14:23:03] [INFO] [EVENT_DISPATCHER] Module subscribed: Module
[2026-02-01 14:23:03] [INFO] [CONTEXT] Context module initialized
[2026-02-01 14:23:03] [INFO] [EVENT_DISPATCHER] Module subscribed: Module
[2026-02-01 14:23:03] [INFO] [EXAMPLE] Module initialized
[2026-02-01 14:23:03] [INFO] [EVENT_DISPATCHER] Dispatching event: EXAMPLE_READY
[2026-02-01 14:23:03] [INFO] [MEMORY] Memory module initialized
[2026-02-01 14:23:03] [INFO] [EVENT_DISPATCHER] Module subscribed: Module       
[2026-02-01 14:23:03] [INFO] [EVENT_DISPATCHER] Module subscribed: Module       
[2026-02-01 14:23:03] [INFO] [CORE] System started
System running. Press ENTER to shutdown...

[2026-02-01 14:47:14] [INFO] [CORE] System shutting down
[2026-02-01 14:47:14] [INFO] [MEMORY] Memory cleared on shutdown
[2026-02-01 14:47:14] [INFO] [ENGINE] Execution engine stopping
[2026-02-01 14:47:14] [INFO] [ENGINE] Execution engine stopped
[2026-02-01 14:47:14] [INFO] [CORE] System stopped
```
This version validates deterministic startup and shutdown behavior.
---
📄 Documentation
- `/docs`
- `decisions`
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

![Version](https://img.shields.io/badge/version-v0.3.0-orange)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-system--awareness-blue)

# VOMAC

## 🚧 Current Development Phase — v0.3.0

VOMAC is currently in **v0.3.0 — System Awareness Layer (Implementation Phase)**.

This version introduces system-level state awareness
through passive memory and live context tracking.

❗ No intelligence, reasoning, learning, or decision-making
is implemented in this phase.

This phase exists to validate the system foundation
before introducing higher-level reasoning in future versions.

**VOMAC (Vision-Oriented Modular AI Core)**  
VOMAC is a modular system orchestration core
designed to evolve toward event-driven and intelligent architectures.

Modern AI systems are not just models.  
Real-world systems require:

- structured decision logic  
- memory and context handling  
- task orchestration  
- modular extensibility  
- observability and control  

**VOMAC focuses on the system — not the model.**

---

## ❓ What is VOMAC?

VOMAC is not an AI model.  
It is not a framework wrapper.  
It is not a chatbot engine.

**VOMAC is a system orchestration core.**

It provides the foundational layer required to coordinate:

- decision mechanisms  
- modular components  
- AI services  
- hardware events  
- workflow execution  

AI becomes a tool —  
**the architecture remains the authority.**

---

## 🎯 Project Vision

Most AI projects fail not because models are weak,  
but because systems around them are fragile.

VOMAC is built to answer one question:

> **How do we design intelligent systems that can grow safely?**

The goal is to create a core that supports:

- long-term evolution  
- modular replacement  
- system-level reasoning  
- real-world integration  

---

## 🧩 Core Principles

- **Architecture First** — structure before intelligence  
- **Event-Driven Design** — loose coupling by default  
- **Modular Expansion** — components can evolve independently  
- **AI as a Tool** — not the decision authority  
- **Production Awareness** — logging, config, isolation  

---

## 🏗️ Architecture Overview

```Text
+-------------------------------+
|           Core                |
| Orchestration • Config • Log  |
+-------------+-----------------+
              |
              v
+---------------------------+
|         Modules           |
|  Memory • Reasoning       |
|  AI • Hardware • Tasks    |
+---------------------------+
 ```             
The Core manages the system lifecycle.  
Modules implement domain-specific behaviors.

> Note: The components shown below represent the long-term architecture vision.
> In v0.3.0, the system introduces passive memory and live context modules that observe events without influencing system behavior.
---

## 📦 Current Status

Version: v0.3.0

Current focus:
- system awareness layer
- memory and context modules
- event-driven state observation
- orchestration core implementation
- module lifecycle standardization
- contract-based extensibility
- centralized configuration access  
- early architectural exploration  

---

## ✨ Roadmap Overview

| Version | Focus |
|--------|-------|
| v0.2.0 | Architecture stabilization |
| v0.3.0 | Memory & context layer | 
| v0.4.0 | Task orchestration engine |
| v0.5.0 | AI module integration |
| v0.6.0 | Hardware bridge |
| v1.0.0 | Stable orchestration core |

---

## 🧪 Example Use Cases

- AI system orchestration  
- autonomous task pipelines  
- hybrid decision systems  
- real-world device integration  
- research & experimentation core  

---

## ⚙️ Running the Project
⚡ Running VOMAC
```bash
python main.py
```
Example output:
```output
[2026-01-23 17:19:16] [INFO] [EVENT_DISPATCHER] Module subscribed: Module
[2026-01-23 17:19:16] [INFO] [CONTEXT] Context module initialized
[2026-01-23 17:19:16] [INFO] [EVENT_DISPATCHER] Module subscribed: Module
[2026-01-23 17:19:16] [INFO] [CORE] Module loaded: context
[2026-01-23 17:19:16] [INFO] [EVENT_DISPATCHER] Module subscribed: Module
[2026-01-23 17:19:16] [INFO] [EXAMPLE] Module initialized
[2026-01-23 17:19:16] [INFO] [EVENT_DISPATCHER] Dispatching event: EXAMPLE_READY    
[2026-01-23 17:19:16] [INFO] [EVENT_DISPATCHER] Module subscribed: Module
[2026-01-23 17:19:16] [INFO] [CORE] Module loaded: example
[2026-01-23 17:19:16] [INFO] [MEMORY] Memory module initialized
[2026-01-23 17:19:16] [INFO] [EVENT_DISPATCHER] Module subscribed: Module
[2026-01-23 17:19:16] [INFO] [EVENT_DISPATCHER] Module subscribed: Module
[2026-01-23 17:19:16] [INFO] [CORE] Module loaded: memory
[2026-01-23 17:19:16] [INFO] [CORE] System started
System running. Press ENTER to shutdown...
[2026-01-23 17:19:18] [INFO] [CORE] System shutting down
[2026-01-23 17:19:18] [INFO] [CONTEXT] Context module shutdown
[2026-01-23 17:19:18] [INFO] [EXAMPLE] Module shutting down
[2026-01-23 17:19:18] [INFO] [MEMORY] Memory cleared on shutdown
[2026-01-23 17:19:18] [INFO] [CORE] System stopped
```
This version validates system startup and shutdown behavior.
---
📄 Documentation
- `/docs`
- `devlog.md`
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

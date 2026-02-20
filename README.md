# VOMAC
![Version](https://img.shields.io/badge/version-v0.5.1-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-active%20development-orange)

---

## 🚧 Current Development Phase — v0.5.1

VOMAC is currently in **v0.5.1 — Snapshot Provider System**.

This version adds structured state snapshots from modules into the decision pipeline.

✅ **v0.5.0** — Rule-based decision layer (Event → DecisionEngine → Task).  
✅ **v0.5.1** — Snapshot providers: Memory and Context expose read-only snapshots; TaskRouter collects them and passes them to DecisionContext so rules can use system state.  
❗ No AI, learning, or external reasoning is implemented yet.

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
- **decision mechanisms** (rule-based, deterministic)
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
Event
  ↓
TaskRouter (collects Memory + Context snapshots)
  ↓
DecisionEngine (rule-based, first-match-wins)
  ↓
TaskManager.submit() → TaskQueue → Worker
```

```text
+-----------------------------------+
| Core                              |
| Orchestration • Config • Logging  |
+------------------+----------------+
                   |
                   v
+-----------------------------------+
| Modules                           |
| Memory • Context • Example • …    |
| (Snapshot providers optional)     |
+-----------------------------------+
```

The Core manages the system lifecycle.  
Modules implement domain-specific behaviors.  
Modules that implement `get_snapshot()` are used as snapshot providers for decisions.

---

## 📦 Current Status

**Version: v0.5.1**

- Rule-based decision layer (v0.5.0)
- Snapshot provider system: Memory & Context feed DecisionContext (v0.5.1)
- Event → snapshot collection → rule evaluation → task submission
- Deterministic task execution pipeline
- Worker lifecycle stability
- Clean separation of responsibilities

---

## ✨ Roadmap Overview

| Version   | Focus                              |
|----------:|-------------------------------------|
| v0.2.0    | Architecture stabilization          |
| v0.3.0    | Memory & context layer              |
| v0.4.0    | Task orchestration infrastructure   |
| v0.4.1    | Event → task routing                |
| v0.5.0    | Decision layer (rule-based)         |
| **v0.5.1**| **Snapshot providers (current)**    |
| v0.6.0    | Intelligence abstraction            |
| v0.7.0    | AI integration (optional)            |
| v1.0.0    | Stable orchestration core           |

---

## ⚙️ Running the Project

```bash
python main.py
```

Example output:

```text
[INFO] [CORE] System starting
[INFO] [ENGINE] Execution engine starting
[INFO] [WORKER] Worker loop started
FOUND: ['context', 'example', 'memory']
[INFO] [CONTEXT] Context module initialized
[INFO] [EXAMPLE] Module initialized
[INFO] [MEMORY] Memory module initialized
[INFO] [CORE] Snapshot provider registered: context
[INFO] [CORE] Snapshot provider registered: memory
[INFO] [ROUTER] TaskRouter started (v0.5.1)
[INFO] [CORE] System started
[INFO] [ROUTER] Event received: EXAMPLE_READY
[INFO] [ROUTER] Memory snapshot: {...}
[INFO] [DECISION] Rule matched: rule_example_ready_first_3
[INFO] [WORKER] Executing task: ExampleReadyTask
...
System running. Press ENTER to shutdown...
[INFO] [CORE] System shutting down
[INFO] [CORE] System stopped
```

---

## 📄 Documentation

- `/docs` — architecture and decisions
- `/docs/architecture` — versioned architecture docs (e.g. `architecture-v0.5.0.md`, `architecture-v0.5.1.md`)
- `devlog.md` — development log
- `roadmap.md` — roadmap details

---

## ⚠️ Project Status

VOMAC is under active development.  
The project prioritizes architectural correctness over feature quantity.  
Breaking changes may occur before v1.0.0.

---

## 📜 License

MIT License

---

## 🤝 Contribution

This project is focused on architectural design and experimentation.  
Contributions, discussions, and architectural feedback are welcome.

---

## 🧭 Long-Term Vision

VOMAC aims to become a foundational decision core capable of integrating with:

- REST APIs
- Intelligent services
- Embedded devices
- Hybrid AI systems

The long-term goal is a production-ready, explainable decision engine.

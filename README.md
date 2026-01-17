# VOMAC

**VOMAC (Vision-Oriented Modular AI Core)**  
is an experimental modular core designed to simulate decision-making,
reasoning, and system coordination for future AI-driven software
and hardware systems.

---

## ❓ Why VOMAC?

Modern systems require more than isolated models.
They require structured decision pipelines, memory,
and controllable logic.

VOMAC focuses on:

- Modular architecture  
- Hybrid intelligence (rules + ML)  
- System-level thinking  
- Long-term extensibility  

---

## 🚀 Current Status

**v0.1.1 — Configurable Decision Core**

Currently implemented:

- Modular pipeline architecture  
  (Input → Memory → Reasoning → Output)

- Config-driven decision threshold (`config.yaml`)

- Deterministic rule-based reasoning

- Structured logging system

- Explainable output format

---

## 🧠 Architecture Overview

Input → Memory → Reasoning → Output

yaml
Kodu kopyala

Each module is designed to remain independent,
allowing future AI models, APIs, or hardware components
to be integrated without breaking the core structure.

---

## ⚙️ Configuration

Decision behavior can be modified without changing code.

`config.yaml`
```yaml
threshold: 70
```
▶️ Running VOMAC
```bash
python main.py
```
Example output:
```output
2026-01-17 13:53:36,910 | INFO | VOMAC started with threshold=70
2026-01-17 13:53:36,910 | INFO | Decision result: {'decision': 'OK', 'reason': 'Value within normal range', 'confidence': 1.0}
{'decision': 'OK', 'reason': 'Value within normal range', 'confidence': 1.0}
```

🧭 Long-Term Vision
VOMAC aims to become a foundational decision core
capable of integrating with:

REST APIs

Intelligent services

Embedded devices

Hybrid AI systems

The long-term goal is to evolve toward
a production-ready, explainable decision engine.

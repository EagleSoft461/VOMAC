# VOMAC — Development Roadmap

This roadmap reflects the architectural evolution of VOMAC.
Each version is designed to be independently meaningful,
testable, and explainable.

The focus is on system stability before intelligence.

---

## ✅ v0.1.1 — Decision Core Prototype (Completed)

**Goal:** Validate basic decision flow and configuration handling.

### Implemented
- Rule-based decision engine
- Configuration-driven thresholds
- Basic logging system
- Input → reasoning → output flow
- Initial architecture exploration

### Limitations Identified
- Core contains business logic
- Pipeline architecture limits scalability
- Tight coupling between components

These limitations motivated the architectural redesign in v0.2.0.

---

## 🚧 v0.2.0 — Architecture Stabilization (Current Focus)

**Goal:** Establish a scalable and modular system foundation.

### Objectives
- Transform Core into orchestration layer
- Introduce event-driven communication
- Standardize module lifecycle
- Centralize configuration management
- Centralize logging system
- Remove business logic from Core

### Must-Have (Release Criteria)
- Core contains no decision logic
- Modules communicate only via events
- Unified module interface
- Deterministic system lifecycle
- At least one example module
- System start → run → shutdown flow

### Explicitly Out of Scope
- Memory algorithms
- Reasoning logic
- AI integration
- Hardware communication

### Success Indicators
- System can boot with multiple modules
- Modules can be added or removed without Core changes
- Event flow can be traced end-to-end via logs

This version focuses purely on architecture.

---

## 🧠 v0.3.0 — Memory & Decision Layer

**Goal:** Introduce system-level thinking capabilities.

### Planned Features
- Short-term memory module
- Long-term memory abstraction
- Decision rules engine
- Context-aware reasoning
- Explainable decision outputs
- Deterministic startup/shutdown behavior
- Predictable resource usage
- Versioned module interfaces

Built on top of the stabilized v0.2.0 architecture.

---

## ⚙️ v0.4.0 — Task Orchestration Engine

**Goal:** Enable complex workflow management.

### Planned Features
- Task representation model
- Task queue system
- Priority handling
- Parallel execution support
- Workflow lifecycle tracking

---

## 🤖 v0.5.0 — AI Module Integration

**Goal:** Integrate AI as a managed system component.

### Planned Features
- AI module abstraction
- NLP / Vision module examples
- Model swap capability
- Inference isolation
- AI output normalization

AI remains a tool, not the system authority.

---

## 🔌 v0.6.0 — Hardware Bridge

**Goal:** Connect digital reasoning with real-world signals.

### Planned Features
- MQTT / WebSocket bridge
- Device event adapters
- Sensor simulation layer
- Hardware-triggered events

---

## 🏁 v1.0.0 — Stable Orchestration Core

**Goal:** Production-ready system foundation.

### Targets
- Clean architecture boundaries
- Stable public interfaces
- Full documentation
- Demo scenarios
- Long-term maintainability
- Deterministic startup/shutdown behavior
- Predictable resource usage
- Versioned module interfaces

This release marks architectural maturity.
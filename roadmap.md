# VOMAC — Development Roadmap

This roadmap reflects the architectural evolution of VOMAC.
Each version is designed to be independently meaningful,
testable, and explainable.

The focus is on system stability before intelligence.

---

## ✅ v0.1.x — Decision Core Prototype (Completed)

**Goal:** Validate basic decision flow and configuration handling.

### Implemented
- Rule-based decision engine
- Configuration-driven thresholds
- Basic logging system
- Input → reasoning → output flow
- Initial architecture exploration

### Limitations Identified
- Core contained business logic
- Pipeline architecture limited scalability
- Tight coupling between components

These limitations motivated the architectural redesign in v0.2.0.

---

## ✅ v0.2.0 — Architecture Stabilization (Completed)

**Goal:** Establish a scalable and modular system foundation.

### Implemented
- Core as orchestration layer only (no business logic)
- Event-driven communication (EventDispatcher)
- Standardized module lifecycle and interface
- Centralized configuration and logging
- System start → run → shutdown flow

---

## ✅ v0.3.0 — Memory & Context Layer (Completed)

**Goal:** Introduce system state awareness without decision logic.

### Implemented
- **Memory** module: event history store (append-only, in-process)
- **Context** module: current system state (last event, counters, lifecycle flags)
- Passive observers only; no task production or reasoning
- ContextSnapshot / memory snapshot concepts for safe read-only exposure

See: `docs/architecture/architecture-v0.3.0.md`, ADR-002, ADR-003.

---

## ✅ v0.4.0 — Task Orchestration Infrastructure (Completed)

**Goal:** Enable the system to execute work units.

### Implemented
- Task model, TaskRegistry, TaskQueue, TaskManager
- ExecutionEngine and Worker(s)
- Deterministic task execution pipeline
- No event→task link yet (tasks submitted manually or by later layers)

See: `docs/architecture/architecture-v0.4.0.md`.

---

## ✅ v0.4.1 — Event → Task Routing (Completed)

**Goal:** Connect events to task submission.

### Implemented
- TaskRouter: listens to events, submits tasks via TaskManager
- Event-to-task mapping (at first, simple mapping table)
- Router runs after modules; event flow drives task execution

See: `docs/architecture/architecture-v0.4.1.md`.

---

## ✅ v0.5.0 — Decision Layer, Rule-Based (Completed)

**Goal:** Deterministic rule-based selection of tasks.

### Implemented
- DecisionEngine: ordered rules, first-match-wins
- Rule: condition(ctx) → bool, action(ctx) → DecisionResult
- DecisionContext (event + payload) and DecisionResult (task + trace)
- TaskRouter builds context, calls DecisionEngine, submits selected task
- No AI; decisions are explicit and explainable

See: `docs/architecture/architecture-v0.5.0.md`.

---

## 🚧 v0.5.1 — Snapshot Provider System (Current)

**Goal:** Feed module state into decisions via read-only snapshots.

### Implemented
- SnapshotProvider interface (`get_snapshot()`)
- Core registers modules that implement `get_snapshot()` as snapshot providers
- TaskRouter collects Memory and Context snapshots before calling DecisionEngine
- DecisionContext extended with `memory_snapshot` and `context_snapshot`
- Rules can use system state without coupling to module internals

See: `docs/architecture/architecture-v0.5.1.md`.

---

## ✅ v0.6.0 — Intelligence Abstraction (Completed)

**Goal:** Abstract how “decisions” are made so different strategies can be plugged in.

### Implemented
- **DecisionStrategy interface** — Abstract base for all decision strategies
- **RuleBasedStrategy** — Original DecisionEngine logic as a strategy implementation
- **DecisionEngine as wrapper** — Delegates to a pluggable strategy
- **Strategy swapping** — Can change strategies at runtime via `set_strategy()`
- **Backward compatibility** — Default behavior unchanged, no migration needed
- **Example strategy** — NoOpStrategy demonstrates pluggability

See: `docs/architecture/architecture-v0.6.0.md`.

---

## 📋 v0.7.0 — AI Integration (Optional) (Planned)

**Goal:** Integrate AI as a managed system component.

### Planned
- AI module abstraction
- Optional NLP / Vision module examples
- Model swap capability, inference isolation
- AI output normalization

AI remains a tool, not the system authority.

---

## 📋 v0.8.0+ — Hardware Bridge (Planned)

**Goal:** Connect digital core with real-world signals.

### Planned
- MQTT / WebSocket bridge
- Device event adapters
- Sensor simulation layer
- Hardware-triggered events

---

## 🏁 v1.0.0 — Stable Orchestration Core (Target)

**Goal:** Production-ready system foundation.

### Targets
- Clean architecture boundaries
- Stable public interfaces
- Full documentation and demo scenarios
- Long-term maintainability
- Deterministic startup/shutdown, predictable resource usage

This release marks architectural maturity.
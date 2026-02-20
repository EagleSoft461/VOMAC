# VOMAC v0.6.0 — Intelligence Abstraction

## Overview

VOMAC v0.6.0 introduces **Intelligence Abstraction** — a strategy pattern that allows pluggable decision-making strategies.

This version refactors the Decision Layer to use a strategy interface, enabling different decision approaches (rule-based, policy-based, scoring, etc.) without changing callers.

---

## Design Goal

The primary goal of v0.6.0 is:

> Abstract decision-making logic so different strategies can be plugged in  
> without modifying the DecisionEngine or its callers.

The system must be able to:

- use a strategy interface for decisions
- swap strategies without changing callers
- maintain backward compatibility (default: RuleBasedStrategy)
- enable future strategies (policy, scoring, AI-based, etc.)

---

## What Changed from v0.5.1

v0.5.1 had a monolithic `DecisionEngine` that directly managed rules.

v0.6.0 introduces:

- **DecisionStrategy interface** — Abstract base for all decision strategies
- **RuleBasedStrategy** — Original DecisionEngine logic as a strategy implementation
- **DecisionEngine as wrapper** — Delegates to a pluggable strategy
- **Strategy swapping** — Can change strategies at runtime via `set_strategy()`

---

## Core Philosophy

In v0.6.0:

- Decision logic is abstracted behind an interface
- Strategies are pluggable and swappable
- Default behavior remains unchanged (backward compatible)
- Future strategies can be added without modifying core code
- DecisionEngine API remains the same for callers

---

## Architectural Position

The Strategy Pattern sits between DecisionEngine and decision logic:

```text
TaskRouter
  ↓
DecisionEngine (wrapper)
  ↓
DecisionStrategy (interface)
  ↓
RuleBasedStrategy (implementation)
  ↓
Rules → DecisionResult
```

---

## Main Components

### DecisionStrategy Interface

Abstract base class defining the decision contract:

```python
class DecisionStrategy(ABC):
    @abstractmethod
    def decide(self, ctx: DecisionContext) -> DecisionResult:
        pass
```

Any class implementing `decide()` can be used as a strategy.

### RuleBasedStrategy

The original DecisionEngine logic, now as a strategy:

- Evaluates rules in registration order
- First-match-wins strategy
- Maintains rule registry
- Same behavior as v0.5.x DecisionEngine

### DecisionEngine (Wrapper)

Delegates to a strategy:

- Default: `RuleBasedStrategy`
- Can swap strategies via `set_strategy()`
- Maintains same API for callers (`decide()`, `register_rule()`)
- `register_rule()` only works with `RuleBasedStrategy`

---

## Strategy Lifecycle

### Default (v0.6.0)

```python
# Core creates DecisionEngine with default strategy
engine = DecisionEngine(logger)
# Internally uses RuleBasedStrategy

# Register rules (works because default is RuleBasedStrategy)
engine.register_rule(rule)
```

### Custom Strategy

```python
# Create custom strategy
custom_strategy = MyCustomStrategy(logger)

# Use it
engine = DecisionEngine(logger, custom_strategy)

# Or swap at runtime
engine.set_strategy(custom_strategy)
```

---

## Example: NoOpStrategy

A simple example strategy that never selects tasks:

```python
class NoOpStrategy(DecisionStrategy):
    def decide(self, ctx: DecisionContext) -> DecisionResult:
        return DecisionResult(
            task_name=None,
            payload={},
            matched_rule="noop",
            evaluated_rules=[]
        )
```

Usage:
```python
engine = DecisionEngine(logger, NoOpStrategy(logger))
# All decisions return "no task"
```

---

## Backward Compatibility

v0.6.0 is **fully backward compatible**:

- `DecisionEngine(logger)` works exactly as before
- `register_rule()` works as before
- `decide()` works as before
- No changes required in `Core` or `TaskRouter`

The only difference is internal structure — decision logic is now in `RuleBasedStrategy` instead of `DecisionEngine`.

---

## Lifecycle Flow (v0.6.0)

```text
Core.start()
  → DecisionEngine(logger) [default: RuleBasedStrategy]
  → register_rule() [delegates to RuleBasedStrategy]

Event arrives:
  → TaskRouter.on_event()
  → DecisionEngine.decide(ctx)
  → RuleBasedStrategy.decide(ctx)
  → Returns DecisionResult
```

---

## Future Strategies

v0.6.0 enables future strategies:

- **PolicyStrategy** — Policy-based decisions (v0.7.0+)
- **ScoringStrategy** — Weighted scoring (v0.7.0+)
- **AIStrategy** — LLM-based decisions (v0.8.0+)
- **HybridStrategy** — Combines multiple strategies

All implement `DecisionStrategy.decide()`.

---

## Explicit Non-Goals

The following are intentionally excluded from v0.6.0:

- actual AI/LLM integration (v0.7.0+)
- policy engine implementation
- scoring algorithm
- strategy composition
- strategy configuration from files

These are reserved for future versions.

---

## Expected Outcome

At completion of v0.6.0:

- decision logic is abstracted behind an interface
- strategies are pluggable and swappable
- backward compatibility is maintained
- future strategies can be added easily
- architecture is ready for intelligence expansion

---

## Architectural Principle

> Abstract before you implement.  
> Strategy before intelligence.  
> Interface before concrete.

---

## Migration from v0.5.1

**No migration needed** — v0.6.0 is backward compatible.

If you want to use a custom strategy:

1. Implement `DecisionStrategy`
2. Pass it to `DecisionEngine(logger, strategy)`
3. Done

No changes required to existing code.

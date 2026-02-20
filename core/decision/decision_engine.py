"""
v0.6.0 — Decision engine as a strategy wrapper.

Delegates to a DecisionStrategy (default: RuleBasedStrategy).
Allows swapping strategies without changing callers.
"""

from typing import Optional

from core.decision.strategy import DecisionStrategy
from core.decision.rule_based_strategy import RuleBasedStrategy
from core.decision.decision_context import DecisionContext
from core.decision.decision_result import DecisionResult
from core.decision.rule import Rule


class DecisionEngine:
    """
    Wrapper that delegates decisions to a pluggable strategy.

    Default strategy: RuleBasedStrategy (same behavior as v0.5.x).
    """

    def __init__(self, logger, strategy: Optional[DecisionStrategy] = None):
        self.logger = logger
        self._strategy: DecisionStrategy = strategy if strategy is not None else RuleBasedStrategy(logger)

    def set_strategy(self, strategy: DecisionStrategy) -> None:
        """Use a different decision strategy (v0.6.0)."""
        self._strategy = strategy
        self.logger.info("DECISION", f"Strategy set: {type(strategy).__name__}")

    def decide(self, ctx: DecisionContext) -> DecisionResult:
        """Delegate to the current strategy."""
        return self._strategy.decide(ctx)

    def register_rule(self, rule: Rule) -> None:
        """Register a rule. Only applies when strategy is RuleBasedStrategy."""
        if isinstance(self._strategy, RuleBasedStrategy):
            self._strategy.register_rule(rule)
        else:
            raise ValueError("register_rule() only supported for RuleBasedStrategy")

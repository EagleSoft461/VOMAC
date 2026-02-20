"""
v0.6.0 — Decision strategy abstraction.

Any component that can "decide" given a DecisionContext
implements this interface. Enables pluggable strategies
(rule-based, policy-based, scoring, etc.).
"""

from abc import ABC, abstractmethod

from core.decision.decision_context import DecisionContext
from core.decision.decision_result import DecisionResult


class DecisionStrategy(ABC):
    """
    Abstract base for decision strategies.

    Implementations: RuleBasedStrategy (default), future: PolicyStrategy, etc.
    """

    @abstractmethod
    def decide(self, ctx: DecisionContext) -> DecisionResult:
        """
        Produce a decision from the given context.

        Args:
            ctx: Event + optional memory/context snapshots.

        Returns:
            DecisionResult with task_name (or None) and payload.
        """
        pass

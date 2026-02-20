"""
v0.6.0 — Example alternative strategy: NoOpStrategy.

This strategy never selects any task. Useful for testing
or disabling decision-making temporarily.
"""

from core.decision.strategy import DecisionStrategy
from core.decision.decision_context import DecisionContext
from core.decision.decision_result import DecisionResult


class NoOpStrategy(DecisionStrategy):
    """
    Strategy that never selects a task.

    Always returns DecisionResult with task_name=None.
    Useful for testing or disabling decisions.
    """

    def __init__(self, logger):
        self.logger = logger

    def decide(self, ctx: DecisionContext) -> DecisionResult:
        """Always return 'no task'."""
        self.logger.info("DECISION", f"NoOpStrategy: ignoring event {ctx.event_type}")
        return DecisionResult(
            task_name=None,
            payload={},
            matched_rule="noop",
            evaluated_rules=[]
        )

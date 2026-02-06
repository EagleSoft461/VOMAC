from typing import List

from core.decision.decision_context import DecisionContext
from core.decision.decision_result import DecisionResult
from core.decision.rule import Rule


class DecisionEngine:
    """
    Deterministic rule-based decision engine.

    Evaluation strategy:
    - rules evaluated in order
    - first match wins
    """

    def __init__(self, logger):
        self.logger = logger
        self.rules: List[Rule] = []

    def register_rule(self, rule: Rule):
        self.rules.append(rule)
        self.logger.info("DECISION", f"Rule registered: {rule.name}")

    def decide(self, ctx: DecisionContext) -> DecisionResult:
        evaluated = []

        self.logger.info("DECISION", f"Decision requested for event: {ctx.event_type}")

        for rule in self.rules:
            evaluated.append(rule.name)

            try:
                if rule.condition(ctx):
                    self.logger.info("DECISION", f"Rule matched: {rule.name}")
                    result = rule.action(ctx)

                    # ensure trace exists
                    return DecisionResult(
                        task_name=result.task_name,
                        payload=result.payload,
                        matched_rule=rule.name,
                        evaluated_rules=evaluated
                    )
            except Exception as e:
                self.logger.error("DECISION", f"Rule failed: {rule.name} -> {e}")

        self.logger.info("DECISION", "No rule matched")

        return DecisionResult(
            task_name=None,
            payload={},
            matched_rule=None,
            evaluated_rules=evaluated
        )
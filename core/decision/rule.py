from dataclasses import dataclass
from typing import Callable

from core.decision.decision_context import DecisionContext
from core.decision.decision_result import DecisionResult


@dataclass(frozen=True)
class Rule:
    """
    A single deterministic rule.

    - condition must be side-effect free
    - action must be deterministic
    """
    name: str
    condition: Callable[[DecisionContext], bool]
    action: Callable[[DecisionContext], DecisionResult]
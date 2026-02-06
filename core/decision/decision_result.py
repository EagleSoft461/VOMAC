from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass(frozen=True)
class DecisionResult:
    """
    Deterministic output of the decision engine.

    If task_name is None, no task should be submitted.
    """
    task_name: Optional[str]
    payload: Dict[str, Any]

    matched_rule: Optional[str]
    evaluated_rules: List[str]
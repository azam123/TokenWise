"""Budget validation utilities."""

from dataclasses import dataclass
from typing import List, Optional, Tuple


@dataclass(frozen=True)
class BudgetResult:
    """Describes whether a token or cost budget was exceeded."""

    within_budget: bool
    token_limit: Optional[int]
    cost_limit: Optional[float]
    actual_tokens: int
    actual_cost: float
    reasons: Tuple[str, ...]


def check_budget(
    actual_tokens: int,
    actual_cost: float,
    token_limit: Optional[int] = None,
    cost_limit: Optional[float] = None,
) -> BudgetResult:
    """Check actual usage against optional token and cost limits.

    A result object is returned instead of raising an exception so callers can
    decide whether to log, warn, reject, or retry the operation.
    """
    if actual_tokens < 0 or actual_cost < 0:
        raise ValueError("actual usage values cannot be negative")
    if token_limit is not None and token_limit < 0:
        raise ValueError("token_limit cannot be negative")
    if cost_limit is not None and cost_limit < 0:
        raise ValueError("cost_limit cannot be negative")

    reasons: List[str] = []

    if token_limit is not None and actual_tokens > token_limit:
        reasons.append("token limit exceeded")
    if cost_limit is not None and actual_cost > cost_limit:
        reasons.append("cost limit exceeded")

    return BudgetResult(
        within_budget=not reasons,
        token_limit=token_limit,
        cost_limit=cost_limit,
        actual_tokens=actual_tokens,
        actual_cost=actual_cost,
        reasons=tuple(reasons),
    )

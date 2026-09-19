"""LLM cost estimation helpers."""

from dataclasses import dataclass


@dataclass(frozen=True)
class CostEstimate:
    """Estimated cost for input and output tokens."""

    input_tokens: int
    output_tokens: int
    input_cost: float
    output_cost: float
    total_cost: float
    currency: str = "USD"


def estimate_cost(
    input_tokens: int,
    output_tokens: int,
    input_price_per_million: float,
    output_price_per_million: float,
    currency: str = "USD",
) -> CostEstimate:
    """Calculate estimated LLM cost.

    Prices are expressed per one million tokens. Keeping pricing as arguments
    makes the function provider-agnostic and easy to update.
    """
    values = {
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
        "input_price_per_million": input_price_per_million,
        "output_price_per_million": output_price_per_million,
    }
    for name, value in values.items():
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError(f"{name} must be a non-negative number")

    if not currency or not isinstance(currency, str):
        raise ValueError("currency must be a non-empty string")

    input_cost = input_tokens * input_price_per_million / 1_000_000
    output_cost = output_tokens * output_price_per_million / 1_000_000

    return CostEstimate(
        input_tokens=int(input_tokens),
        output_tokens=int(output_tokens),
        input_cost=input_cost,
        output_cost=output_cost,
        total_cost=input_cost + output_cost,
        currency=currency.upper(),
    )

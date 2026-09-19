"""Token estimation utilities.

The default estimator is intentionally dependency-free. It provides a useful
approximation for planning and budgeting, not an exact model tokenizer count.
For provider-accurate counts, a model-specific tokenizer can be added later.
"""

from dataclasses import dataclass
import re


@dataclass(frozen=True)
class TokenEstimate:
    """Result returned by the token estimator."""

    characters: int
    words: int
    estimated_tokens: int


def estimate_tokens(text: str) -> TokenEstimate:
    """Estimate token usage for a text string.

    Steps:
    1. Validate the input.
    2. Count characters and word-like groups.
    3. Approximate tokens using a practical four-characters-per-token rule.

    The estimate is deterministic and fast, making it suitable for pre-checks.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    characters = len(text)
    words = len(re.findall(r"\S+", text))

    # A common rough estimate for English text is 1 token per 4 characters.
    estimated_tokens = max(0, (characters + 3) // 4)

    return TokenEstimate(
        characters=characters,
        words=words,
        estimated_tokens=estimated_tokens,
    )

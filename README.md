# TokenWise 🚀

**TokenWise** is a lightweight, open-source Python toolkit for estimating LLM token usage, calculating costs, and checking usage budgets.

It is designed to be **modular, readable, and easy to integrate** into chatbots, RAG pipelines, agents, and other AI applications.

## ✨ Current Features

- 📊 Dependency-free token estimation
- 💰 Input and output cost calculation
- 🛡️ Token and cost budget checks
- 🧩 Small, reusable Python functions
- 🧪 Unit tests for core functionality

## 📦 Installation

```bash
pip install -e .
```

For development:

```bash
pip install -e ".[dev]"
pytest
```

## ⚡ Quick Start

```python
from tokenwise import check_budget, estimate_cost, estimate_tokens

text = "Explain retrieval augmented generation in simple terms."
tokens = estimate_tokens(text)

print(f"Estimated tokens: {tokens.estimated_tokens}")

cost = estimate_cost(
    input_tokens=tokens.estimated_tokens,
    output_tokens=150,
    input_price_per_million=1.00,
    output_price_per_million=2.00,
)

print(f"Estimated cost: ${cost.total_cost:.6f}")

budget = check_budget(
    actual_tokens=tokens.estimated_tokens + 150,
    actual_cost=cost.total_cost,
    token_limit=1_000,
    cost_limit=0.01,
)

if not budget.within_budget:
    print("Budget warning:", ", ".join(budget.reasons))
```

## 🗂️ Project Structure

```text
src/tokenwise/
├── __init__.py   # Public package API
├── tokens.py     # Token estimation
├── cost.py       # Cost calculation
└── budget.py     # Token and cost budget checks
```

> **Note:** The default token estimator is an approximation. Use a provider-specific tokenizer when exact token counts are required.

## 🛣️ Roadmap

- Provider-specific tokenizer adapters
- Prompt analysis and optimization
- RAG context diagnostics
- CLI and JSON reports
- Usage tracking and dashboards

## 📄 License

MIT License. See [LICENSE](LICENSE).

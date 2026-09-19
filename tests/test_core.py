from tokenwise import check_budget, estimate_cost, estimate_tokens


def test_estimate_tokens_returns_useful_counts():
    result = estimate_tokens("Hello world")
    assert result.characters == 11
    assert result.words == 2
    assert result.estimated_tokens == 3


def test_estimate_cost_calculates_input_and_output_costs():
    result = estimate_cost(1_000_000, 500_000, 1.0, 2.0)
    assert result.input_cost == 1.0
    assert result.output_cost == 1.0
    assert result.total_cost == 2.0


def test_check_budget_detects_limit_violations():
    result = check_budget(120, 0.25, token_limit=100, cost_limit=0.20)
    assert result.within_budget is False
    assert len(result.reasons) == 2

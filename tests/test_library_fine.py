import pytest
from src.library_fine import calculate_fine

@pytest.mark.parametrize(
    ("days_overdue", "expected_fine"),
    [
        (0, 0),
        (1, 50),
        (2, 100),
        (5, 250),
        (10, 500),
        (11, 550),
        (20, 1000),
        (100, 5000),
    ],
)

def test_calculate_fine_valid(days_overdue, expected_fine):
    result = calculate_fine(days_overdue)
    assert result == expected_fine
    assert type(result) is int

@pytest.mark.parametrize("days_overdue", [-1, -10])
def test_calculate_fine_negative_days_raises_value_error(days_overdue):
    with pytest.raises(ValueError):
        calculate_fine(days_overdue)

@pytest.mark.parametrize("days_overdue", [1.5, "5", None, True, False, [3]])
def test_calculate_fine_invalid_type_raises_type_error(days_overdue):
    with pytest.raises(TypeError):
        calculate_fine(days_overdue)
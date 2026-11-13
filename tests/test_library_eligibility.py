import pytest
from src.library_eligibility import can_borrow

@pytest.mark.parametrize(
    ("active_loans", "overdue_books", "expected"),
    [
        (0, 0, True),
        (1, 0, True),
        (4, 0, True),
        (5, 0, False),
        (6, 0, False),
        (0, 1, False),
        (3, 2, False),
        (5, 1, False),
    ],
)

def test_can_borrow_valid(active_loans, overdue_books, expected):
    result = can_borrow(active_loans, overdue_books)
    assert result is expected
    assert type(result) is bool

@pytest.mark.parametrize(
    ("active_loans", "overdue_books"),
    [(-1, 0), (0, -1), (-1, -1)],
)

def test_can_borrow_negative_values_raises_value_error(active_loans, overdue_books):
    with pytest.raises(ValueError):
        can_borrow(active_loans, overdue_books)

@pytest.mark.parametrize(
    ("active_loans", "overdue_books"),
    [
        (1.5, 0), (0, 1.5), 
        ("2", 0), (0, "1"), 
        (None, 0), (0, None), 
        (True, 0), (0, False), 
    ],
)

def test_can_borrow_invalid_type_raises_type_error(active_loans, overdue_books):
    with pytest.raises(TypeError):
        can_borrow(active_loans, overdue_books)
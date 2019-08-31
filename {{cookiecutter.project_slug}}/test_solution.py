import pytest
from solution import solution


@pytest.mark.parametrize(('input', 'expected'), [
    # Happy path
    (1, 1),
    # Min parameters
    # Max parameters
    # Negative-Positive transitions.
    ])
def test_solution(input, expected):
    assert solution(input) == expected

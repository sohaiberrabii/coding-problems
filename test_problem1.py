import pytest

from problem1 import solution


@pytest.mark.parametrize(
    "x, y, expected",
    [
        ([13, 5, 6, 2, 5], [5, 2, 5, 13], 6),
        ([14, 27, 1, 4, 2, 50, 3, 1],
         [2, 4, -4, 3, 1, 1, 14, 27, 50], -4)
    ]
)
def test_solution(x, y, expected):
    assert solution(x, y) == expected



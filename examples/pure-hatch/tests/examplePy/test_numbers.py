# tests/examplePy/test_numbers.py
from examplePy.numbers import add_numbers


def test_add_numbers():
    """Test the add_numbers function."""
    # test with positive numbers
    result = add_numbers(2, 3)
    assert result == 5, f"Expected 5, but got {result}"

    # test with negative numbers
    result2 = add_numbers(-1, 4)
    assert result2 == 3, f"Expected 3, but got {result2}"

    # test with zero
    result3 = add_numbers(0, 5)
    assert result3 == 5, f"Expected 5, but got {result3}"
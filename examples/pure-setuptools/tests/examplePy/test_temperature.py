"""Parametrized conversion cases for the example temperature module."""

import pytest

from examplePy import temperature


@pytest.mark.parametrize(
    "value, expected",
    [
        pytest.param(95, 35, id="positive"),
        pytest.param(-13, -25, id="negative"),
        pytest.param(0, -17.7778, id="zero"),
    ],
)
def test_fahrenheit_to_celsius(value, expected):
    """Check known Fahrenheit/Celsius pairs, including zero Fahrenheit."""
    result = temperature.fahrenheit_to_celsius(value)
    assert result == pytest.approx(expected, abs=0.0001)


@pytest.mark.parametrize(
    "value, expected",
    [
        pytest.param(100, 212, id="positive"),
        pytest.param(-20, -4, id="negative"),
        pytest.param(0, 32, id="zero"),
    ],
)
def test_celsius_to_fahrenheit(value, expected):
    """Check known Celsius/Fahrenheit pairs."""
    result = temperature.celsius_to_fahrenheit(value)
    assert result == pytest.approx(expected, abs=0.0001)

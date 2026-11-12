"""Pytest-based unit test examples for the temperature module"""

import pytest

from examplePy import temperature


def test_convert_and_average():
    """
    Test that convert_and_average correctly combines conversion
    and averaging.
    """
    # Test with known values: [0, 10, 20] Celsius
    # Should average to 10 Celsius = 50 Fahrenheit
    temps_celsius = [0, 10, 20]
    result = temperature.convert_and_average(temps_celsius)
    assert abs(result - 50.0) < 0.01

    # Test with different values
    temps_celsius = [0, 100]
    result = temperature.convert_and_average(temps_celsius)
    # Average of 32 and 212 Fahrenheit = 122
    assert abs(result - 122.0) < 0.01


def test_temperature_workflow():
    """
    Test the complete temperature processing workflow.

    This end-to-end test provides sample temperature data in
    Celsius, processes it through the full workflow
    (conversion and averaging), and verifies the output is
    correct.
    """
    # Sample temperature data in Celsius
    temps_celsius = [0, 10, 20]

    # Run the complete workflow
    result = temperature.convert_and_average(temps_celsius)

    # Verify the output
    # Average of 32, 50, and 68 Fahrenheit = 50 Fahrenheit
    assert abs(result - 50.0) < 0.01


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

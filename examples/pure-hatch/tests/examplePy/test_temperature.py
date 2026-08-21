"""Pytest-based unit test examples for the temperature module"""

import math

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


def test_fahrenheit_to_celsius_positive():
    """Test F to C calculation for positive values"""
    value = 95
    expected_result = 35
    result = temperature.fahrenheit_to_celsius(value)

    assert result == expected_result


def test_fahrenheit_to_celsius_negative():
    """Test F to C calculation for negative values"""
    value = -13
    expected_result = -25
    result = temperature.fahrenheit_to_celsius(value)

    assert result == expected_result


def test_fahrenheit_to_celsius_zero():
    """Test F to C calculation for zero"""
    value = 0
    expected_result = -17.7778
    result = temperature.fahrenheit_to_celsius(value)

    # Test that the result is close to the expected value, within tolerances
    assert math.isclose(result, expected_result, abs_tol=0.0001)


def test_celsius_to_fahrenheit_positive():
    """Test C to F calculation for positive values"""
    value = 100
    expected_result = 212
    result = temperature.celsius_to_fahrenheit(value)

    assert result == expected_result


def test_celsius_to_fahrenheit_negative():
    """Test C to F calculation for negative values"""
    value = -20
    expected_result = -4
    result = temperature.celsius_to_fahrenheit(value)

    assert result == expected_result


def test_celsius_to_fahrenheit_zero():
    """Test C to F calculation for zero"""
    value = 0
    expected_result = 32
    result = temperature.celsius_to_fahrenheit(value)

    assert result == expected_result

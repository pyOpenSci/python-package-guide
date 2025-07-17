"""Pytest-based unit test examples for the temperature module"""
import math

from examplePy import temperature


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

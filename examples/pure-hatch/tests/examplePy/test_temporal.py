"""Pytest-based unit test examples for the temporal module"""
import pathlib

import numpy
import pandas
import pytest

from examplePy import temperature, temporal

# Get the path to the test data directory
TEST_DATA = pathlib.Path(__file__).parents[0] / "data"


@pytest.fixture
def temperatures():
    """Pytest fixture for temperature data, used to avoid duplicate code
    in all of our tests."""
    filename = TEST_DATA / "temperatures_testdata.csv"
    df = pandas.read_csv(filename)
    return df


def test_calc_annual_mean(temperatures):
    """Test the calculation of the annual and total mean temperatures in the
    data"""
    expected_mean_1988 = temperature.fahrenheit_to_celsius(56.0)
    expected_mean_final = temperature.fahrenheit_to_celsius(50.78252)

    # Calculate the means
    df_mean, df_final = temporal.calc_annual_mean(temperatures)

    # Compare specific means to validate the calculations
    assert numpy.isclose(
        df_mean.loc[[1988], "Temperature"].iloc[0], expected_mean_1988)
    assert numpy.isclose(df_final.loc["Temperature"], expected_mean_final)


def test_calc_annual_mean_no_data():
    """Negative test - test the calculation of the annual and total mean
    temperatures in the data when given no data results in an empty result"""
    temperatures = pandas.DataFrame(columns=("Year", "Month", "Temperature"))

    # Calculate the means with no data
    df_mean, df_final = temporal.calc_annual_mean(temperatures)

    # Verify the result dataframe is empty
    assert df_mean.empty

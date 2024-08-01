from examplePy.temperature import fahrenheit_to_celsius
import pandas
from typing import Sequence

def calc_annual_mean(df: pandas.DataFrame):
    """Function to calculate the mean temperature for each year and the final mean"""
    # TODO: make this a bit more robust so we can write integration test examples??
    # Calculate the mean temperature for each year
    yearly_means = df.groupby('Year').mean()

    # Calculate the final mean temperature across all years
    final_mean = yearly_means.mean()

    # Return a converted value
    return fahrenheit_to_celsius(yearly_means), fahrenheit_to_celsius(final_mean)

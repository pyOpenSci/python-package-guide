# src/examplePy/temperature.py
def celsius_to_fahrenheit(celsius: float) -> float:
    """
    Convert temperature from Celsius to Fahrenheit.

    Parameters:
        celsius (float): Temperature in Celsius.

    Returns:
        float: Temperature in Fahrenheit.
    """
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """
    Convert temperature from Fahrenheit to Celsius.

    Parameters:
        fahrenheit (float): Temperature in Fahrenheit.

    Returns:
        float: Temperature in Celsius.
    """
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


def average_temperature(temps: list[float]) -> float:
    """
    Calculate average temperature from a list.

    Parameters
    ----------
    temps : list
        List of temperatures.

    Returns
    -------
    float
        Average temperature.
    """
    return sum(temps) / len(temps)


def convert_and_average(temps_celsius: list[float]) -> float:
    """
    Convert list of Celsius temps to Fahrenheit and
    calculate the average.

    Parameters
    ----------
    temps_celsius : list
        List of Celsius temperatures.

    Returns
    -------
    float
        Average temperature in Fahrenheit.
    """
    temps_fahrenheit = [celsius_to_fahrenheit(t)
                        for t in temps_celsius]
    return average_temperature(temps_fahrenheit)

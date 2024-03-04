
def convert_celsius_to_fahrenheit(temperature_celsius):
    """ Functions that converts temperature in ºC to ºF using the formula: °F = (°C x 9/5) + 32

    Args:
        temperature_celsius (float): Temperature in Celsius to convert in Fahrenheit

    Returns:
        float: The temperature in Fahrenheit
    """
    return (temperature_celsius * 9/5) + 32
    
celsius_grades = 35
print(f"How many degrees Fahrenheit is {celsius_grades}ºC? --> {convert_celsius_to_fahrenheit(celsius_grades)}ºF")   # 95ºF

import math

def area_of_circle(radio):
    """ Function that calculates the area of a circle with the expression area = π x r x r

    Args:
        radio (float): radio of the circle

    Returns:
        float: The area of the circle
    """
    return math.pi * radio * radio

radio = 5.3
print(f"The area of a circle of radius {radio} is {area_of_circle(radio)} square meters.")
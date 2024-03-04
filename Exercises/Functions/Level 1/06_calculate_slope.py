
def calculate_slope(x1, y1, x2, y2):
    """ Function that calculates the slope of a linear equation

    Args:
        x1 (float): x of the first point
        y1 (float): y of the first point
        x2 (float): x of the second point
        y2 (float): y of the second point

    Returns:
        float: The slope of the linear equation
    """
    return (y2 - y1) / (x2 - x1)

x1 = 1
y1 = 5
x2 = 3
y2 = 9
# line --> y = 2x + 3

print("The line y = 2x + 3 has 2 points such that (1,5) and (3,9) and its slope is", calculate_slope(x1,y1,x2,y2))  # m = 2.0
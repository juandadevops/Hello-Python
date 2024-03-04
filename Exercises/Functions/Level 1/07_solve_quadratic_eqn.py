# Importing cmath module to handle complex numbers
import cmath  

def solve_quadratic_eqn(a, b, c):
    """ Function that calculates solution set of a quadratic equation ax² + bx + c = 0.

    Args:
        a (float): a value
        b (float): b value
        c (float): c value

    Returns:
        float: Both values result
    """
    # Calculate the discriminant
    discriminant = cmath.sqrt(b**2 - 4*a*c)

    # Calculate the solutions
    solution1 = (-b + discriminant) / (2*a)
    solution2 = (-b - discriminant) / (2*a)

    return solution1, solution2

# Example usage
a = 1
b = -3
c = 2

solutions = solve_quadratic_eqn(a, b, c)
print("Solutions:", solutions)  # Solutions: ((2+0j), (1+0j))
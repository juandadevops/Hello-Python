
def sum_of_odds(number):
    """ Function that takes a number of parameter and it adds all the odd number in that range

    Args:
        number (int): Positive integer number

    Returns:
        int: The sum of all the odd number in that range
    """
    if number < 1:
        return "ERROR: Please provide a positive integer greater than or equal to 1."
    
    total_sum_odds = sum(range(2, number + 1, 2))
    return total_sum_odds 

print(sum_of_odds(5))    # 6
print(sum_of_odds(10))   # 30
print(sum_of_odds(100))  # 2550
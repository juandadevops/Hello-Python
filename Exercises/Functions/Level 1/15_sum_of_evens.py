
def sum_of_evens(number):
    """ Function that takes a number parameter and it adds all the even number in that range

    Args:
        number (int): Positive integer number 

    Returns:
        int: The sum of all the even number in that range
    """
    if number < 1:
        return "ERROR: Please provide a positive integer greater than or equal to 1."
    
    total_sum_evens = sum(range(1, number + 1, 2))
    return total_sum_evens 

print(sum_of_evens(5))    # 9
print(sum_of_evens(10))   # 25
print(sum_of_evens(100))  # 2500
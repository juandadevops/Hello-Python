
def sum_of_numbers(number):
    """ Function that takes a number parameter and it adds all the number in that range

    Args:
        number (int): Positive integer number 

    Returns:
        int: The sum of all the number in that range
    """
    
    if number < 1:
        return "ERROR: Please provide a positive integer greater than or equal to 1."
    
    total_sum = sum(range(1, number + 1))
    return total_sum 
    
print(sum_of_numbers(5))    # 15
print(sum_of_numbers(10))   # 55
print(sum_of_numbers(100))  # 5050
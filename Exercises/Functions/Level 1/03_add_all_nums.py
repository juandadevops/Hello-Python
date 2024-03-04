
def add_all_nums(*values):
    """ Function that takes arbitrary number of arguments and sums all the arguments

    Returns:
        float: The sum of all arguments
    """
    result = 0
    for value in values:
        if type(value) == int or type(value) == float:
            result += value
    return result

print(add_all_nums(4))              # 4
print(add_all_nums(4, 5))           # 9
print(add_all_nums(4, 5, 4))        # 13
print(add_all_nums(4, 5, 4, 5))     # 18
print(add_all_nums(4, 5, 4, 5, 2))  # 20
print(add_all_nums(4, 5, 4, 5, 2, "error", 5))  # 25
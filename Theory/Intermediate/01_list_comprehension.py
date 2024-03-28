##########################
### LIST COMPREHENSION ###
##########################
"""
    List comprehension in Python is a compact way of creating a list from a sequence. 
    It is a short way to create a new list. 
    List comprehension is considerably faster than processing a list using the for loop.
    # syntax --> [i for i in iterable if expression]
"""

###############
## EXAMPLE 1 ##
###############
"""
    For instance if you want to change a string to a list of characters.
"""
# One way
language = 'Python'
lst = list(language) # changing the string to list
print(type(lst))     # <class 'list'>
print(lst)           # ['P', 'y', 't', 'h', 'o', 'n']

# Second way: list comprehension
lst = [i for i in language]
print(type(lst)) # <class 'list'>
print(lst)       # ['P', 'y', 't', 'h', 'o', 'n']

 
###############
## EXAMPLE 2 ##
###############
"""
    For instance if you want to generate a list of numbers
"""
my_original_list = [1, 2, 3, 4, 5, 6]
print(my_original_list)     # [1, 2, 3, 4, 5, 6]

my_list = [i for i in my_original_list]
print(my_list)      # [1, 2, 3, 4, 5, 6]

new_list = [i for i in range(10)]
print(new_list)     # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

my_range = range(10)
print(list(my_range))   # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

new_list = [i * 2 for i in range(10)]
print(new_list)     # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

def sum_five(number):
    return number + 5
new_list = [sum_five(i) for i in range(10)]
print(new_list)     # [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

# It is possible to do mathematical operations during iteration
squares = [i * i for i in range(11)]
print(squares)      # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# It is also possible to make a list of tuples
numbers = [(i, i * i) for i in range(11)]
print(numbers)      # [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]


###############
## EXAMPLE 3 ##
###############
"""
    List comprehension can be combined with if expression
"""
# Generating even numbers
even_numbers = [i for i in range(21) if i % 2 == 0]  # to generate even numbers list in range 0 to 21
print(even_numbers)         # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Generating odd numbers
odd_numbers = [i for i in range(21) if i % 2 != 0]  # to generate odd numbers in range 0 to 21
print(odd_numbers)          # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# Filter numbers: let's filter out positive even numbers from the list below
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_even_numbers = [i for i in numbers if i % 2 == 0 and i > 0]
print(positive_even_numbers)        # [4, 6, 8, 10]

# Flattening a three dimensional array
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [ number for row in list_of_lists for number in row]
print(flattened_list)    # [1, 2, 3, 4, 5, 6, 7, 8, 9]
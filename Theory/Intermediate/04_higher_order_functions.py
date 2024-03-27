##############################
### HIGHER ORDER FUNCTIONS ###
##############################
"""
    In Python functions are treated as first class citizens, allowing you to perform the following operations on functions:
        - A function can take one or more functions as parameters
        - A function can be returned as a result of another function
        - A function can be modified
        - A function can be assigned to a variable
        
    In this section, we will cover:

        - Handling functions as parameters
        - Returning functions as return value from another functions
        - Using Python closures and decorators
"""

#############################
## Function as a Parameter ##
#############################
def sum_one(value):
    return value + 1

def sum_two(value):
    return value + 2

def sum_two_values_and_add_value(value1, value2, function_sum):
    return function_sum(value1 + value2)

print(sum_two_values_and_add_value(5,5,sum_one))    # 11
print(sum_two_values_and_add_value(5,5,sum_two))    # 12


def sum_numbers(nums):  # normal function
    return sum(nums)    # a sad function abusing the built-in sum function :<

def higher_order_function(f, lst):  # function as a parameter
    summation = f(lst)
    return summation
result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result)       # 15


################################
## Function as a Return Value ##
################################
def square(x):          # a square function
    return x ** 2

def cube(x):            # a cube function
    return x ** 3

def absolute(x):        # an absolute value function
    if x >= 0:
        return x
    else:
        return -(x)

def higher_order_function(type): # a higher order function returning a function
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute

result = higher_order_function('square')
print(result(3))       # 9
result = higher_order_function('cube')
print(result(3))       # 27
result = higher_order_function('absolute')
print(result(-3))      # 3


#######################
### Python Closures ###
#######################
"""
    Python allows a nested function to access the outer scope of the enclosing function. This is is known as a Closure. 
    In Python, closure is created by nesting a function inside another encapsulating function and then returning the inner function.
"""
def add_ten(original_number):
    ten = 10
    def add(num):
        return num + ten + original_number
    return add

closure_result = add_ten(5)
print(closure_result(5))    # 20
print(closure_result(10))   # 25

print(add_ten(5)(5))        # 20 


#######################################
### Built-in Higher Order Functions ###
#######################################
"""
    Some of the built-in higher order functions that we cover in this part are map(), filter, and reduce. 
    Lambda function can be passed as a parameter and the best use case of lambda functions is in functions like map, filter and reduce.
"""
numbers = [2, 5, 7, 12, 30, 2, 11] # iterable

###########################
## Python - Map Function ##
###########################
"""
    The map() function is a built-in function that takes a function and iterable as parameters.
    # syntax --> map(function, iterable)
"""
# Example 1 #
def multiply_two(number):
    return number * 2

print(list(map(multiply_two, numbers)))                 # [4, 10, 14, 24, 60, 4, 22]
print(list(map(lambda number: number * 2, numbers)))    # [4, 10, 14, 24, 60, 4, 22]

# Example 2 #
numbers_squared = map(lambda x : x ** 2, numbers)
print(list(numbers_squared))    # [4, 25, 49, 144, 900, 4, 121]

# Example 3 #
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']  # iterable

def change_to_upper(name):
    return name.upper()

names_upper_cased = map(change_to_upper, names)
print(list(names_upper_cased))    # ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']

# Let us apply it with a lambda function
names_upper_cased = map(lambda name: name.upper(), names)
print(list(names_upper_cased))    # ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']


##############################
## Python - Filter Function ##
##############################
"""
    The filter() function calls the specified function which returns boolean for each item of the specified iterable (list). 
    It filters the items that satisfy the filtering criteria.
    # syntax --> filter(function, iterable)
"""
# Example 1 #
def filter_greater_ten(number):
    if number > 10:
        return True
    return False

print(list(filter(filter_greater_ten, numbers)))            # [12, 30, 11]
print(list(filter(lambda number: number > 10, numbers)))    # [12, 30, 11]

# Example 2 #
numbers = [1, 2, 3, 4, 5, 6, 7, 8]  # iterable

def is_odd(num):
    if num % 2 != 0:
        return True
    return False

odd_numbers = filter(is_odd, numbers)
print(list(odd_numbers))       # [1, 3, 5, 7]

##############################
## Python - Reduce Function ##
##############################
"""
    The reduce() function is defined in the functools module and we should import it from this module. 
    Like map and filter it takes two parameters, a function and an iterable. 
    However, it does not return another iterable, instead it returns a single value.
"""
from functools import reduce

# Example 1 #
def sum_two_values(value1, value2):
    return value1 + value2

print(reduce(sum_two_values, numbers))  # 36

# Example 2 #
numbers_str = ['1', '2', '3', '4', '5']  # iterable
def add_two_nums(x, y):
    return int(x) + int(y)

total = reduce(add_two_nums, numbers_str)
print(total)    # 15



#########################
### Python Decorators ###
#########################
"""
    A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure. 
    Decorators are usually called before the definition of a function you want to decorate.
"""
#########################
## Creating decorators ##
#########################
"""
    To create a decorator function, we need an outer function with an inner wrapper function.
"""
# Normal function
def greeting():
    return 'Welcome to Python'

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
g = uppercase_decorator(greeting)
print(g())          # WELCOME TO PYTHON

## Implementation of the example above with a decorator
'''This decorator function is a higher order function
that takes a function as a parameter'''
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
@uppercase_decorator
def greeting():
    return 'Welcome to Python'
print(greeting())   # WELCOME TO PYTHON


#######################################################
## Applying Multiple Decorators to a Single Function ##
#######################################################
'''These decorator functions are higher order functions
that take functions as parameters'''

# First Decorator
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

# Second decorator
def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string

    return wrapper

@split_string_decorator
@uppercase_decorator     # order with decorators is important in this case - .upper() function does not work with lists
def greeting():
    return 'Welcome to Python'
print(greeting())   # ['WELCOME', 'TO', 'PYTHON']


#################################################
## Accepting Parameters in Decorator Functions ##
#################################################
"""
    Most of the time we need our functions to take parameters, so we might need to define a decorator that accepts parameter
"""
def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print("I live in {}".format(para3))
    return wrapper_accepting_parameters

@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print("I am {} {}. I love to teach.".format(
        first_name, last_name, country))

print_full_name("Asabeneh", "Yetayeh",'Finland')    # I am Asabeneh Yetayeh. I love to teach. I live in Finland
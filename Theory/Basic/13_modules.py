### MODULES ###

import my_module
#from 10_functions import sum_two_values

my_module.sumValue(5, 5)
my_module.printValue("Hello Pyhton!")


from my_module import sumValue, printValue as p

sumValue(5, 5)
p("Hello Python!")

## EXISTING MODULES ##
# Using python os module it is possible to automatically perform many operating system tasks. The OS module in Python provides functions for creating, 
# changing current working directory, and removing a directory (folder), fetching its contents, changing and identifying the current directory.
import os
# Getting current working directory
print(os.getcwd())

# The sys module provides functions and variables used to manipulate different parts of the Python runtime environment. Function sys.argv returns a 
# list of command line arguments passed to a Python script. The item at index 0 in this list is always the name of the script, at index 1 is the argument 
# passed from the command line.
import sys
#print(sys.argv[0], argv[1],sys.argv[2])  # this line would print out: filename argument1 argument2
#print('Welcome {}. Enjoy  {} challenge!'.format(sys.argv[1], sys.argv[2]))
print(sys.maxsize)

# The statistics module provides functions for mathematical statistics of numeric data. The popular statistical functions which are defined in this 
# module: mean, median, mode, stdev etc.
from statistics import *
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))       # ~21.1
print(median(ages))     # 22
print(mode(ages))       # 20
print(stdev(ages))      # ~6.1

# Module containing many mathematical operations and constants.
import math
print(math.pi)           # 3.141592653589793, pi constant
print(math.sqrt(2))      # 1.4142135623730951, square root
print(math.pow(2, 3))    # 8.0, exponential function
print(math.floor(9.81))  # 9, rounding to the lowest
print(math.ceil(9.81))   # 10, rounding to the highest
print(math.log10(100))   # 2, logarithm with 10 as base

# A string module is a useful module for many purposes. The example below shows some use of the string module.
import string
print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)        # 0123456789
print(string.punctuation)   # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

# Random numbers
from random import random, randint
print(random())   # it doesn't take any arguments; it returns a value between 0 and 0.9999
print(randint(5, 20)) # it returns a random integer number between [5, 20] inclusive
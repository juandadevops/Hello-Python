### ERROR TYPES ###

## SyntaxError ##
# print "¡Hola comunidad!"  # SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
print("¡Hola Comunidad!")

## NameError ##
# print(language)   # NameError: name 'language' is not defined
language = "Spanish"
print(language)

## IndexError ##
numbers = [1, 2, 3, 4, 5]
# print(numbers[5])   # IndexError: list index out of range
print(numbers[4])


## ModuleNotFoundError ##
# import maths    # ModuleNotFoundError: No module named 'maths'
import math

## AttributeError ##
# print(math.PI)  # AttributeError: module 'math' has no attribute 'PI'. Did you mean: 'pi'?
print(math.pi)

## KeyError ##
my_dict = {"Nombre":"Juan David", "Apellido":"Corrales", "Edad": 35, 1: "Python"}
print(my_dict["Edad"])
# print(my_dict["Apelido"])   # KeyError: 'Apelido'
print(my_dict["Apellido"])


## TypeError ##
# result = 4 + '3'    # TypeError: unsupported operand type(s) for +: 'int' and 'str'
result = 4 + int('3')
# print(numbers["Edad"])  # TypeError: list indices must be integers or slices, not str


## ImportError ##
# from math import PI # ImportError: cannot import name 'PI' from 'math' (unknown location). Did you mean: 'pi'?
from math import pi


## ValueError ##
# print(int('12a'))   # ValueError: invalid literal for int() with base 10: '12a'
print(int('12'))


## ZeroDivisionError ##
# result = 20 / 0     # ZeroDivisionError: division by zero
result = 20 / 1
###################
### ERROR TYPES ###
###################
"""
    When we write code it is common that we make a typo or some other common error. 
    If our code fails to run, the Python interpreter will display a message, containing feedback with information on where the problem occurs and the type of an error. 
    It will also sometimes gives us suggestions on a possible fix.
    Understanding different types of errors in programming languages will help us to debug our code quickly and also it makes us better at what we do.
"""

#################
## SyntaxError ##
#################
"""
    print "¡Hola comunidad!"  --> SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
"""
print("¡Hola Comunidad!")

###############
## NameError ##
###############
"""
    print(language)  --> NameError: name 'language' is not defined
"""
language = "Spanish"
print(language)

################
## IndexError ##
################
"""
    numbers = [1, 2, 3, 4, 5]
    print(numbers[5]) --> IndexError: list index out of range
"""
numbers = [1, 2, 3, 4, 5]
print(numbers[4])

#########################
## ModuleNotFoundError ##
#########################
"""
    import maths --> ModuleNotFoundError: No module named 'maths'
"""
import math

####################
## AttributeError ##
####################
"""
    print(math.PI) --> AttributeError: module 'math' has no attribute 'PI'. Did you mean: 'pi'?
"""
print(math.pi)

##############
## KeyError ##
##############
"""
    my_dict = {"Nombre":"Juan David", "Apellido":"Corrales", "Edad": 35, 1: "Python"}
    print(my_dict["Apelido"]) --> KeyError: 'Apelido'
"""
my_dict = {"Nombre":"Juan David", "Apellido":"Corrales", "Edad": 35, 1: "Python"}
print(my_dict["Apellido"])

###############
## TypeError ##
###############
"""
    result = 4 + '3' --> TypeError: unsupported operand type(s) for +: 'int' and 'str'
    print(numbers["Edad"]) --> TypeError: list indices must be integers or slices, not str
"""
result = 4 + int('3')

#################
## ImportError ##
#################
"""
    from math import PI --> ImportError: cannot import name 'PI' from 'math' (unknown location). Did you mean: 'pi'?
"""
from math import pi

################
## ValueError ##
################
"""
    print(int('12a')) --> ValueError: invalid literal for int() with base 10: '12a'
"""
print(int('12'))

#######################
## ZeroDivisionError ##
#######################
"""
    result = 20 / 0  --> ZeroDivisionError: division by zero
"""
result = 20 / 1
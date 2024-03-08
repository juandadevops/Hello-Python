### EXCEPTION HANDLING ###

from datetime import date
from datetime import datetime

numberOne, numberTwo = 5, 1
#numberTwo = "1 "

# try except else finally

try:
    print(numberOne + numberTwo)
except:
    # Se ejecuta si se produce una excepción
    print("ERROR: Se ha producido un error")
else:   # Opcional
    # Se ejecuta si no se produce una excepción
    print("No se ha producido un error")
finally:    # Opcional
    # Se ejecuta siempre
    print("La ejecución continua")
    
    
    
# Captura de la información de la excepción

# try:
#     name = input('Enter your name:')
#     year_born = input('Year you were born:')
#     age = 2019 - year_born
#     print(f'You are {name}. And your age is {age}.')
# except TypeError:
#     print('Type error occured')
# except ValueError:
#     print('Value error occured')
# except ZeroDivisionError:
#     print('zero division error occured')

# try:
#     name = input('Enter your name:')
#     year_born = input('Year you born:')
#     age = date.today().year - int(year_born)
#     print(f'You are {name}. And your age is {age}.')
# except TypeError:
#     print('Type error occur')
# except ValueError:
#     print('Value error occur')
# except ZeroDivisionError:
#     print('zero division error occur')
# else:
#     print('I usually run with the try block')
# finally:
#     print('I alway run.')
    
try:
    name = input('Enter your name:')
    year_born = input('Year you born:')
    age = 2019 - year_born
    print('You are {name}. And your age is {age}.')
except Exception as ex:
    print(ex)
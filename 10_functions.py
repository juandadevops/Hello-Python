### FUNCTIONS ### 

from math import sqrt
from statistics import mean, median, mode, pstdev, pvariance


print("FUNCTION TEST")
def my_function (test):
    print("Esto es función %d" %(test))
    
    
my_function(2)

print("SUM TWO VALUES FUNCTION")
def sum_two_values (valor1, valor2):
    if((type(valor1) == int or type(valor1) == float) and (type(valor2) == int or type(valor2) == float)):
        result = valor1 + valor2
        print("El resultado la operación %0.2f + %0.2f es igual a %0.2f" %(valor1, valor2, result))
    else:
        print("Se deben pasar como parámetros 2 valores int o float")
    
    
sum_two_values(10, 10)
sum_two_values(4432, 9439)
sum_two_values(10.5, 8.5)
sum_two_values(10.333333, 8.99999)
sum_two_values("1", "9")

print("SUM TWO VALUES FUNCTION WITH RETURN")
def sum_two_values_with_return (valor1, valor2):
    if((type(valor1) == int or type(valor1) == float) and (type(valor2) == int or type(valor2) == float)):
        result = valor1 + valor2
        #print("El resultado la operación %0.2f + %0.2f es igual a %0.2f" %(valor1, valor2, result))
        return result
    else:
        #print("Se deben pasar como parámetros 2 valores int o float")
        return -1
    
print(sum_two_values_with_return(10, 10))
print(sum_two_values_with_return(4432, 9439))
print(sum_two_values_with_return(10.5, 8.5))
print(sum_two_values_with_return(10.333333, 8.99999))
print(sum_two_values_with_return("1", "9"))


print("PRINT NAME")
def print_name (name, surname):
    print(f"{name} {surname}")
    
print_name(surname = "Corrales", name = "Juan David")   # Reordenar parametros indicandoloo
print_name("Juan David", "Corrales")


print("PRINT NAME WITH DEFAULT")
def print_name_with_default (name, surname, alias = "Sin alias"):   # Parametros opcionales / por defecto
    print(f"{name} {surname} {alias}")
    
print_name_with_default("Juan David", "Corrales", "JuandaDevOps")
print_name_with_default("Juan David", "Corrales")


print("PRINT TEXT")
def print_texts(*texts):
    print("Imprimiendo texto con saltos de línea")
    for text in texts:
        print(text.upper())
    
print_texts("Hola", "C#", "JuandaDevOps")
print_texts("Hola", "C#", "JuandaDevOps", "Padel")
print_texts("Hola")


####################################################################
######################## Exercises: Level 2 ########################
####################################################################

######################## EXERCISE 1 ########################
def evens_and_odds(positive_number):
    """Declare a function named evens_and_odds . It takes a positive integer 
        as parameter and it counts number of evens and odds in the number.

    Args:
        positive_number (int): Positive integer
    """
    evens = 0
    odds = 0
    
    if type(positive_number) == int and positive_number > 0:
        while positive_number >= 0:
            if positive_number % 2 == 0:
                evens += 1
            else:
                odds += 1
            positive_number -= 1
        
        print(f"The number of odds are {odds}")
        print(f"The number of evens are {evens}")     
    else:
        print("El parametro debe ser un numero entero positivo")
    
evens_and_odds(100)


######################## EXERCISE 2 ########################
# Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

# Example usage
number = 5
result = factorial(number)
print(f"The factorial of {number} is: {result}")


def factorial_recursive(n):
    if type(n) != int:
        print("Factorial is defined just for integer numbers")
    else:
        if n < 0:
            return "Factorial is not defined for negative numbers"
        elif n == 0 or n == 1:
            return 1
        else:
            return n * factorial_recursive(n - 1)

# Example usage
number = 5
result = factorial_recursive(number)
print(f"The factorial of {number} is: {result}")


######################## EXERCISE 3 ########################
# Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(value):
    if value is None:
        return True
    elif isinstance(value, str) and not value.strip():
        return True
    elif isinstance(value, (list, tuple, dict, set)) and not value:
        return True
    else:
        return False

# Example usage
empty_string = ""
non_empty_string = "Hello, World!"
empty_list = []
non_empty_list = [1, 2, 3]
empty_tuple = ()
non_empty_tuple = (1, 2, 3)


print(f"Is empty string empty? {is_empty(empty_string)}")
print(f"Is non-empty string empty? {is_empty(non_empty_string)}")
print(f"Is empty list empty? {is_empty(empty_list)}")
print(f"Is non-empty list empty? {is_empty(non_empty_list)}")
print(f"Is empty tuple empty? {is_empty(empty_tuple)}")
print(f"Is non-empty tuple empty? {is_empty(non_empty_tuple)}")



######################## EXERCISE 4 ########################
# Write different functions which take lists. They should calculate_mean, calculate_median, 
# calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
def calculate_mean(values):
    
    sum = 0
    result = 0
    len_list = len(values)
    
    for value in values:
        sum += value
    
    result = sum / len_list
    return result

def calculate_median(values):
    list_values = list(values)
    list_values.sort()
    median = 0
    
    len_list = len(list_values)
    if len_list % 2 == 0:
        position = int(len_list / 2)
        median = (list_values[position] + list_values[position - 1]) / 2
        
    else:
        median = list_values[int(len_list / 2)]
    
    return median
    
def calculate_mode(values):
    list_values = list(values)
    list_values.sort()
    moda = 0
    count = 0
    countAux = 0
    
    for i in list_values:
        countAux = list_values.count(i)
        if countAux > count:
            count = countAux
            moda = i
            
    return moda

    
def calculate_range(values):
    list_values = list(values)
    list_values.sort()
    
    min_value = list_values[0]
    max_value = list_values[-1]      
    range = max_value - min_value      
    
    return range
    
def calculate_variance(values):
    list_values = list(values)
    list_values.sort()
    len_list = len(values)
    mean = calculate_mean(list_values)
    variance = 0
    
    for value in values:
        variance += pow((value-mean),2)
    
    return variance / len_list
    
def calculate_std(values):
    list_values = list(values)
    list_values.sort()
    variance = calculate_variance(values)
    return sqrt(variance)
    
values = [2, 4, 4, 1, 1, 2, 1, 3, 4, 4, 11]
print("Operaciones estadísticas con funciones propias")
print(f"Lista: {values}")
print(f"Mean: {calculate_mean(values)}")
print(f"Median: {calculate_median(values)}")
print(f"Mode: {calculate_mode(values)}")
print(f"Range: {calculate_range(values)}")
print(f"Variance: {calculate_variance(values)}")
print(f"Standard Deviation: {calculate_std(values)}")

print("Operaciones estadísticas con librería statistics propia de Python")
print(f"Lista: {values}")
print(f"Mean: {mean(values)}")
print(f"Median: {median(values)}")
print(f"Mode: {mode(values)}")
print(f"Range: {max(values) - min(values)}")
print(f"Variance: {pvariance(values)}")
print(f"Standard Deviation: {pstdev(values)}")
    
####################################################################
######################## Exercises: Level 3 ########################
####################################################################

######################## EXERCISE 1 ########################
# Write a function called is_prime, which checks if a number is prime.
def is_prime(number):
    if type(number) != int or number < 0:
        print("ERROR: El número pasado como parámetro debe ser un número entero positivo")
    elif number == 0:
        print("El cero no es primo porque no se puede dividir entre sí mismo y tampoco se puede escribir como un producto de primos. El cero es un numero aparte de todos")
    elif number == 1:
        print("El número 1 no es primo porque solo tiene un divisor")
    else:
        for n in range(2, number):
            if number % n == 0: 
                print(number, "NO es primo,", n, "es divisor") 
                return False 
            
        print("Es primo") 
        return True
        
is_prime(13) # Es primo
is_prime(165) # 165 NO es primo, 3 es divisor
is_prime(887) # Es primo
is_prime(1542) # 1542 NO es primo, 2 es divisor
is_prime(654977) # 654977 NO es primo, 103 es divisor


######################## EXERCISE 2 ########################
# Write a functions which checks if all items are unique in the list.

def check_unique_items(lista):
    list_values = list(lista)
    list_values.sort()
    len_list = len(lista)
    for i in list_values:
        if list_values.count(i) > 1:
            print("En la lista no todos los items son únicos. Se repite el", i) 
            return False
    
    print("Todos los valores de la lista son únicos")
    return True


lista = [1,2,3,4,5,6,7,8,9,10]
lista2 = [1,2,3,4,5,6,7,8,9,10, 8]
lista3 = [1,2,2,3,5,4,5,6,7,8,9,10, 8]
check_unique_items(lista)
check_unique_items(lista2)
check_unique_items(lista3)



######################## EXERCISE 3 ########################
# Write a function which checks if all the items of the list are of the same data type.
def check_same_data_type(lista):
    


######################## EXERCISE 4 ########################


######################## EXERCISE 5 ########################
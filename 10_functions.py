### FUNCTIONS ### 

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
def calculate_mean(values):
    
    count = 0
    sum = 0
    result = 0
    
    for value in values:
        count += 1
        sum += value
    
    result = sum / count
    return result

def calculate_median(values):
    print("")
    
def calculate_mode(values):
    print("")
    
def calculate_range(values):
    print("")
    
def calculate_variance(values):
    print("")
    
def calculate_std(values):
    print("")
    
values = [2, 4, 5, 6]
print(calculate_mean(values))
print(calculate_median(values))
print(calculate_mode(values))
print(calculate_range(values))
print(calculate_variance(values))
print(calculate_std(values))
    
####################################################################
######################## Exercises: Level 3 ########################
####################################################################

######################## EXERCISE 1 ########################


######################## EXERCISE 2 ########################


######################## EXERCISE 3 ########################


######################## EXERCISE 4 ########################


######################## EXERCISE 5 ########################
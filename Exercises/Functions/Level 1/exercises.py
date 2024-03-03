# Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)

x1 = 1
y1 = 5
x2 = 3
y2 = 9
# line --> y = 2x + 3

print("La línea y = 2x + 3 tiene 2 puntos tal que (1,5) y (3,9) y su pendiente es", calculate_slope(x1,y1,x2,y2))
    

# Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
# Importing cmath module to handle complex numbers
import cmath  

def solve_quadratic_eqn(a, b, c):
    # Calculate the discriminant
    discriminant = cmath.sqrt(b**2 - 4*a*c)

    # Calculate the solutions
    solution1 = (-b + discriminant) / (2*a)
    solution2 = (-b - discriminant) / (2*a)

    return solution1, solution2

# Example usage
a = 1
b = -3
c = 2

solutions = solve_quadratic_eqn(a, b, c)
print("Solutions:", solutions)


# Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(lista):
    
    if type(lista) != list:
        print("ERROR: El parámetro indicado debe ser una lista")
    else:
        print("Items en la lista:")
        for i in lista:
            print(f"Item: {i}")
        
        
lista = [2,5,"Test"]
listaError = 4343
print_list(lista)       # Ok
print_list(listaError)  # ERROR: El parámetro indicado debe ser una lista

# Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list(lista):
    if type(lista) != list:
        print("ERROR: El parámetro indicado debe ser una lista")
    else:
        listaAux = []
        for i in lista[::-1]:
            listaAux.append(i)
        return listaAux
            
print(reverse_list([2,5,"Test"]))  # ['Test', 5, 2]
print(reverse_list([1, 2, 3, 4, 5]))    # [5, 4, 3, 2, 1]

def reverse_list1(lista):
    if type(lista) != list:
        print("ERROR: El parámetro indicado debe ser una lista")
    else:
        lista.reverse()
        return lista

print(reverse_list1(["A", "B", "C"]))   # ["C", "B", "A"]

ffff = "sfffff"
print(ffff.capitalize())
print(ffff.upper())
lista = ["A", "B", "C", "B"]
print(lista.index("B"))

# Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(lista):
    if type(lista) != list:
        return "ERROR: El parámetro proporcionado debe ser una lista"
    else:
        for i in lista:
            if type(i) == str:
                pos = lista.index(i)
                lista[pos] = i.capitalize()
                #lista[pos] = i.upper()
        return lista
    
lista = ["test", "adios", 2, "buscandoO", "hola", "adios", 5.34]
listaError = "adiosError"
print(capitalize_list_items(lista))         # ['Test', 'Adios', 2, 'Buscandoo', 'Hola', 'Adios', 5.34]
print(capitalize_list_items(listaError))    # "ERROR: El parámetro proporcionado debe ser una lista"

# Función complementaria, pero que no se hace comprobaciones previas y solo funciona con listas donde todos sus valores son strings
def capitalize_list_items2(input_list):
    capitalized_list = [item.capitalize() for item in input_list]
    return capitalized_list

# Example usage
original_list = ["apple", "banana", "cherry"]
result = capitalize_list_items2(original_list)

print("Original List:", original_list)
print("Capitalized List:", result)


# Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
def add_item(lista, item):
    if type(lista) != list:
        return "ERROR: ERROR: El parámetro proporcionado debe ser una lista"
    else:
        new_list = lista.copy()  # Create a copy to avoid modifying the original list
        new_list.append(item)
        return new_list
    
original_list = ["apple", "banana", "cherry"]
new_item = "orange"
result = add_item(original_list, new_item)

print("Original List:", original_list)      # ['apple', 'banana', 'cherry']
print("List with Item Added:", result)      # ['apple', 'banana', 'cherry', 'orange']

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat']
numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))      # [2, 3, 7, 9, 5]
        
        
# Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
def remove_item(lista, item):
    if type(lista) != list:
        return "ERROR: ERROR: El parámetro proporcionado debe ser una lista"
    else:
        new_list = lista.copy()  # Create a copy to avoid modifying the original list
        new_list.remove(item)
        return new_list

original_list = ["apple", "banana", "cherry", "orange"]
new_item = "banana"
result = remove_item(original_list, new_item)

print("Original List:", original_list)      # ['apple', 'banana', 'cherry', 'orange']
print("List with Item Added:", result)      # ['apple', 'cherry', 'orange']

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk']
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))           # [2, 7, 9]


# Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
def sum_of_numbers(number):
    
    if number < 1:
        return "ERROR: Please provide a positive integer greater than or equal to 1."
    
    total_sum = sum(range(1, number + 1))
    return total_sum 
    
print(sum_of_numbers(5))    # 15
print(sum_of_numbers(10))   # 55
print(sum_of_numbers(100))  # 5050



# Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(number):
    if number < 1:
        return "ERROR: Please provide a positive integer greater than or equal to 1."
    
    total_sum_odds = sum(range(2, number + 1, 2))
    return total_sum_odds 

print(sum_of_odds(5))    # 6
print(sum_of_odds(10))   # 30
print(sum_of_odds(100))  # 2550

# Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
def sum_of_evens(number):
    if number < 1:
        return "ERROR: Please provide a positive integer greater than or equal to 1."
    
    total_sum_evens = sum(range(1, number + 1, 2))
    return total_sum_evens 

print(sum_of_evens(5))    # 9
print(sum_of_evens(10))   # 25
print(sum_of_evens(100))  # 2500
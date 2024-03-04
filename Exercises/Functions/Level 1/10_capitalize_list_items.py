
def capitalize_list_items(lista):
    """ Function that takes a list as a parameter and it returns a capitalized list of items

    Args:
        lista (list): List with items to capitalize

    Returns:
        list: Capitalized list of items
    """
    if type(lista) != list:
        return "ERROR: The specified parameter must be a list."
    else:
        for i in lista:
            if type(i) == str:
                pos = lista.index(i)
                lista[pos] = i.capitalize()
        return lista
    
lista = ["test", "bye", 2, "searching", "hello", "welcome", 5.34]
listaError = "byeError"
print(capitalize_list_items(lista))         # ['Test', 'Bye', 2, 'Searching', 'Hello', 'Welcome', 5.34]
print(capitalize_list_items(listaError))    # ERROR: The specified parameter must be a list.


# Complementary function, but it does not make previous checks and only works with lists where all its values are strings.
def capitalize_list_items2(input_list):
    capitalized_list = [item.capitalize() for item in input_list]
    return capitalized_list

# Example usage
original_list = ["apple", "banana", "cherry"]
result = capitalize_list_items2(original_list)

print("Original List:", original_list)  # Original List: ['apple', 'banana', 'cherry']
print("Capitalized List:", result)      # Capitalized List: ['Apple', 'Banana', 'Cherry']
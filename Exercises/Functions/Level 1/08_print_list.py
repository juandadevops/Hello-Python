
def print_list(lista):
    """ Function that takes a list as a parameter and it prints out each element of the list

    Args:
        lista (list): List  to print each element of the list
    """
    
    if type(lista) != list:
        print("ERROR: The specified parameter must be a list.")
    else:
        print("Items in the lista:")
        for i in lista:
            print(f"Item: {i}")
        
        
lista = [2,5,"Test"]
listaError = 4343
print_list(lista)       # Ok
print_list(listaError)  # ERROR: The specified parameter must be a list.

def reverse_list(lista):
    """ Function that takes an array as a parameter and it returns the reverse of the array (using loops)

    Args:
        lista (list): List to reverse

    Returns:
        list: Reversed list
    """
    if type(lista) != list:
        print("ERROR: The specified parameter must be a list.")
    else:
        listaAux = []
        for i in lista[::-1]:
            listaAux.append(i)
        return listaAux
            
print(reverse_list([2,5,"Test"]))       # ['Test', 5, 2]
print(reverse_list([1, 2, 3, 4, 5]))    # [5, 4, 3, 2, 1]


def reverse_list1(lista):
    if type(lista) != list:
        print("ERROR: The specified parameter must be a list.")
    else:
        lista.reverse()
        return lista

print(reverse_list1(["A", "B", "C"]))   # ["C", "B", "A"]
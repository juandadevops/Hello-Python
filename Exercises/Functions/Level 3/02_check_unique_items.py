
def check_unique_items(lista):
    """ Function that checks if all items are unique in the list

    Args:
        lista (list): List to check their items

    Returns:
        _type_: True if all items are unique or False is not
    """
    list_values = list(lista)
    list_values.sort()

    for i in list_values:
        if list_values.count(i) > 1:
            print("In the list not all items are unique. It repeats the", i) 
            return False
    
    print("All values in the list are unique")
    return True


lista = [1,2,3,4,5,6,7,8,9,10]
lista2 = [1,2,3,4,5,6,7,8,9,10, 8]
lista3 = [1,2,2,3,5,4,5,6,7,8,9,10, 8]
check_unique_items(lista)   # True --> All values in the list are unique
check_unique_items(lista2)  # False --> In the list not all items are unique. It repeats the 8
check_unique_items(lista3)  # False --> In the list not all items are unique. It repeats the 2

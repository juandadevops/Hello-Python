
def check_same_data_type(lista):
    """ Function that checks if all items of the list are of the same data type

    Args:
        lista (list): List to check their items
    """
    
    if type(lista) != list:
        print("ERROR: Parameter must be a list")
    else:
        tipoDato = type(lista[0])
        
        for i in lista:
            tipoDatoAux = type(i)
            if (tipoDato != tipoDatoAux):
                print("The items in the list are NOT of the same data type.")
                return
            
        print("All items in the list are of the same data type.")
        
lista = [1,2,3,4, 4, 5,6,7,8,9,10]       
lista2 = [1,2,3,4, 4.6, 5,6,7,8,9,10]       
check_same_data_type(lista)     # True --> All items in the list are of the same data type.
check_same_data_type(lista2)    # False --> The items in the list are NOT of the same data type.


## Another implementation more abbreviated
def are_all_same_type(data):
    return all(isinstance(item, type(data[0])) for item in data)

# Example usage
same_type_list = [1, 2, 3, 4, 5]
mixed_type_list = ['three', 2, 'three', 4, 5]

print(f"All items in same_type_list have the same type? {are_all_same_type(same_type_list)}")       # True
print(f"All items in mixed_type_list have the same type? {are_all_same_type(mixed_type_list)}")     # False
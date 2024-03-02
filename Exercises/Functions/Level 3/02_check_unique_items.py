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

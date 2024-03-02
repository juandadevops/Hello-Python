# Write a function which checks if all the items of the list are of the same data type.
def check_same_data_type(lista):
    
    if type(lista) != list:
        print("ERROR: El parámetro debe ser una lista")
    else:
        tipoDato = type(lista[0])
        
        for i in lista:
            tipoDatoAux = type(i)
            if (tipoDato != tipoDatoAux):
                print("Los items de la lista NO son del mismo tipo de dato")
                return
            
        print("Todos los items de la lista son del mismo tipo de dato")
        
lista = [1,2,3,4, 4.6, 5,6,7,8,9,10]       
check_same_data_type(lista)


## Segunda implementación más resumida
def are_all_same_type(data):
    return all(isinstance(item, type(data[0])) for item in data)

# Example usage
same_type_list = [1, 2, 3, 4, 5]
mixed_type_list = ['three', 2, 'three', 4, 5]

print(f"All items in same_type_list have the same type? {are_all_same_type(same_type_list)}")       # Output: True
print(f"All items in mixed_type_list have the same type? {are_all_same_type(mixed_type_list)}")     # Output: False
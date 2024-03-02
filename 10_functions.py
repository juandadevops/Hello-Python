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

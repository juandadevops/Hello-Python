### LOOPS ###

# WHILE
print("BUCLE WHILE")
my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else:   # Opcional
    print("Mi condición es mayor o igual que 10")
    
print("La ejecución continua")

my_condition = 0

while my_condition < 20:
    print(my_condition)
    my_condition += 3
    if my_condition == 15:
        print("Se detiene la ejecución")
        break
    print("Mi condición es menor que 20")
    
    
    
# FOR
print("BUCLE FOR")
my_list = [20, 13, 43, 65, 12, 13, 5, 51]

for element in my_list:
    print(element)
    
my_tuple = (35, 1.77, "Juan David", "Corrales")

for element in my_tuple:
    print(element)

my_set = {"Juan David", "Corrales", 24}

for element in my_set:
    print(element)

my_dict = {
    "Nombre":"Juan David",
    "Apellido":"Corrales",
    "Edad": 24,
    "Lenguajes": {"Python", "Swift", "Kotlin"}
}

for element in my_dict:
    print(element)
    if element == "Edad":
        print("Salir del bucle para el diccionario")
        break
else:
    print("El bucle for para diccionario ha finalizado")
    
print("La ejecución continua")


for element in my_dict:
    print(element)
    if element == "Edad":
        continue
    print("Se ejecuta")
else:
    print("El bucle for para diccionario ha finalizado")
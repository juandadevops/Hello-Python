### DICTIONARIES ### 

my_dict = dict();
my_other_dict = {}

print(type(my_dict))
print(type(my_dict))

my_other_dict = {"Nombre":"Juan David", "Apellido":"Corrales", "Edad": 35, 1: "Python"}

my_dict = {
    "Nombre":"Juan David",
    "Apellido":"Corrales",
    "Edad": 24,
    "Lenguajes": {"Python", "Swift", "Kotlin"}
}


print(my_other_dict)
print(my_dict)

print(len(my_dict))

print(my_dict["Nombre"])

my_dict["Nombre"] = "Luis"
print(my_dict["Nombre"])

print(my_other_dict[1])

my_dict["CP"] = "52400"
print(my_dict)

del my_dict["CP"]
print(my_dict)

print("Corrales" in my_dict)
print("Apellido" in my_dict)
print("Corraleees" in my_dict)

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())
print(dict.fromkeys(("Nombre", "CP")))
my_new_dict = dict.fromkeys(my_dict, "Juanda")
print(my_new_dict)

my_values = my_new_dict.values()
print(my_values)

print(list(my_values))
print(tuple(my_new_dict))
print(set(my_new_dict))
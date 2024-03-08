### SETS ###

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set))

my_other_set = {"Juan David", "Corrales", 24}   # El orden cambia en cada ejecución
print(type(my_other_set))


print(len(my_other_set))


my_other_set.add("Juanda")  # Un set no es una estructura ordenada
print(my_other_set)

my_other_set.add("Juanda")  # Un set no admite repetidos, solo valores únicos
print(my_other_set)

print("Juanda" in my_other_set)
print("Juanda1" in my_other_set)

my_other_set.remove("Juan David")
print(my_other_set)

my_other_set.clear()
print(my_other_set)

del my_other_set    # Elimina toda la variable
# print(my_other_set) --> NameError: name 'my_other_set' is not defined

my_set = {"Juan David", "Corrales", 24}
my_list = list(my_set)
print(type(my_list))
print(my_list)

my_other_set = {"Kotlin", "Swift", "Python"}

my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_set).union({"JavaScript", "C#"}))

print(my_new_set.difference(my_set))
### LISTS ###

list = list()
other_list = []

print(len(list))

list = [23, 23, 24, 31, 51]
print(list)
print(len(list))

other_list = [35, 1.77, "Juan David", "Corrales"]
print(other_list)
print(type(other_list))
print(other_list[0])
print(other_list[1])
print(other_list[-1])
print(other_list[-2])
print(other_list.count("Corrales"))
print(list.count(23))

age, height, name, surname = other_list
print(name)

name = other_list[2]
print(name)

print(list + other_list)

other_list.insert(1, "Azul")
print(other_list)

other_list.remove("Azul")
print(other_list)

list.remove(23)
print(list)

list.pop()
print(list)

list.pop(1)
print(list)

new_list = list.copy()

del list[0]
print(list)

list.clear()
print(list)

print(new_list)
new_list.reverse()
print(new_list)

new_list.sort()
print(new_list)

print(new_list[1:2])
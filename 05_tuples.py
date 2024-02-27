### my_tupleS ###

my_tuple = tuple()
other_my_tuple = ()

my_tuple = (35, 1.77, "Juan David", "Corrales")
other_my_tuple = (32, 43, 4, 5, 10)
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])


print(my_tuple.count(1.77))
print(my_tuple.index("Corrales"))
print(my_tuple.index("Corrales"))

# my_tuple[1] = 1.80 --> TypeError: 'my_tuple' object does not support item assignment

sum_my_tuple = my_tuple + other_my_tuple
print(sum_my_tuple)

print(sum_my_tuple[2:6])

list_my_tuple = list(my_tuple)
print(type(list_my_tuple))
print(list_my_tuple)

list_my_tuple[2] = "Juanda"
list_my_tuple.insert(1, "Azul")
my_tuple_my_tuple = tuple(list_my_tuple)
print(type(my_tuple_my_tuple))
print(my_tuple_my_tuple)

del my_tuple
# print (my_tuple) --> NameError: name 'my_tuple' is not defined
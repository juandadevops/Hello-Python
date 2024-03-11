### LAMBDAS ###

sum_two_values = lambda first_value, second_value: first_value + second_value

print(sum_two_values(5,5))

multiply_values = lambda value1, value2: value1 * value2 - 3
print(multiply_values(5,5))


def sum_three_values(value):
    return lambda value1, value2: value1 + value2 + value


my_sum = sum_three_values(5)(5,5)
print(my_sum)


def power(x):
    return lambda n : x ** n

cube = power(2)(3)   # function power now need 2 arguments to run, in separate rounded brackets
print(cube)          # 8
two_power_of_five = power(2)(5) 
print(two_power_of_five)  # 32
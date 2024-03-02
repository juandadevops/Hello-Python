from math import sqrt
from statistics import mean, median, mode, pstdev, pvariance

# Write different functions which take lists. They should calculate_mean, calculate_median, 
# calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
def calculate_mean(values):
    
    sum = 0
    result = 0
    len_list = len(values)
    
    for value in values:
        sum += value
    
    result = sum / len_list
    return result

def calculate_median(values):
    list_values = list(values)
    list_values.sort()
    median = 0
    
    len_list = len(list_values)
    if len_list % 2 == 0:
        position = int(len_list / 2)
        median = (list_values[position] + list_values[position - 1]) / 2
        
    else:
        median = list_values[int(len_list / 2)]
    
    return median
    
def calculate_mode(values):
    list_values = list(values)
    list_values.sort()
    moda = 0
    count = 0
    countAux = 0
    
    for i in list_values:
        countAux = list_values.count(i)
        if countAux > count:
            count = countAux
            moda = i
            
    return moda

    
def calculate_range(values):
    list_values = list(values)
    list_values.sort()
    
    min_value = list_values[0]
    max_value = list_values[-1]      
    range = max_value - min_value      
    
    return range
    
def calculate_variance(values):
    list_values = list(values)
    list_values.sort()
    len_list = len(values)
    mean = calculate_mean(list_values)
    variance = 0
    
    for value in values:
        variance += pow((value-mean),2)
    
    return variance / len_list
    
def calculate_std(values):
    list_values = list(values)
    list_values.sort()
    variance = calculate_variance(values)
    return sqrt(variance)
    
values = [2, 4, 4, 1, 1, 2, 1, 3, 4, 4, 11]
print("Operaciones estadísticas con funciones propias")
print(f"Lista: {values}")
print(f"Mean: {calculate_mean(values)}")
print(f"Median: {calculate_median(values)}")
print(f"Mode: {calculate_mode(values)}")
print(f"Range: {calculate_range(values)}")
print(f"Variance: {calculate_variance(values)}")
print(f"Standard Deviation: {calculate_std(values)}")

print("Operaciones estadísticas con librería statistics propia de Python")
print(f"Lista: {values}")
print(f"Mean: {mean(values)}")
print(f"Median: {median(values)}")
print(f"Mode: {mode(values)}")
print(f"Range: {max(values) - min(values)}")
print(f"Variance: {pvariance(values)}")
print(f"Standard Deviation: {pstdev(values)}")
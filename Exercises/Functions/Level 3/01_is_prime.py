# Write a function called is_prime, which checks if a number is prime.
def is_prime(number):
    if type(number) != int or number < 0:
        print("ERROR: El número pasado como parámetro debe ser un número entero positivo")
    elif number == 0:
        print("El cero no es primo porque no se puede dividir entre sí mismo y tampoco se puede escribir como un producto de primos. El cero es un numero aparte de todos")
    elif number == 1:
        print("El número 1 no es primo porque solo tiene un divisor")
    else:
        for n in range(2, number):
            if number % n == 0: 
                print(number, "NO es primo,", n, "es divisor") 
                return False 
            
        print("Es primo") 
        return True
        
is_prime(13) # Es primo
is_prime(165) # 165 NO es primo, 3 es divisor
is_prime(887) # Es primo
is_prime(1542) # 1542 NO es primo, 2 es divisor
is_prime(654977) # 654977 NO es primo, 103 es divisor

def is_prime(number):
    """ Function that checks if a number is prime

    Args:
        number (int): Positive number

    Returns:
        _type_: True if the number is prime or False is not
    """
    
    if type(number) != int or number < 0:
        print("ERROR: The number passed as parameter must be a positive integer.")
    elif number == 0:
        print("Zero is not prime because it cannot be divided by itself and it cannot be written as a product of primes either. Zero is a number apart from all")
    elif number == 1:
        print("The number 1 is not prime because it has only one divisor")
    else:
        for n in range(2, number):
            if number % n == 0: 
                print(number, "is NOT prime,", n, "is divisor") 
                return False 
            
        print("It's prime") 
        return True
        
is_prime(13) # It's prime
is_prime(165) # 165 is NOT prime, 3 is divisor
is_prime(887) # It's prime
is_prime(1542) # 1542 is NOT prime, 2 is divisor
is_prime(654977) # 654977 is NOT prime, 103 is divisor
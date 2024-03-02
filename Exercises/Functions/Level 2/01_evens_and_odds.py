
def evens_and_odds(positive_number):
    """It takes a positive integer as parameter and it counts number of evens and odds in the number
    Args:
        positive_number (int): Positive integer
    """
    evens = 0
    odds = 0
    
    if type(positive_number) == int and positive_number > 0:
        while positive_number >= 0:
            if positive_number % 2 == 0:
                evens += 1
            else:
                odds += 1
            positive_number -= 1
        
        print(f"The number of odds are {odds}")
        print(f"The number of evens are {evens}")     
    else:
        print("The parameter must be a positive integer.")
    
evens_and_odds(100)
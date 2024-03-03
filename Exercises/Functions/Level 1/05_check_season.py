
def check_season(month: str):
    """ Function that takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.

    Args:
        month (str): Month of the year
    """
    
    if type(month) != str:
        print("ERROR: The parameter provided must be a string")
        return
        
    month = month.lower()
    if month == "march" or month == "april" or month == "may":
        print("The season is Spring")
    elif month == "june" or month == "july" or month == "august":
        print("The season is Summer")
    elif month == "september" or month == "october" or month == "november":
        print("The season is Autumn")
    elif month == "december" or month == "january" or month == "february":
        print("The season is Winter")
    else:
        print("ERROR: The month indicated as parameter does not exist")

check_season("March")       # The season is Spring
check_season("JulY")       # The season is Summer
check_season("september")  # The season is Autumn
check_season("DECEMBER")   # The season is Winter
check_season(44)            # ERROR: The parameter provided must be a string
check_season("ErrorTest")   # ERROR: The month indicated as parameter does not exist
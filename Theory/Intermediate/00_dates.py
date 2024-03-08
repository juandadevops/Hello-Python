### DATES ###

from datetime import datetime as dt

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(now.timestamp())


now = dt.now()

date = now.strftime("%d/%m/%Y, %H:%M:%S")
print("Datetime:", date)    # dd/mm/YY H:M:S format




print_date(now)

year_2025 = dt(2025, 1, 1)

print_date(year_2025)

from datetime import time

current_time = time(22, 30, 2)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)


from datetime import date

current_date = date.today()

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(2024, 8, 3)

print(current_date.year)
print(current_date.month)
print(current_date.day)
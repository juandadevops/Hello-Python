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


current_date = date(current_date.year, current_date.month + 1, current_date.day)

print(current_date)


diff = year_2025 - now
diff_2 = year_2025.date() - current_date
print(diff) 
print(diff_2) 

# Difference Between Two Points in Time Using timedelata
from datetime import timedelta

start_timedelta = timedelta(200, 100, 100, weeks = 10)
end_timedelta = timedelta(300, 100, 100, weeks = 13)
print (end_timedelta - start_timedelta)
print (end_timedelta + start_timedelta)


# String to Time Using strptime
from datetime import datetime
date_string = "5 December, 2019"
print("date_string =", date_string)
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)


# Formatting Date Output Using strftime
now = dt.now()
date = now.strftime("%d/%m/%Y, %H:%M:%S")
print("Datetime:", date)    # dd/mm/YY H:M:S format
#############
### DATES ###
#############
"""
    Python has got datetime module to handle date and time.
"""
from datetime import datetime as dt


##################################
## Getting datetime Information ##
##################################
"""
    Timestamp or Unix timestamp is the number of seconds elapsed from 1st of January 1970 UTC.
"""
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


#################################################
## Difference Between Two Points in Time Using ##
#################################################
diff = year_2025 - now
diff_2 = year_2025.date() - current_date
print(diff)     # 278 days, 22:38:05.248643
print(diff_2)   # 120 days, 0:00:00


###########################################
## Formatting Date Output Using strftime ##
###########################################
now = dt.now()
date = now.strftime("%d/%m/%Y, %H:%M:%S")
print("Datetime:", date)    # dd/mm/YY H:M:S format (Datetime: 28/03/2024, 01:11:08)


###################################
## String to Time Using strptime ##
###################################
from datetime import datetime
date_string = "5 December, 2019"
print("date_string =", date_string)     # date_string = 5 December, 2019
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)     # date_object = 2019-12-05 00:00:00


##############################
## Using date from datetime ##
##############################
from datetime import date
d = date(2020, 1, 1)
print(d)
print('Current date:', d.today())    # 2024-03-28
# date object of today's date
today = date.today()
print("Current year:", today.year)   # 2024
print("Current month:", today.month) # 03
print("Current day:", today.day)     # 28


####################################
## Time Objects to Represent Time ##
####################################
from datetime import time
# time(hour = 0, minute = 0, second = 0)
a = time()
print("a =", a)     # a = 00:00:00
# time(hour, minute and second)
b = time(10, 30, 50)
print("b =", b)     # c = 10:30:50
# time(hour, minute and second)
c = time(hour=10, minute=30, second=50)
print("c =", c)     # c = 10:30:50
# time(hour, minute, second, microsecond)
d = time(10, 30, 50, 200555)
print("d =", d)     # d = 10:30:50.200555


############################################################
## Difference Between Two Points in Time Using timedelata ##
############################################################
from datetime import timedelta

t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
t3 = t1 - t2
print("t3 =", t3)       # t3 = 86 days, 22:56:50
# ## Dates ## #

from datetime import datetime

def print_date(date):
    print(date.month)
    print(date.day)
    print(date.year)
    print(date.hour)
    print(date.minute)
    print(date.timestamp())

now = datetime.now()

print_date(now)

timestamp = now.timestamp()
print(timestamp)

year_2025 = datetime(2025, 1, 1)

print_date(year_2025)

from datetime import time

current_time = time(21, 6, 0)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)
print(current_time.microsecond)


from datetime import date

current_date = date.today()

print(current_date.day)
print(current_date.month)
print(current_date.year)

current_date = date(current_date.year + 2, current_date.month, current_date.day)
print(current_date)

diff = (year_2025 - now)
print(diff)

diff =(year_2025.date() - current_date)
print(diff)


from datetime import timedelta

init_timedelta = timedelta(200, 100, 100, weeks = 10)
end_timedelta = timedelta(300, 100, 100, weeks = 13)

print(init_timedelta - end_timedelta)
print(init_timedelta + end_timedelta)

#модуль datetime
from datetime import date
from datetime import time
from datetime import datetime, timedelta

print(type(date))
my_date = date(2100, 4, 15)
print(my_date)

print(my_date.day)
print(my_date.year)
print(my_date.month)


print(my_date.isocalendar())

my_time = time(18, 10, 45)
print(my_time)

print(my_date.day)
print(my_date.year)
print(my_date.month)

my_date_time = datetime(2222, 12, 10, 10, 45)
print(my_date_time)
print(my_date_time.year)
print(my_date_time.second)
print(my_date_time.microsecond)

print(my_date_time.now().microsecond)
print(my_date_time.strftime('%d-%b-%Y'))
print(my_date_time.strftime('%d-%b-%Y %H:%M'))


#конвертация даты из строки
date_str = '10/12/2222'
converted_date = datetime.strptime(date_str, '%d/%m/%Y')
print(converted_date)

#
print(timedelta)
print(my_date_time + timedelta(days=100, minutes=120))
print(my_date_time - timedelta(days=100, minutes=120))




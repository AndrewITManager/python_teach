#модуль random
import random

print(random.random())
print(random.randint(1, 10))
print(random.choice('abcdf'))
print(random.choice([1, 10, 6]))
print(random.choices([1, 10, 6, 5, 3], k=2))
my_list = [1, 10, 6, 5, 3]
random.shuffle(my_list)#рандомизированный порядок в списке
print(my_list)

print(''.join(random.choices('ABCDF012345678', k=8)))
#практика кортежи
my_nums = (10, 5, 100, 0)
index_one = my_nums.count(5)
print(index_one)
my_list = list(my_nums)
my_list.append(7)
print(my_list)
my_nums = tuple(my_list)
print(my_nums)
my_tuple = tuple('abc')
print(my_tuple)
my_tuple2 = tuple({'first': 1, 'second': True})
print(my_tuple2)


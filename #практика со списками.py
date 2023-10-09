#практика со списками
my_nums = [10, 50, 0, 5, 5, 100]
print(type(my_nums))
print(dir(my_nums))
res = my_nums.count(5)
print(res)
my_nums.append(25)
print(my_nums)
my_nums.insert(2,-5)
print(my_nums)
my_nums.clear()
print(my_nums)
my_nums.extend('abcdfg')
print(my_nums)
my_nums = [10, 50, 0, 5, 5, 100]
other_nums = my_nums.copy()
my_nums.append(3)
other_nums.clear()

print(id(my_nums))
print(id(other_nums))
print(my_nums, other_nums)
print(len(my_nums))


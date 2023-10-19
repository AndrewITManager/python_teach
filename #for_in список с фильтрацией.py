#for_in список с фильтрацией
all_nums = [-3, 1, 0, 10, -20, 5]
positive_nums = []
for num in all_nums:
    if num > 0:
        positive_nums.append(num)
    
print(positive_nums)
print(all_nums)

#сокрашенный for_in с фильтрацией для списков(list)
all_nums_2 = [-3, 1, 0, 10, -20, 5]
pozitive_nums_1 = [num for num in all_nums_2 if num > 0]
print(pozitive_nums_1)
print(all_nums_2)

#формирование нового наборы в обычном for_in
my_set = {1, 10, 15}
new_set = set()
for val in my_set:
    new_set.add(val * val)

print(new_set)
print(my_set)



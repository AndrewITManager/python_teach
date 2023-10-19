#сокращенны цикл for..in
#для формирования новых последовательностей
#list, dict, tuple, set
#выражение for элемент in последовательность if условие
#пример:
all_nums = [-3, 1, 0, 10, -20, 5]
absolute_nums = []
for num in all_nums:
    absolute_nums.append(abs(num))

print(absolute_nums)
print(all_nums)
#то же но с сокращенным for...in для списков
absolute_nums2 = [abs(num) for num in all_nums]#создание нового списка
print(absolute_nums2)
print(all_nums)



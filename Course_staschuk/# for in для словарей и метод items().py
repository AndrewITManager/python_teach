# for in для словарей и метод items()
my_object = {
    'x': 10,
    'y': True,
}

for item in my_object.items():#метод возвращает последовательность
    key, value = item
    print(key, value)

#
my_object_2 = {
    'x': 10,
    'y': True
}
for key, value in my_object_2.items():#распаковка кортежа
    print(key, value)

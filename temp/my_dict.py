my_dict = {
    'name': 'Andrew',
    'age': 36,
    'height': 81,
    'color_eyes': 'green',
    'weight': 78
}

print(my_dict)
temp_dict = {}
my_dict.update({'auto': 'LADA', 'moto': 'DUCATI'})#добавляет одну или несколько парз к - з
print(my_dict)
print(my_dict.get('name'))#выводит значение по ключу
print(my_dict.get('other', 'No key'))#выводит значение по ключу, если отсутствует второй аргумент
my_dict.pop('auto')#удаляет элемент по ключу
print(my_dict)
print(my_dict.keys())#выводит ключи без значений
print(my_dict.values())#выводит значения без ключей
print(my_dict.items())#выводит пары к - з
dict_two = my_dict.copy()#копия словаря
print(dict_two)
# my_dict.clear()#удаляет все из словаря
# print(my_dict)

dict_key = my_dict.keys()

for k in dict_key:
    print([i for i in k])
    # print(v)

dict_item = my_dict.items()





print('')
x = 0
while x <= 30:
    print(x)
    x += 1

lis = {'asd', 2, 19, 1, 'r', 5}

print(type(lis))


sk = [i for i in range(30)]
print(sk)

print([i for i in range(100) if not i % 2 == 0]) # список NOTчетных до 100

# for i in range(10):
#     print(i)
#     for n in range(20):
#         print(n)


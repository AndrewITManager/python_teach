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
my_dict.clear()#удаляет все из словаря
print(my_dict)
dict_1 = {
    'name': 'Andrey',
    'o_name': 'Akimov',
    'age': 36,
    'heigt': 178,
    'weight': 82

}
dict_2 = {
    'name': 'Andrey',
    'o_name': 'Akimov',
    'age': 35,
    'heigt': 178,
    'weight': 78
}

dict_items_1 = dict_1.items()
dict_items_2 = dict_2.items()
dict_3  = {}
for k, v in dict_items_1:
    for k2, v2 in dict_items_2:
        if k == k2 and not v == v2:
            # print(f"key = {k2} value = {v2}")  
            dict_3.update({k2: v2})

print(dict_3)

dict_value_1 = dict_1.values()
dict_value_2 = dict_2.values()

print(dict_value_1)
print(dict_value_2)

lst = [i for i in dict_value_1]
print(lst)

list_value = []
for i in dict_value_1:
    for e in dict_value_2:
        if i == e:
            list_value.append(e)
print(list_value)






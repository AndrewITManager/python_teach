#задача for_in c
lowercase = {
    'a': 'andrew',
    'b': 'maria',
    'c': 'konstantin',
    'd': 'timofey',
}
upper_case = {k: v.upper() for k, v in lowercase.items()}
print(upper_case)


list_str = ('andrew', 'mari', 'konstantin', 'timofey')
print(type(list_str))
list_str_3 = (value for value in list_str if len(list_str[value]) < 5)
print(list_str)
print(type(list_str))
print(len(list_str[2]))
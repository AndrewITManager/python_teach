#for...in
my_list = [True, 10, 'abc', {}]#цикл для списка

for elem in my_list:
    print(elem)

#цикл для кортежа
video_info = ('1920x1080', True, 27)
for elm in video_info:
    print(elm)

#для словарей
my_object = {
    'x': 10,
    'y': True,
    'z': 'abc',
}
for key in my_object:
    print(key, my_object[key])

for el in [1, 'abc', True]:
    print(type(el))
    print(el)

print(el)
print(dir())


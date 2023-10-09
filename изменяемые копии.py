#
a = 345
print(id(a))
b = a
print(id(b))

num = 10
print(id(10))

other_num = 10
print(id(other_num))


print(id(10))

info = {
    'name': 'Bogdan',
    'is_instructor': True,
}
print(info)
print(id(info))
info_copy = {
    'name': 'Bogdan',
    'is_instructor': True,
}

print(id(info_copy))
info['reviews'] = 5
info_copy['rating'] = 100
print(id(info))
print(info_copy)


info_copy_1 = info.copy()
print(info_copy_1)

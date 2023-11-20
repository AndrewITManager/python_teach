#практика словари
my_disk = {}
print(id(my_disk))
print(type(my_disk))

my_disk['brand'] = 'Samsung'
my_disk['price'] = 80
print(my_disk)
print(id(my_disk))

#print(my_disk.__doc__)
print(my_disk.items())
print(type(my_disk.items()))
print(list(my_disk.keys()))
print(type(my_disk.popitem()))
print(my_disk.popitem())
print(my_disk)
my_disk['brand'] = 'Opel'
my_disk['price'] = 5000
print(my_disk)
new_disk = my_disk.copy()
new_disk['type'] = 'ssd'
print(my_disk)
print(new_disk)

print(len(my_disk))
my_list = [['first', 0], ['second', True]]
my_dict = dict(my_list)
print(my_dict)









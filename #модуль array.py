#модуль array
#для однотипных данных
from array import array

my_int_array = array('i', [4, 5, 10, 5, 7, 5])

# print(my_int_array)
# print(type(my_int_array))

# my_int_array.append(15)
# print(my_int_array)

# my_int_array.append(129)
# print(my_int_array)

# print(my_int_array.count(5))
# print(len(my_int_array))

# my_array_two = array('i', [])
# for elem in my_int_array:
#     my_array_two.append(elem)

# print(f"array two: {my_array_two} ")

# print(my_array_two[2])

with open('my_array.bin', 'wb') as my_file:
    my_int_array.tofile(my_file)

imported_array = array('i')

with open('my_array.bin', 'rb') as my_file:
    imported_array.fromfile(my_file, 3)
    print(imported_array)

imported_array.reverse()
print(imported_array)




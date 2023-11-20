#working with lists
my_lists = [num for num in range(5)]
print(my_lists)
print(f"the second element: {my_lists[1]}")
my_lists.append(6)
my_lists.pop(3)
print(my_lists)



#working with dict
my_dict = {}
print(type(my_dict))
my_dict['name'] = 'Jhon'
my_dict['old'] = 30
print(my_dict['old'])
print(my_dict)
my_dict['city'] = 'New York'
my_dict['old'] = 31
#del my_dict['city']
print(my_dict)
my_dict.pop('city')
print(my_dict)









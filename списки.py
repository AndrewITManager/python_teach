users = [
    {
        'user_id' : 134,
        'user_name' : 'Alice'
    },
    {
        'user_id' : 831,
        'user_name' : 'Bob'
    }
    
]
print(len(users))
print(users[1]['user_id'])
print(users[0]['user_name'])
#42
#добавление в пустой список
happy_smiles = []
happy_smiles.append('one')
happy_smiles.append('two')
happy_smiles.append('free')
happy_smiles.append('six')

print(happy_smiles)

#удаление элемнтов в списке
happy_smiles.pop()
print(happy_smiles)
happy_smiles.pop(0)

#сохранение элемента в списке
removed_element = happy_smiles.pop()
print(removed_element)
print(happy_smiles)

#сортировка списка по возрастанию
post_ids = [245, 151, 762, 167]
post_ids.sort()
print(post_ids)
#сортировка списка по убыванию
post_ids.sort(reverse=True)
print(post_ids)

#конвертация в список
#строк
greeting = "Hello from Python"
greeting_letters = list(greeting)
print(greeting_letters)

#конвертация словарей в список
my_dict = {'a': 10, 'b': True}
my_dict_keys = list(my_dict)
print(my_dict_keys)

#арифметические операции в списках
ratings = [2.5, 5.0, 4.3, 3.7]

print(min(ratings))
print(max(ratings))
print(sum(ratings))
print(sum(ratings)/len(ratings))

#объединение списков
my_ratings = [2.5, 5.0]
other_ratings = [3.7, 4.5, 4.9]
all_ratings = my_ratings + other_ratings
print(all_ratings)

#нарезка списков
first_two_ratings = ratings[:2]
print(first_two_ratings)

middle_ratings = ratings[1:-1]
print(middle_ratings)

last_two_ratings = ratings[-2:]
print(last_two_ratings)

#копирование списка по ссылке
my_cars = ['BMV', 'Mersedes']
copied_cars = my_cars
copied_cars.append('Audi')
print(copied_cars)

print(my_cars)
print(id(my_cars) == id(copied_cars))

#копирование в новый список
#копирование используя slice
copied_cars_2 = my_cars[:]
copied_cars_2.append('Volvo')
print(copied_cars_2)
print(my_cars)
print(id(my_cars) == id(copied_cars_2))

#метод copy
copied_cars_3 = my_cars.copy()
copied_cars_3.append('VAZ')
print(copied_cars_3)
print(my_cars)
print(id(my_cars) == id(copied_cars_3))

#создание списка используя функцию list
copied_cars_4 = list(my_cars)
copied_cars_4.append('GAZ')
print(my_cars)
print(copied_cars_4)
print(id(my_cars) == id(copied_cars_4))
#45
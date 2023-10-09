#передача неизменяемых объектов
def my_fn(a, b):
    print(id(a))
    a = a + 1
    print(id(a))
    c = a + b
    return c
num_one = 10
num_two = 5

res = my_fn(num_one, num_two)
print(res)
print(num_one)
print(id(num_one))

#передача изменяемых объектов
def increase_person_age(person):
    print(id(person))
    person['age'] += 1 #внутри функции не рекомендуется изменять внешние объекты
    return person
person_one = {
    'name': 'Bob',
    'age': 21,
}
print(id(person_one))
increase_person_age(person_one)
print(person_one['age'])

#создание копии объекта
def increase_person_age2(person):
    person_copy = person.copy()
    person_copy['age'] += 1
    return person_copy

new_person = increase_person_age2(person_one)
print(new_person['age'])
print(person_one['age'])

#
def merge_lists_to_dict(list_one, list_two):
    zip_lists = zip(list_one, list_two)
    dict_zip_lists = dict(zip_lists)
    return dict_zip_lists

a = ['sanya', 'durak', 'sovsem']
b = ['kishilo', 'ne', 'tak!!!']

print(merge_lists_to_dict(a, b))


#инструкция if
my_number = 25
if my_number > 0:
    print(my_number, "is positive number")

person_info = {
    'age': 20,
    'name': 'Andrew',
}

if not person_info.get('name'):
    # действия в случаях, если:
    #1. ключа "name" у объекта персон нет
    #2. ключ "name" есть, но его значение ложно
    print("name net")
else: print(f"name {person_info['name']} est")

print(not 0)

num_one = 10
num_two = 5

if (num_one > 0 and
    num_two > 0 and
    isinstance(num_one, int) and 
    isinstance(num_two, int)):
    print("Both numbers are ints and positive")

#соединение строк
print('Hello ' + 'Python')
hello = 'Hello'
world = 'World!'
greeting = hello + ' ' + world
print(greeting)
name = 'Andrew'
#форматирование строк
print(f"{hello} {world}") #f-strings - ф-строки
print(f"Hello {name}") 


my_name = 'Bogdan'
my_hobby = 'running'
time = 8

#info = my_name + ' likes ' + my_hobby + ' at ' + str(time) + " o'clock"

info = f"{my_name} likes {my_hobby} at {str(time)} o\'clock"
print(info)





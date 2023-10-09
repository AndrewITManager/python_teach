#диапазон - упорядочненная неизменяемая последовательность элементов
#диапазон - обычно используется в цыклах
my_range = range(7)
print(type(my_range))#принадлежность к классу
print(my_range)
print(list(my_range))#конвертация в список

#добавление шага в диапазонах
my_range = range(10, 20, 3)#третий аргумент в диапазоне это шаг
print(type(my_range))
print(list(my_range))
print(my_range)
#индексы элементов в диапазонах
print(my_range[0])
print(my_range[1])
print(my_range[2])
print(my_range[3])
#print(my_range[4])
#использование диапазонов в циклах
my_range1 = range(10, 20, 3)
for n in my_range1:
    print(n)


for n in range(12, 25, 5):
    print(n)

print(list(range(12, 25, 5)))

print(my_range.count(10))


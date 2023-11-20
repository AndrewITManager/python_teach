#praktika metodi naborov
my_set = {'abc', 'd', 'f', 'y'}
other_set = {'a', 'f', 'd'}
#пересечение
print(my_set.intersection(other_set))
print(other_set.intersection(my_set))
print(my_set.intersection('abcd'))
#объеденение
print(my_set.union(other_set))
#подмножество
print(other_set.issubset(my_set))
print(my_set.issuperset(other_set))
#разница множеств
print(my_set.difference(other_set))
#удаление элементов из множеств
print(my_set.discard('d'))
print(my_set)
print(my_set.remove('abc'))
print(my_set)
#копирование набора
copied_set = my_set.copy()
my_set.add('t')
copied_set.add('l')
print(my_set)
print(copied_set)
#объединение и отнять пересечение
print(my_set.symmetric_difference(copied_set))









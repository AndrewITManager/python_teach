#генераторы
# nums = (3, 5, 10)

squares = (num * num for num in range(6))#можно выполнять итерацию по любой последовательности
print(squares)
print(type(squares))
# for num in squares:
#     print(num)


# gen = list(squares)
# print(gen)
# print(type(gen))

gen_tuple = tuple(squares)
print(gen_tuple)
print(type(gen_tuple))
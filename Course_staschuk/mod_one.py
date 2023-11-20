#module
# import other as other_module - переименование модуля
# from other import my_name, print_sum - вызов только функций
# from other import my_name, print_sum as sum - вызов только функций и переименование функции
# from other import * - импорт всех переменных 
import other

print(other)
print(type(other))
print(dir(other))
print('')
print(other.my_name)

other.print_sum(5, 2)


#переход к следующей итерации с помощью continue
import random#встроенный модуль в пайтон по умолчанию

random_num = random.randint(1, 5)#randint можно сгенерить случайное число с 1 до 5
while True:
    num = int(input("Gues the number from 1 to 5: "))
    if num != random_num: #совпадение
        print("Try again...")
        continue
    print("Congratulations!", random_num)
    break


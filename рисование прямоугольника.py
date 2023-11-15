print('Введите длину прямоугольника: ')
x = input()
print('Введите ширину прямоугольника: ')
y = input()

for i in range(0, int(x)):
    if i == 0 or i == (int(x) - 1):
        print("-" * int(x))
    if i > 0 and i < (int(x)-2):
        print("|" + (" " * (int(x) - 2)) + "|")



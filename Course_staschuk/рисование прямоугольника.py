print('Введите длину прямоугольника: ')
x = int(input())
print('Введите ширину прямоугольника: ')
y = int(input())

k = 0
if x > y:
    k = x
else:
    k = y
print(k)

for i in range(0, k+1):
    if i == 0 or i == k:
        print("-" * k)
    if i > 0 and i < (y + 1):
        print("|" + ' ' * (x - 2) + "|")
    # if i == 0 or i == k:
    #     print("-" * x)
    # if i > 0 and i < (int(x)-2):
    #     print("|" + (" " * (int(x) - 2)) + "|")



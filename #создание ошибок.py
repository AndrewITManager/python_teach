#создание ошибок
def divide_nums(a, b):
    if b == 0:
        raise ValueError("Second arument can't be 0")#генерация ошибки с помощью райс
    return a / b

try:
    divide_nums(10, 0)  
#except Exception as e:
except ValueError as e:
    print(e)

print('Continue...')

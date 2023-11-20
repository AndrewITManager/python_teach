#обработка ошибок
"""
"""
try:
    pass
except ErrorType:#с определенным кодом ошибки
    pass



try:
    print(10/0)
except ZeroDivisionError:
    print(ZeroDivisionError)
    print("Error - Divizion by zero!")

print('Continue...')


try:
    print('10' / 0)
except ZeroDivisionError as e:
    print(isinstance(e, ZeroDivisionError))
    print(e)
except TypeError as e:
    print(type(e))
    print(e)
else:
    print("There was no error")
finally:
    print('Continue...')

#Любые ошибки в блоке except

try:
    print(10/0)
except Exception as e:
    print(e)

#не рекомендуется делать так
try:
    print(10/0)
except:
    print("Some error occured")




print('Continue...')
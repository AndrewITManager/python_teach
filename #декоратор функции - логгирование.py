#декоратор функции - логгирование
def log_function_call(fn):#функция декоратор
    def wrapper(*args, **kwargs):
        print(f"Function name is {fn.__name__}")#имя функции
        print(f"Function arguments are: {args}, {kwargs}")#значения аргументов
        result = fn(*args, **kwargs)#вызов основной функции
        print(f"Function result: {result}")#вывод результата
        return result
    return wrapper

@log_function_call#вызов функции декоратора
def mult(a, b):#основная функция
    return a * b

print(mult(5, 2))
print('')



@log_function_call
def sum(a, b):
    return a + b

print(sum(45.4, 20.7))


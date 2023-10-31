#функция декоратор - проверка аргуметов
def validate_arguments(fn):
    def wrapper(*args, **kwargs):
        for arg in [*args, *kwargs.values()]:
            if not isinstance(arg, int) and not isinstance(arg, float):
                raise ValueError(f"Type of the {arg} is {type(arg)}",
                "All arguments must be int or float!")

        result = fn(*args, **kwargs)
        return result

    return wrapper

@validate_arguments
def sum_nums(a, b):
    return a + b

try:
    print(sum_nums(7, 2))
    print(sum_nums(10.5, 2.3))
    print(sum_nums(10.5, '2.0'))
except ValueError as e:
    print(e)
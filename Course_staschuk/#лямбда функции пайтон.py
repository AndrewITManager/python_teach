#лямбда функции пайтон
"""
lambda(ключевое слово) parameters(может иметь несколько параметров
): expression(допускает только одно выражение), лямбда функции всегда
анонимные

    """
def mult(a, b):
    return a * b #обычная функция


print(mult(10, 5))

mult2 = lambda a, b: a * b #лямда ф. пишется на одной строке, но так лучше не использовать
print(mult2(10, 5))


#пример2
def greeting(greet):
    return lambda name: f"{greet}, {name}!"


"""
def greeting_two(greet):
    def info(name):
        return f"{greet}, {name}!"
    return info 
"""


morning_greeting = greeting("Good morning")
print(morning_greeting('Andrew'))
evening_greeting = greeting("Good evening")
print(evening_greeting('Andrew'))


#глобальные переменные
c = 5
def my_fn(a, b):
    d = 10
    print(c)
    print(a, b)
    print(dir())# dir - просмотр текущих переменных
    
    
my_fn('abc', 'xyz')
print(dir())#переменные в глобальной области видимости

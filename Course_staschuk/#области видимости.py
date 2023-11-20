#области видимости
a = 10 #глобальные переменные
def my_fn():
    a = True # локальные переменные
    b = 15   #
    print(a)
    print(b)
    
my_fn()

print(a)
#print(b)

#цепочка областей видимости
a = 5


def my_fn1():
    def inner_fn():
        print(a)
    inner_fn()
    
my_fn1()    

#создание глобальной переменной
def my_fn2():
    global v
    v = 10
    
my_fn2()
print(v)
#декораторы
def decorator_function(original_fn):
    def wrapper_function(*args, **kwargs):#универсальные аргументы
        #Some actions before execution of the original_fn
        print("Executed before fuction")

        result = original_fn(*args, **kwargs)#универсальные аргументы
        
        #Some actions after execution of the original_fn
        print("Executed after fuction")

        return result
    return wrapper_function





@decorator_function
def my_function(a, b):
    print("My function")
    return (a, b)

result = my_function(100, 50)
print(result)
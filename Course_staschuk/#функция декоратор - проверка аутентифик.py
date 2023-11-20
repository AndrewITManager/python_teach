#функция декоратор - проверка аутентификации
def is_user_authenticated():
    return False # or True

def check_user_auth(fn):
    def wrapper(*args, **kwargs):
        if is_user_authenticated():
            print("User is authenticated!")
            return fn(*args, **kwargs)
        else: 
            raise Exception("User is NOT authenticated")

    return wrapper

@check_user_auth#с помощью декоратора можно быстро вкл или откл проверку аутентификации пользователя
def do_sensitive_job():
    #Do some tasks only if user is authenticated
    print("Results of some sensitive tasks")

try:
    do_sensitive_job()

except Exception as e:
    print(e)
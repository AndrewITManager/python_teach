import random

def generate_password():
lentch = 12 
# Генерация случайного пароля
password = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(lentch))

return password
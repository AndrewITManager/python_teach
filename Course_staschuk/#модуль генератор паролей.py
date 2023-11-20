#модуль генератор паролей
import secrets
import string

all_chars = string.ascii_letters + string.digits + string.punctuation
n = 20
print(''.join(secrets.choice(all_chars) for i in range(n))) #генератор пароля

# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
# print(string.digits)

# print(string.ascii_letters + string.digits + string.punctuation)



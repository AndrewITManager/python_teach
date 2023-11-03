#модуль sys
import sys

print(sys.argv)

if len(sys.argv) < 3:# генерация ошибки при запуске программы без аргументов
    raise IOError("You must provide username and password")

# username = sys.argv[1]
# password = sys.argv[2]

# # РАСПАКОВКА СПИСКА НИЖЕ
filename, username, password = sys.argv

print(username, password)
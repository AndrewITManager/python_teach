#проверка пароля
import re

# test_password = 'dfjAJNJN!@2323'

def chek_password(password):
    lenght_pattern = re.compile(r"\S{8,}") #проверка длины
    lowercase_pattern = re.compile(r"^.*[a-z]+.*$")#буквы в нижнем регистре
    uppercase_pattern = re.compile(r"^.*[A-Z]+.*$")#заглавные буквы
    number_pattern = re.compile(r"^.*[0-9]+.*$")#цыфры
    special_symbol_pattern = re.compile(r"^.*[@%#!&*^]+.*$")#спец символы
    no_wightspace_pattern = re.compile(r"^\S*$")

    
    if not re.fullmatch(no_wightspace_pattern, password):
        return (False, "No whitespaces allowed in the password!")
    if not re.fullmatch(lenght_pattern, password):
        return (False, "Password must have at least 8 symbols")
    if not re.fullmatch(lowercase_pattern, password):
        return (False, "Password must have at least one lowercase letter")
    if not re.fullmatch(uppercase_pattern, password):
        return (False, "Password must have at least one uppercasre letter")
    if not re.fullmatch(number_pattern, password):
        return (False, "Password must have at least one number")
    if not re.fullmatch(special_symbol_pattern, password):
        return (False, "Password must have at least one special symbol @%#!&*^ ")
    return (True, "Password is valid!")
    
    
    
    
    
# print(chek_password('123'))
# print(chek_password('12345678'))
# print(chek_password('12334545AS'))
# print(chek_password('asdaASDFFG'))
# print(chek_password('123asdfASD'))
# print(chek_password('123asdfASD !#$'))

while True:
    password = input("Please enter password: ")
    password_check_res = chek_password(password)
    if password_check_res[0]:
        print(password_check_res[1])
        break
    print(password_check_res[1])


import getpass
from cryptography.fernet import Fernet
import json
import os 
import logging


# Натсройка логгера
logging.basicConfig(filename='log.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')
PASSWORD_FILE = "password.json"
KEY_FILE = "key.key"

def generate_key():
  """Генерирует и сохраняет ключ шифрования"""
  key = Fernet.generate_key()
  with open(KEY_FILE, "wb") as file:
    file.write(key)  
  return key 

def load_key():
  """ Загружает ключ шифрования из файла"""
  return open(KEY_FILE, "rb").read()

def encrypt_data(data, key):
  """Шифрует данные с использованием ключа.""" 
  encrypted_data = Fernet(key).encrypt(data.encode())
  return encrypted_data

def decrypt_data(encrypted_data, key):
  """Расшифровывает данные с использованием ключа.""" 
  decrypted_data = Fernet(key).decrypt(encrypted_data)
  return decrypted_data.decode()

# Функция для проверки сложности пароля
def is_password_strong(password):
  if len(password) < 5:
    return False
  has_digit = any(char.isdigit() for char in password)
  has_upper = any(char.isupper() for char in password)
  has_lower = any(char.islower() for char in password)
  # has_special = any(char in '!@#$%^&*()' for char in password)
  return has_digit and has_upper and has_lower

def get_password(prompt, show_password=False):
  """ Получение пароля от пользователя с возможностью отображения ввода"""
  if show_password:
    return input(prompt)
  else:
    return getpass.getpass(prompt)

def create_and_store_password():
  """ Создает и сохраняет пароль в файле JSON."""
  if os.path.exists(PASSWORD_FILE) and os.path.exists(KEY_FILE):
    logging.warning(' Попытка создания нового пароля, когда зашифрованный файл уже существует.')
    print('Зашифрованный файл пароля уже существует.')

  key = generate_key()

  while True:
    # Создание и сохранение пароля
    show_password = input("Хотите ли вы видеть вводимый пароль? (да/нет)").lower() == 'да'
    created_password = get_password('Создайте пароль: ', show_password)
    confirm_password = get_password('Потвердите пароль: ', show_password)

    if created_password != confirm_password:
      logging.warning(' Пароли не совпадают при попытке создания')
      print('Пароли не совпадают. Попробуйте еще раз.')
      continue

    if is_password_strong(created_password):
      encrypted_password = encrypt_data(created_password, key)
      password_data = {"password": encrypted_password.decode()}
      with open(PASSWORD_FILE, 'w') as file:
        json.dump(password_data, file)
      logging.info("Пароль успешно создан и сохранен")
      print(" Пароль успешно создан и сохранен")
      break
    else:
      logging.warning(" Попытка создания слабого пароля")
      print(f'Пароль слишком простой. Используйте комбинацию цифр, заглавных и строчных букв.')

def user_interface():
  """ Интерфейс пользователя для работы с менеджером паролей."""
  print('Добро пожаловать в менеджер паролей!')

  if not os.path.exists(PASSWORD_FILE) or not os.path.exists(KEY_FILE):
    print("Зашифрованный пароль или ключ не найдены. Создайте пароль сначала")
    create_and_store_password()
    return 

  key = load_key()
  with open(PASSWORD_FILE, 'r') as file:
    password_data = json.load(file)
    encrypted_password = password_data['password'].encode()
    created_password = decrypt_data(encrypted_password, key)

  # Аутентификация пользователя
  while True:
    print("Хотите ли вы видеть вводимый пароль? (да/нет)")
    show_password = input().lower() == 'да'
    entered_password = get_password('Введите ваш пароль для доступа: ',show_password)

    if entered_password == created_password:
      break
    print('Неверный пароль. Попробуйте еще раз.')

  # Генерируем ключ
  key = generate_key()
  secret_word = 'key'

  while True:
    choice = input(
        "Введите '1' для шифрования, '2' для расшифрования, '0' для выхода: ")
    if choice == '1':
      data_to_encrypt = input('Введите данные для шифрования: ')
      encrypted_data = encrypt_data(data_to_encrypt, key)
      print(f'Зашифрованные данные: {encrypted_data}')
    elif choice == '2':
      data_to_decrypt = input('Введите данные для расшифрования: ')
      try:
        decrypted_data = decrypt_data(data_to_decrypt, key)
        print(f'Расшифрованные данные: {decrypted_data}')
      except Exception as e:
        print(f'Ошибка расшифровки: {e}')
    elif choice == '0':
      print(" Спасибо! До свидания!")
      break
    elif choice == secret_word:
      print(f'Your key is: \n{key}')
    else:
      print(" Неверный ввод. Введите '1', '2' или '0'. ")


# Запуск пользовательского интерфейса
if __name__ == "__main__":
  user_interface()

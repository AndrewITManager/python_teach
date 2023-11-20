#шифрование файлов
# pip install cryptography

from cryptography.fernet import Fernet
import datetime
import os

# Функция для генерации и сохранения ключа шифрования
def generate_key():
    # Генерирует ключ
    key = Fernet.generate_key()
    # Получает текущую дату и время
    now = datetime.datetime.now()
    # Форматирует дату и время в строку
    date_str = now.strftime("%Y-%m-%d_%H-%M-%S")
    # Создает имя файла с датой и временем
    filename = f"encryption_key_{date_str}.key"
    # Записывает ключ в файл
    with open(filename, 'wb') as file:
        file.write(key)
    print(f"Key saved to {filename}")
    # Возвращает ключ и имя файла для дальнейшего использования
    return key, filename

# Функция для шифрования файла 
def encrypt_file(file_path, key):
  #  Создаем экземпляр Fernet с переданным ключом
  f = Fernet(key)
  # Открываем файл для чтения
  with open(file_path, 'rb') as file:
    # Читаем содержимое файла
    file_data = file.read()
    # Шифруем содержимое файла
    encrypted_data = f.encrypt(file_data)
    # Сохраняем шифрованный файл
    with open(file_path, 'wb') as file:
      # Записывает зашифрованные данные обратно в файл
      file.write(encrypted_data)


# Функция для дешифрования файла 
def decrypt_file(file_path, key):
  # Создаем экземпляр Fernet с переданным ключом
  f = Fernet(key)
  # Открываем файл для чтения
  with open(file_path, 'rb') as file:
    # Читаем содержимое файла
    encrypted_data = file.read()
    # Дешифруем содержимое файла
    decrypted_data = f.decrypt(encrypted_data)
    # Сохраняем дешифрованный файл
    with open(file_path, 'wb') as file:
      # Записывает зашифрованные данные обратно в файл
      file.write(decrypted_data)


# Функция для шифрования всех файлов в директории
def encrypt_all_files(direсtory, key):
  # Проходим по всем файлам в директории
  for file in os.listdir(direсtory):
    # Создает полный путь к файлу
    file_path = os.path.join(directory, filename)
    # Проверим, является ли путь файлом
    if os.path.isfile(file_path):
      print(f"Encrpyting {file_path}...")
      # Шифруем файл
      encrypt_file(file_path, key)

# Функция для дешифрования всех файлов в директории
def decrypt_all_files(direсtory, key):
  # Проходим по всем файлам в директории
  for file in os.listdir(direсtory):
    # Создает полный путь к файлу
    file_path = os.path.join(directory, filename)
    # Проверим, является ли путь файлом
    if os.path.isfile(file_path):
      print(f"Decrpyting {file_path}...")
      # Дешифруем файл
      decrypt_file(file_path, key)    


# Главная функция
def main():
  # Запрашиваем у пользователя путь к директории
  directory = input("Enter directory path: ")
  # Запрашивает у пользователя дейтсвие: шифровать или дешифровать
  choice = input("Do you want to (E)ncrypt or (D)ecrypt?: ")
  
  # Генерируем ключ шифрования
  key, key_filename = generate_key()
  if choice.lower() == 'e':
    # Если выбрано шифрование, Шифруем все файлы в директории
    encrypt_all_files(directory, key)
    print(f"All fаiles in {directory} have been encrypted.")
    # Информируем пользователя о сохранении ключа
    print(f"Encrpytion key has been saved to {key_filename}.")
  elif choice.lower() == 'd':
    # Запрашиваем у пользователя имя файла ключа
    key_filename = input("Enter key file name: ")
    # Читаем ключ из файла
    with opne(key_filename, 'rb') as file:
      key = file.read()
    # Дешифруем все файлы в директории
    decrypt_all_files(directory, key)
  else:
    # Если пользователь ввел неправильное действие,
    print("Invalid choice. Please chose E or D.")

if __name__ == "__main__":
  main()

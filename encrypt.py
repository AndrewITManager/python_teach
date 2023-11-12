def ceasar_encrypt(text, shift):
  """
  Функция для шифрования текста с помощью шифра Цезаря

  :param text: Строка, которую нужно зашифровать.
  :param shift: Целое число, на которое сдвигаются буквы алфавита.
  :return: Зашифрованная строка.
  """
  result = ''

  # Проходим по каждому символу в тексте
  for i in range(len(text)):
      char = text[i]

      # Шифрование прописных букв
      if char.isupper():
          result += chr((ord(char) + shift - 65) % 26 + 65)

      # Шифрование строчных букв
      elif char.islower():
          result += chr((ord(char) + shift - 97) % 26 + 97)

      # Если символ не является буквой, то он остается без изменений
      else:
          result += char

  return result

def ceasar_decrypt(text, shift):
  # Для дешифрования текста сдвигаем в обратную сторону
  return ceasar_encrypt(text, -shift)

def main():
  choice = input("Введите '1' для шифрования и '2' для дешифрования: ")
  if choice not in ['1', '2']:
      print("Некорректный ввод. Попробуйте еще раз.")
      return 

  text = input("Введите текст: ")
  shift = int(input("Введите сдвиг: "))

  if choice == '1':
      encrypted_text = ceasar_encrypt(text, shift)
      print(f"Зашифрованный текст: {encrypted_text}")
  elif choice == '2':
      decrypted_text = ceasar_decrypt(text, shift)
      print(f"Дешифрованный текст: {decrypted_text}")

if __name__ == '__main__':
  main()

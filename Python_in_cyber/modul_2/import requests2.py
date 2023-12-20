import requests
from bs4 import BeautifulSoup

#Определение функции для получения цены книги 
def get_book_price(url):
  try:
    # Отправка HTTP-запроса на указанный URL
    response = requests.get(url)
    # Проверка на наличие ошибок HTTP (например, 404 или 500)
    response.raise_for_status()

    # Парсинг HTML-контента ответа
    soup = BeautifulSoup(response.content, 'html.parser')

    # Поиск элемента с ценой в HTML 
    price_meta = soup.find('meta', itemprop='price')

    # Проверка, найден ли элемент  есть ли у него атрибут 'content'
    if price_meta and 'content' in price_meta.attrs:
      # Извлечение значения цены из атрибута 'content'
      price = price_meta.attrs['content']
      # Возвращение найденной цены
      return price
    else:
      # В случае, если элемент цена не найдена
      return "Цена не найдена"
  except requests.RequetsException as e:
    # В случае, если возникла ошибка при отправке HTTP-запроса
    return "Ошибка при получении цены: " + str(e)

# URL страницы продукта
url = "http://www.bookvoed.ru/book?id=13627000"

# Вызов функции для получения цены и сохранение результата в переменную
price = get_book_price(url)

# Вывод цены книги или сообщения об ошибки 
print(f"Цена книги: {price}")
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
  except Exception as e:
    # В случае, если возникла ошибка при отправке HTTP-запроса
    return "Ошибка при получении цены: " + str(e)

# URL страницы продукта
url = "http://www.bookvoed.ru/book?id=13627000"

# Вызов функции для получения цены и сохранение результата в переменную
price = get_book_price(url)

# Вывод цены книги или сообщения об ошибки 
print(f"Цена книги: {price}")



# Импортируем необходимые библиотеки
from selenium import webdriver # Импорт основной библиотеки Selenium для работы с веб-браузерами
from selenium.webdriver.chrome.service import Service # Импорт для настройки сервиса ChromeDriver
from webdriver_manager.chrome import ChromeDriverManager # Импорт библиотеки для установки ChromeDriver
from selenium.webdriver.chrome.options import Options # Импорт для натсройки опций браузера Chrome


# Функция для получения заголовка веб-страницы
def get_website_title_with_selenium(url):
  # Настройка опций для браузера
  chrome_options = Options
  chrome_options.add_argument("--headless") # Добавление опции для запуска Chrome в фоновом режиме (без графического интерфейса пользователя )
 # Инициализация драйвера Chromе с автоматической установкой через ChromeDriveManager
  driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options) 
  # Открытие указанной веб страницы в браузере 
  driver.get(url)

  # Получение заголовка веб-страницы
  title = driver.title
  # Закрытие браузера после завершения работы
  driver.quit()
  # Возвращение значения заголовка веб-страницы
  return title


# URL сайта, с которого нужно получить заголовок
url = "https://kod.mob-edu.ru/"

# Вызов функции и получение заголовка сайта
title = get_website_title_with_selenium(url)

# Вывод заголовка в консоль в формате HTML-тега <title>
print(f"<title>{title}</title>")
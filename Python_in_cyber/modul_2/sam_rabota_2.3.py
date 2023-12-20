#импорт библиотек
import requests
from bs4 import BeautifulSoup

#запрос страницы
req = requests.get('https://www.bookvoed.ru/book?id=625433')
#преобразование полученных данных
soup = BeautifulSoup(req.content, 'html.parser')
#поиск нужного класса
price = soup.find('div', {'class': 'PG'}).get_text()
#печать текста из найденного блока
print(price)
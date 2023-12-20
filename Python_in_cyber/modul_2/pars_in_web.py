import requests
from bs4 import BeautifulSoup

# Отпарвляем GET запрос на страницу Википедии
url = "https://en.wikipedia.org/wiki/Python_(programming_language)"

def get_related_links(soup):
  """
  Извлекает и возвращает список связанных ссылок на статьи из Википедии
  """
  related_links = []
  # Находитм все ссылки на статьи (теги <a>) внутри контента статьи
  content_dic = soup.find("div", {"id": "content"})
  for link in content_dic.find_all("a", href=True):
    related_links.append(link["href"])

  return related_links

try:
  response = requests.get(url)
  # Проверяем успешность запроса
  response.raise_for_status()

  # Если запрос успешен, получаем содержимое страницы
  page_content = response.text

  # Используем BeautifulSoup для парсинга HTML
  soup = BeautifulSoup(page_content, "html.parser")

  # Находим заголовок страницы
  title = soup.title.string
  print(f"Заголовок страницы: {title}")

  # Находим и выводим первый абзац текста
  first_paragraph = soup.find("p")
  print(f"Первый абзац текста: \n{first_paragraph}\n")

  # Находим и выводим все заголовки h2
  h2_headings = soup.find_all("h2")
  print(" Заголовки h2:")
  for heading in h2_headings:
    print(heading.text)

  # Извлекаем и выводим связанные сслыки 
  related_links = get_related_links(soup)
  print("\nСвязанные ссылки:")
  for link in related_links:
    print(link)
    
except requests.exceptions.RequestException as e:
  print(f"Ошибка запроса: {e}")
except Exception as e:
  print(f"Ошибка парсинга: {e}")
  
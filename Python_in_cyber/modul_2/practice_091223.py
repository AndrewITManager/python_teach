import requests
from bs4 import BeautifulSoup


def get_random_wikipedia_article(language='en', save_to_file=False, extract_image=False):
    #URL для получения случайной статьи
    url = "https://ru.wikipedia.org/wiki/Special:Random"
    #получаем HTML-код случайной статьи
    response = requests.get(url)
    html = response.content


    #Создаем объект BeautifulSoup для парсинга HTML
    soup = BeautifulSoup(html, "html.parser")

    #Извлекаем заголовок статьи
    title = soup.find("h1").text.strip()

    #Извлекаем описание статьи
    description = soup.find('p').text.strip()

    #формируем ссылку на статьи
    full_article_link = response.url

    article = {
        "title" : title,
        "description" : description,
        "link" : full_article_link
    }


    if extract_image:
        #извлекаем ссылку на изображение
        image = soup.find('img')['src']
        if image:
            article['image'] = 'https:' + image
        else:
            article['image'] = 'No image found'

    if save_to_file:
        save_article(article)
    return article

def save_article(article):
    with open('saved_articles.txt', 'a', encoding='utf-8') as file:
        file.write(f"Title: {article['title']}\n")
        file.write(f"Description: {article['description']}\n")
        file.write(f"Link: {article['link']}\n")
        if 'image' in article:
            file.write(f"Image: {article['image']}\n")
        file.write("\n-------------------------------------------------------------\n")


random_article = get_random_wikipedia_article(language='ru', save_to_file=True, extract_image=True)
print(f"Title: {random_article['title']}")
print(f"Description: {random_article['description']}")
print(f"Link: {random_article['link']}")
if 'image' in random_article:
    print(f"Image: {random_article['image']}")
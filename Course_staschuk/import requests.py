import requests
from bs4 import BeautifulSoup


link = "https://browser-info.ru/"
responce = requests.get(link).text
soup = BeautifulSoup(responce, 'lxml')
block = soup.find('div', id = "tool_padding")
chek_js = block.find('div', id = 'javascript_chek')





with open("1.html", "w", encoding="utf-8") as file:
    file.write(responce)

print(responce)
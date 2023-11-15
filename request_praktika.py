# 1. Отправка простого текстового сообщения(файл 1)
# pip install requests
import requests

# URL интернет-сервиса, к которому вы хотите обратиться 
url = 'https://example.com/api'

# Текстовое сообщение, которое хотите отправить
data = " Ваше сообщение"

# Отправка POST запрос на сервер
response = requests.post(url, data=data)

# Выводим текст ответа от сервера
print(response.text)



# 2. Отправка сообщения в формате JSON(файл 2)
import requests
import json

# URL интернет-сервиса, к которому вы хотите обратиться 
url = 'https://example.com/api'

# Заголовки, необходимые для отправки данных в формате JSON
headers = {'Content-Type': 'application/json'}

# Данные, которые вы хотите отправить, в формате словаря Python
data = {
  "key": "value",
  "key2": "value2"
}

# Отправка POST запрос с данными в формате JSON 
response = requests.post(url, headers=headers, data=json.dumps(data))

# Преобразуем ответ сервера из формата JSON обратно в словарь Python
print(response.json())
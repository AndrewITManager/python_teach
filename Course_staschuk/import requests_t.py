import requests
import json
# URL интернет-сервиса 
url = 'https://httpbin.org/'
# запрос к ресурсу
print(requests.get(url))
# Текстовое сообщение, которое хотите отправить
data = "Text data"
# Отправка POST запрос на сервер
response = requests.post(url + 'post', data=data)
# Вывод ответа
print(response.text)

# Заголовки, необходимые для отправки данных в формате JSON
headers = {'Content-Type': 'application/json'}
# Данные, которые вы хотите отправить, в формате словаря Python
data_1 = {
  "key": "value",
  "key2": "value2"
}
# Отправка POST запрос с данными в формате JSON 
response_2 = requests.post(url + 'post', headers=headers, data=json.dumps(data_1))
# Преобразуем ответ сервера из формата JSON обратно в словарь Python
print(response_2.json())
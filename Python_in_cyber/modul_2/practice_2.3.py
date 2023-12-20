import requests


url = 'https://open-college.ru/'
response = requests.get(url)
response.raise_for_status()
print(response.text)
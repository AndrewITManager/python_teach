#request in dadata.ru 
from dadata import Dadata #импортируем библиотеку

token = '25b303d7a9a7f9367146c3fdc84c1aecded0da8a' # API ключ
secret = '46b69b5627460d06457e8352b015882cb1a02802' # секретный ключ
dadata = Dadata(token, secret) # сообщаем свои token и секретный ключ для обращения
result = dadata.iplocate("188.244.134.209")
print(result)#вывод результата
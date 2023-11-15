#request in dadata.ru 
from dadata import Dadata #импортируем библиотеку

token = '70f89aaae2279526d6c10fc68e2b374c2ae51435' # API ключ
secret = '2d7defa7b8daed5e95578b96efece6b974b9ab85' # секретный ключ
dadata = Dadata(token, secret) # сообщаем свои token и секретный ключ для обращения
result = dadata.clean("address", "Сегежа Антикайнена 18")
print(result)#вывод результата
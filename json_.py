#json - формат обмена данными и формат файлов, javascript object notation
import json #импорт модуля 

json_str = '{"id":235, "brand":"Nike", "qty":84, "status":{"isForSale:true}"}'

sneakers = json.loads(json_str)#метод loads, парсинг объекта json


print(type(sneakers))

print(sneakers['brand'])
print(sneakers['qty'])
print(sneakers['status']['isForSale'])

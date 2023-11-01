#конвертация json в словарь
import json #импорт модуля 
#print(dir(json))
# json.loads
json_str = '{"id":235, "brand":"Nike", "qty":84, "status":{"isForSale":true}}'
json_array = '[{"a":1}, {"b":2}]'
sneakers = json.loads(json_str)#метод loads, парсинг объекта json
print(type(sneakers))
print(sneakers['brand'])
print(sneakers['qty'])
print(sneakers['status']['isForSale'])
print(sneakers)
print('')
my_list = json.loads(json_array)
print(my_list)

json_from_disct = json.dumps(sneakers, indent=2)#конвертация обратно в json с форматированием
print(json_from_disct)
print(type(json_from_disct))

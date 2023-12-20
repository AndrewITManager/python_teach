import requests
import json

response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
data = response.json()

print("JSON response:")
print(json.dumps(data, indent=4))

########################################################################

import xml.etree.ElementTree as ET

xml_data = '''
<user>
    <id>1</id>
    <name>John</name>
    <age>38</age>
</user>
'''


#Функция для разбора XML и возврата данных в виде словаря
def parse_xml(xml_data):
    root = ET.fromstring(xml_data)
    user_data = {}
    user_data['id'] = root.find('id').text
    user_data['name'] = root.find('name').text
    user_data['age'] = root.find('age').text
    return user_data

#разбор XML
user_info = parse_xml(xml_data)


#Output data
print("\nUser info:")
print(f"User ID: {user_info['id']}")
print(f"User Name: {user_info['name']}")
print(f"User Age: {user_info['age']}")

# print(f"User Name: {root.find('name').text}")
# print(f"User Age: {root.find('age').text}")



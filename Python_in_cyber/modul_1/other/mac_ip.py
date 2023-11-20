import os
import platform 


def get_mac_address(ip_address):
  # Проверяем на какой операционной ситеме мы находимся
  if platform.system() == "Windoows":
    # Для Windows используем команду "arp -a" для получения таблицы ARP 
    result = os.popen(f"arp -a {ip_address}").read()
    # Извлекаем MAC-alhtc из вывода команды
    mac_address = result.split("\n")[3].split()[1]
  elif platform.system() == 'Linux':
    # Для Linux используем команду "arp" для получения таблицы ARP
    result = os.popen(f"arp -a {ip_address}").read()
    # Извлекаем MAC-alhtc из вывода команды
    mac_address = result.split()[7]
  else:
    return " Неподдерживаемая операционная системa"

  return mac_address

# Задаем IP-адрес, для которого хотим получить MAC-адрес
ip_address = "192.168.1.1"
# Получаем MAC-адрес для указанного IP- адреса
mac_address = get_mac_address(ip_address)

if mac_address:
  print(f"MAC-адрес для IP-адреса {ip_address}: {mac_address}")
else:
  print("Не удалось получить MAC-адрес")
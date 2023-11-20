""" 
  Импорты: Мы используем библиотеку scapy для захвата и анализа сетевых пакетов, а также           defaultdict из модуля collections для удобного хранения данных о попытках подключения.
""" 
from scapy.all import sniff, IP, TCP
from collections import defaultdict
import time

"""
  Хранение данных: connections — это словарь, где ключом является IP-адрес, а значением —  информация о подключениях к разным портам и время последнего подключения.
""" 
connections = defaultdict(lambda: {"ports": set(), "last_seen": 0})


"""
Функция detect_port_scan: Эта функция вызывается для каждого захваченного пакета. Она проверяет, содержит ли пакет IP и TCP данные, затем обновляет информацию о подключениях и проверяет на наличие подозрительной активности
"""
def detect_port_scan(packet):
  # Проверяем, содержит ли пакет IP и TCP слои данных
  if IP in packet and TCP in packet:
    # Извлекаем IP-адрес отправителя и порт назначения
    src_ip = packet[IP].src
    dst_port = packet[TCP].dport

  # Обновляем информацию о подключениях для этого IP-адреса
  data = connections[src_ip]
  data["ports"].add(dst_port)
  data["last_seen"] = time.time()

  # Проверяем не является ли активность подозрительной
  # В данном случае, более 5 попыток подключения к разным портам  в течение минуты
  if len(data["ports"]) > 5 and (time.time() - data["last_seen"]) < 60:
    # Выводим предупреждение о возможном сканировании портов 
    print(f"Port scanning detected from {src_ip} on ports on {data['ports']}")


# Начинаем захват пакетов с использованием функции shiff из Scapy 
# Фильтруем только TCP пакеты , не сохраняя их в памяти (store=0)
# Функция detect_port_scan будет вызвана для каждого захваченного пакета
sniff(filter="tcp", prn=detect_port_scan, store=0)
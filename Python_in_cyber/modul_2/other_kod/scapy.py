# pip install scapy

# Sendinf ICMP Echo Requests (ping) к заданному IP aдресу
# Захватываем и выводим ответ (Echo Reply)

from scapy.all import *

def ping_host(target_ip):
  # Создаем пакет ICMP Echo Request пакет 
  icmp_request = IP(dst=target_ip)/ICMP()
  # Отправляем пакет ICMP Echo Request пакет 
  response = sr1(icmp_request, timeout=1, verbose=0)

  # Проверяем, есть ли ответ от сервера
  if response is not None:
    # Если ответ есть, то выводим его
    print(f"Received reply from {target_ip}: {response[IP].src}")
  else:
    # Если ответ нет, то выводим сообщение
    print(f"No reply received from {target_ip}")


if __name__ == "__main__":
  target_ip = "8.8.8.8"
  ping_host(target_ip)
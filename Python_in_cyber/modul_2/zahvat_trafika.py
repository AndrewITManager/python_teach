from scapy.all import *
import logging

# № Настройка логирования
logging.basicConfig(filename='traffic_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

def capture_and_count_traffic(interface, limit_mb):
  try:
     print(f"Захват трафика на интерфейсе {interface}...")

    total_bytes = [0] # Используем список дял изменяемой переменной в замыкании

    # Функция для проверки условияя установки
    def stop_capture(packet):
      total_bytes[0] += len(packet)
      return total_bytes[0] >= limit_mb * 1024 * 1024 # 1 MB
      
    # захватим пакеты сетевого интерфейса c условием остановки
     packets = sniff(iface=interface, stop_filter=stop_capture)
     
     # Кол-во захваченных пакетов 
     packet_count = len(packets)
     # Подсчитаем общий объем трафика в мегабайтах 
     total_megabytes = total_bytes[0] / (1024 * 1024)
     # Выведим информацию о кол-во захваченных пакетов
     message = f"Захвачено {packet_count} пакетов трафика на интерфейсе {interface}.\nОбщий объем трафика: {total_megabytes:.2f} MB"
     logging.info(message)

  except Exception as e:
     print("Остановка захвата трафика...")
     print(f"Failed: {e}")
     logging.error(f"Произошла ошибка: {e}")

if __name__ == "__main__":
   print("Программа для захвата и подсчета сетевого трафика...")
   print(f"Запуск программы...")
   # Пользователь вводит имя сетевого интерфейса
   network_interface = input("Введите имя сетевого интерфейса (например, eth0): ")
   limit_mb = float(input("Введите желаемый объем трафика для захвата в мегабайтах (например, 1 или 2): "))   
   # Запускаем функцию захвата трафика
   capture_and_count_traffic(network_interface, limit_mb)

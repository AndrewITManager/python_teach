from scapy.all import sniff, ARP 

def detect_all_spoofing(packet):
    # Проверяет, является ли пакет ARP-ответом
  if packet[ARP].op == 2: # 2 означет ARP-ответ 
    try:
      real_mac = getmacbyip(packet[ARP].psrc)
      response_mac = packet[ARP].hwsrc
      # Проверяем, соответсвует ли MAC-адрес в ARP-ответе реальному MAC-адресу  
      if real_mac != spoofed_mac:
        print(f"[!] ARP Spoofing Detected: {packet[ARP].psrc} has MAC {respone_mac}, but should have MAC {real_mac}}")
    except IndexError as i:
      print(f"Не удалось получить MAC aдрес {i}") 

print("Starting ARP Spoofing Detecor...")
sniff(store=False, prn=detect_all_spoofing, filter="app")


######################################################################################################
# скрипт 2
######################################################################################################

from scapy.all import ARP, sniff
from collections import defaultdict

# Словарь для хранения пар IP-MAC
ip_mac_mapping = defaultdict(set)

def process_packet(packet):
    # Проверяем, является ли пакет ARP-запросом или ARP-ответом
    if packet.haslayer(ARP):
        # Получаем IP и MAC адреса
        source_ip = packet[ARP].psrc
        source_mac = packet[ARP].hwsrc

        # Проверяем наличие несоответствия IP и MAC
        if source_mac not in ip_mac_mapping[source_ip]:
            ip_mac_mapping[source_ip].add(source_mac)
            print(f"[!] Обнаружено потенциальное ARP-спуфинг: IP {source_ip} связан с MAC {source_mac}")

def main():
    print("Начинаем обнаружение ARP-спуфинга...")
    sniff(store=False, prn=process_packet, filter="arp")

if __name__ == "__main__":
    main()

apt-get install dsniff
arpspoof -i lo -t [целевой IP] [шлюз IP]
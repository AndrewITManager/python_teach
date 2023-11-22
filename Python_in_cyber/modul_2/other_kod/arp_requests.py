# 2 ARP requests

# pip install scapy

from scapy.all import ARP, Ether, srp

def scan_network(network):
  # Создаем ARP запрос
  arp_request = ARP(post=network)
  # Создаем Ethernet frame
  ether_frame = Ether(dst="ff:ff:ff:ff:ff:ff")
  # Стекуем Ethernet-фрейм и ARP-запрос
  packet = ether_frame / arp_request
  # Отправляем пакет
  result = srp(packet, timeout=1, verbose=0)[0]

  devices = []
  for sent, received in result:
      devices.append({'ip': received.psrc, 'mac': received.hwsrc})

  return devices


if __name__ == "__main__":
  network = "192.168.0.0/24"
  devices = scan_network(network)
  print("Found devices")
  for device in devices:
    print(f"IP: {device['ip']} MAC: {device['mac']}")
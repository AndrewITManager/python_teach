# Server.py

import socket
import threading
from dadata import Dadata

# Вставьте ваш API-ключ Dadata здесь
DADATA_API_KEY = '25b303d7a9a7f9367146c3fdc84c1aecded0da8a'
DADATA_API_SECRET = '46b69b5627460d06457e8352b015882cb1a02802'

# Создание экземпляра клиента Dadata
dadata = Dadata(DADATA_API_KEY, DADATA_API_SECRET)

# Функция для получения геолокации по IP-адресу через API Dadata
def get_location_by_ip(ip_address):
    try:
        # Выполнение запроса к API Dadata
        location = dadata.iplocate(ip_address)
        if location and 'location' in location:  
            # Возвращаем данные о местоположении, если они доступны
            return location
        return None
    except Exception as e:
        print(f"Ошибка при запросе к Dadata: {e}")
        return None



# Функция для обработки подключения клиента
def handle_client(client_socket, username):
    try:
        while True:
            message = client_socket.recv(1024).decode('utf-8')
            if message.lower() == 'quit':
                break
            elif message.startswith('Вычисли его по ip'):
                ip_address = message.split()[-1]
                client_socket.sendall("IP-бот: Вычисляю…".encode('utf-8'))
                location_info = get_location_by_ip(ip_address)
                if location_info:
                    country = location_info.get("data", {}).get("country", "Неизвестно")
                    region = location_info.get("data", {}).get("region_with_type", "Неизвестно")
                    city = location_info.get("data", {}).get("city", "Неизвестно")
                    response = f"IP-бот: Страна: {country}, Регион: {region}, Город: {city}"
                else:
                    response = f"IP-бот: Не удалось определить местоположение по {ip_address}"
                client_socket.sendall(response.encode('utf-8'))
            else:
                broadcast(f"{username}: {message}")
    except ConnectionResetError:
        print(f"{username} удален")
    except Exception as e:
        print(f"Ошибка при обработке сообщения: {e}")
    finally:
        client_socket.close()

# Список для хранения подключенных клиентов
clients = []

# Функция для рассылки сообщений всем подключеннным клиентам
def broadcast(message):
    for client in clients:
        client.sendall(message.encode('utf-8'))

# Функция для принятия входящих подключений 
def accept_connections(server_socket):
    while True:
        # Принятия подключения от клиента
        client_socket, _ = server_socket.accept()
        # Добавление клиента в список
        clients.append(client_socket)
        # Получение имени пользователя
        username = client_socket.recv(1024).decode('utf-8').split(" присоединился к чату.")[0]
        # Запуск потока для обработки сообщений от клиента
        threading.Thread(target=handle_client, args=(client_socket, username)).start()

if __name__ == '__main__':
    try:
        # Создание сокета сервера
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            # Привязка сокета к порту
            server_socket.bind(('127.0.0.1', 12345))
            # Начало прослушивания входящих подключений
            server_socket.listen()
            print("Сервер чата запущен и ожидает подключений...")
            # Запуск функции для принятия подключений
            accept_connections(server_socket)
    finally:
        # Закрытие сессии клиента Dadata при завершении работы
        dadata.close()
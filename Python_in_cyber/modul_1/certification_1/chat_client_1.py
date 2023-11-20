# client.py

import socket
import threading

# Функция для отправки сообщений серверу
def send_messages(client_socket, name):
    try:
        while True:
            message = input()
            client_socket.sendall(message.encode('utf-8'))
            if message.lower() == 'quit':
                break
    except Exception as e:
        print(f"Ошибка при отправке сообщения: {e}")

# Функция для получения сообщений от сервера
def receive_messages(client_socket):
    try:
        while True:
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
    except ConnectionResetError:
        print("Соединение с сервером потеряно")
    except Exception as e:
        print(f"Ошибка при получении сообщения: {e}")

if __name__ == '__main__':
    name = input("Введите ваше имя: ")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect(('127.0.0.1', 12345))
        client_socket.sendall(f"{name} присоединился к чату.".encode('utf-8'))
        threading.Thread(target=receive_messages, args=(client_socket,)).start()
        send_messages(client_socket, name)

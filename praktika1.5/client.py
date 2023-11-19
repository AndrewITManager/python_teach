import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#параметры клиента и для сервера

client.connect(('127.0.0.1', 9897))#подключение к локальному адресу на том же порте
flag = True


while flag:#цикл
    client.send(input('Client_1:').encode('utf-8'))#отправка сообщений от клиента
    message = client.recv(1024).decode('utf-8')#клиент получает сообщение и декодирует его
    if message == 'quit':#возможность выхода по quit
        flag = False
    else:
        print(message)

client.close()
server.close()


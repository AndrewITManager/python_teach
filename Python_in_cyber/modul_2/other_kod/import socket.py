import socket
import threading

def client_handler(client_socket, clien_address):
  while True:
    try:
      message = client_socket.recv(1024).decode("utf-8")
      if message:
        print(f"Received message from {clients_address}: {meesage}")
        broadcast(message, client_socket)
      else:
        remove(client_socket)
        break
    except:
      continue


def broadcast(message, connection):
  for client in clients:
    try:
      client.send(message.encode("utf-8"))
    except:
      client.close()
      remove(client)


def remove(connection):
  if connection in clients:
    clients.remove(connection)

# Server setup
host = '127.0.0.1'
port = 12345
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen()

clients = []

print("Server is listening")


while True:
  client_socket, client_address = server_socket.accept()
  clients.append(client_socket)
  print(f"Connection from {client_address} has been established.")
  threading.Thread(target=clien_handler, args=(client_socket, client_address)).start()


# client.py

def receive_message(client_socket):
  while True:
    try:
      message = client_socket.recv(1024).decode("utf-8")
      if message:
        print(message)
    except:
      print("AN error occured!")
      client_socket.close()
      break


# Client setup
host = "127.0.0.1"
port =12345
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

threading.Thread(target=receive_message, args=(client_socket,)).start()

while True:
  message = input("")
  if message:
    client_socket.send(message.encode("utf-8"))


# UDP

import socket
import datetime

def get_current_time():
  return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# Server setup 

host = "127.0.0.1"
port = 12345
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((host, port))

print("UDP Time Server is running...")


while True:
  data, addr = server_socket.recvfrom(1024)
  print(f"Received requset from {addr}")
  current_time = get_current_time()
  server_socket.sendto(current_time.encode("utf-8"), addr)


# Client setup

host = "127.0.0.1"
port = 12345
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
  message = "Requesting current time"
  clien_socket.sendto(message.encode("utf-8"), (host, port))
  data, _ = client_socket.recvfrom(1024)
  print(f"Current time is {data.decode('utf-8')}")
finally:
  client_socket.close()
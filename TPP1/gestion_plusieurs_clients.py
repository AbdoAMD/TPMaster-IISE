import socket

import threading

def handle_client(client_socket):

 while True:

  data = client_socket.recv(1024).decode('utf-8')

  if not data:

   break

  print(f"Message reçu: {data}")

  client_socket.send(data.encode('utf-8'))

 client_socket.close()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('localhost', 12345))

server_socket.listen(5)

print("Serveur en attente de connexions...")

while True:

  client_socket, client_address = server_socket.accept()

  print(f"Connexion établie avec {client_address}")

  client_thread = threading. Thread (target=handle_client, args=(client_socket,))

  client_thread.start()
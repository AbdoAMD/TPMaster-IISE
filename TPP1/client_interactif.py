import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

while True:
    message = input("Entrez un message (ou 'quit' pour quitter) : ")
    if message.lower() == 'quit':
        break
    client_socket.send(message.encode('utf-8'))
    response = client_socket.recv(1024).decode('utf-8')
    print(f"Réponse du serveur : {response}")

client_socket.close()
# TCP socket, client, example 2
# this client connects to the server given with the IP and Port# below and sends a message to server
from socket import *
serverName = "161.9.39.193"
serverPort = 12000

client_socket = socket(AF_INET, SOCK_STREAM)

client_socket.connect((serverName, serverPort))

while True:
    message = input('Type message:')

    client_socket.send(message.encode())
    if message == "exit":
        client_socket.close()
        exit(0)
    else:
        print("message is sent")

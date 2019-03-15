# TCP socket, threaded server, example 2
# this server receives a message from client and print it on screen, then wait for another connection requests as well
# as listen for connected clients

from socket import *
import threading


class ThreadedServer:
    @staticmethod
    def listen_to_client(client, addr):
            while True:
                    message = client.recv(1024)
                    if message == "exit":
                        print(addr, " is closed")
                        client.close()
                        exit(0)
                    else:
                        print(addr, " says: ", message.decode("utf-8"))

    def __init__(self, server_port):
        try:
            server_socket = socket(AF_INET, SOCK_STREAM)
        except:
            print("Socket cannot be created!!!")
            exit(1)
        print("Socket is created...")
        try:
            server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        except:
            print("Socket cannot be used!!!")
            exit(1)
        print("Socket is being used...")
        try:
            server_socket.bind(('', server_port))
        except:
            print("Binding cannot de done!!!")
            exit(1)
        print("Binding is done...")
        try:
            server_socket.listen(45)
        except:
            print("Server cannot listen!!!")
            exit(1)
        print ("The server is ready to receive")
        while True:
            connection_socket, addr=server_socket.accept()
            threading.Thread(target=self.listen_to_client, args=(connection_socket, addr)).start()


if __name__ == "__main__":
    server_port = 12000
    ThreadedServer(server_port)

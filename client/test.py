from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

# GLOBAL CONSTANTS
HOST = "localhost"
PORT = 5500
ADDR = (HOST, PORT)
BUFSIZ = 512

# GLOBAL VARIABLE
messages = []

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)


def receive_messages():
    while True:
        msg = client_socket.recv(BUFSIZ).decode()
        messages.append(msg)
        print(msg)


def send_message(msg):
    


receive_thread = Thread(target=receive_messages)
receive_thread.start()

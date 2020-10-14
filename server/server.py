from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import time

#Global variable
HOST = 'localhost'
PORT =  55000
BUFSIZ = 512
ADDR = (HOST, PORT)
MAX_CONECTION = 5
SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

def broudcast()

def client_communicate(client):
    """
    Tread to handle all masages from client
    :param client: socket
    :return: None
    """
    run = True
    while run:
        msg = client.recv(BUFSIZ)
        if msg == bytes("{quit}", "utf8"):
            client.close()
        else:




def wait_for_connect():
    """
    wait for connect from new client and start new thread
    :param SERVER: socket
    :return: none
    """
    run = True
    while run:
        try:
            client, addr =SERVER.accept()
            print(f"[CONNECTION] {addr} connected to the server at {time.time()}")
            Thread(target=client_communicate, args=(client,)).start()
        except Exception as e:
            print("[FAILED]",e)
            run = False
    print("SERVER CRASHED")

if __name__ == '__main__':
    SERVER.listen(MAX_CONECTION) #listen for max conections
    print("[STARTED] Waiting for conection...")
    ACCEPT_THEARD =Thread(target=wait_for_connect)
    ACCEPT_THEARD.start()
    ACCEPT_THEARD.join()
    SERVER.close()




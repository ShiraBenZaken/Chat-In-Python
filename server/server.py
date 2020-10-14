
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

HOST = 'localhost'
PORT =  55000
BUFSIZ = 512
ADDR = (HOST, PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

def client_communicate(client):
    run = True
    while run:
        msg = client.recv(BUFSIZ)
        client.close()
        



def wait_for_conect(SERVER):
    run = True
    while run:
        try:
            client, addr =SERVER.accept()
            Thread(target=client_communicate, args=(client,)).start()
        except Exception as e:
            print("[FAILED]",e)
            run = False


if __name__ == '__main__':
    SERVER.listen(5)
    print("Waiting for conection...")
    ACCEPT_THEARD =Thread(target=wait_for_conect(SERVER))
    ACCEPT_THEARD.start()
    ACCEPT_THEARD.join()
    SERVER.close()




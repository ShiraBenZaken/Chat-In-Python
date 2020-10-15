from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import time
from person import Person

#Global constants
HOST = 'localhost'
PORT =  55000
BUFSIZ = 512
ADDR = (HOST, PORT)
MAX_CONECTION = 5
SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR) #set up the server

#Global VARIABLE
persons=[]


def broudcast(msg,name):
    """
    send new messages to all clients
    :param msg: bytes["utf8"]
    :param name: str
    :return:
    """
    for person in persons:
        client=person.client
        client.send(bytes(name+": ", "utf8")+ msg)


def client_communicate(person):
    """
    Tread to handle all masages from client
    :param client: Person
    :return: None
    """
    client=person.client
    addr=person.addr

    #get persons name
    name=client.recv(BUFSIZ).decode("utf8")
    msg= f"{name} has joined the chat"
    broudcast(msg)

    while True:
        msg = client.recv(BUFSIZ)
        if msg == bytes("{quit}", "utf8"):
            client.send(bytes("{quit}", "utf8"))
            client.close()
            persons.remove(person)
        else:
            client.send(msg, name)


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
            person= Person(addr, client)
            persons.append(person)
            print(f"[CONNECTION] {addr} connected to the server at {time.time()}")
            Thread(target=client_communicate, args=(person,)).start()
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




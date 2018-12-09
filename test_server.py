from socket import *
from config import *
from character import Character, JOBS
from threading import Thread

userlist = {}

def handle_client(client, client_addr):
    while True:
        try:
            msg = client.recv(BUFFER_SIZE)
            msg = msg.decode("utf8").split(";", 3)
            if (msg[1] == 'create'):
                a = Character(json_data=msg[2])
                userlist[msg[0]] = a
            elif (msg[1] == 'show'):
                for k, v in userlist.items():
                    print(k + " : " + v.name)
        except ConnectionResetError:
            continue

server = socket(AF_INET, SOCK_STREAM)
server.bind((HOST_IP, APP_PORT))
server.listen(MAX_CLIENTS)

while True:
    client, client_addr = server.accept()
    Thread(target=handle_client, args=(client, client_addr)).start()
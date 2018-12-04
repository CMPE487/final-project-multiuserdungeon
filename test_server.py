from socket import *
from config import *
from character import Character, JOBS
from threading import Thread

def handle_client(client, client_addr):
    while True:
        try:
            msg = client.recv(BUFFER_SIZE)
            a = Character(json_data=msg.decode("utf8"))
            print("{addr} says:".format(addr=client_addr))
            print("{name} is a {job}".format(name=a.name, job=a.jobname))
            print(a.stats_display())
        except ConnectionResetError:
            continue

server = socket(AF_INET, SOCK_STREAM)
server.bind((HOST_IP, APP_PORT))
server.listen(MAX_CLIENTS)

while True:
    client, client_addr = server.accept()
    Thread(target=handle_client, args=(client, client_addr)).start()

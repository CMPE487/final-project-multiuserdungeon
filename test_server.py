from socket import *
from config import *
from character import Character, JOBS
from threading import Thread
from map import Map

userlist = {}

def handle_client(client, client_addr):
    while True:
        try:
            msg = client.recv(BUFFER_SIZE)
            msg = msg.decode("utf8").split(";", 3)
            if (msg[1] == 'create'):
                a = Character(json_data=msg[2])
                userlist[msg[0]] = {"character": a, "client": client}
            elif (msg[1] == 'show'):
                for k, v in userlist.items():
                    userlist[msg[0]]["client"].send((f"{k} : {v['character'].name}").encode("utf8"))
            elif (msg[1] == 'move'):
                char = userlist[msg[0]]["character"]
                char.move(msg[2])
                print(char.position())
            elif (msg[1] == 'map'):
                char = userlist[msg[0]]['character']
                userlist[msg[0]]['client'].send(world.display_map(char.x, char.y).encode("utf8"))
            elif (msg[1] == 'look'):
                char = userlist[msg[0]]['character']
                userlist[msg[0]]['client'].send(world.ROOMS[char.x][char.y].description().encode("utf8"))
        except ConnectionResetError:
            continue

server = socket(AF_INET, SOCK_STREAM)
server.bind((HOST_IP, APP_PORT))
server.listen(MAX_CLIENTS)

world = Map("Lodea")
world.fill_map()

while True:
    client, client_addr = server.accept()
    Thread(target=handle_client, args=(client, client_addr)).start()

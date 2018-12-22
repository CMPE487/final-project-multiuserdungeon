from socket import *
from config import *
from character import Character, JOBS
from enemy import Enemy, Goblin
from threading import Thread
from map import Map

userlist = {}
def move(ip, char, to):
    world.ROOMS[char.x][char.y].users.remove(ip)
    char.move(to)
    world.ROOMS[char.x][char.y].users.append(ip)

def handle_client(client, client_addr):
    while True:
        try:
            msg = client.recv(BUFFER_SIZE)
            msg = msg.decode("utf8").split(";", 3)
            if (msg[1] == 'create'):
                a = Character(json_data=msg[2])
                userlist[msg[0]] = {"character": a, "client": client}
                world.ROOMS[a.x][a.y].users.append(msg[0])
            elif (msg[1] == 'show'):
                for k, v in userlist.items():
                    userlist[msg[0]]["client"].send((f"{k} : {v['character'].name}").encode("utf8"))
            elif (msg[1] == 'move'):
                char = userlist[msg[0]]["character"]
                move(msg[0], char, msg[2])
                print(char.position())
            elif (msg[1] == 'map'):
                char = userlist[msg[0]]['character']
                userlist[msg[0]]['client'].send(world.display_map(char.x, char.y).encode("utf8"))
            elif (msg[1] == 'look'):
                char = userlist[msg[0]]['character']
                s = world.ROOMS[char.x][char.y].description() + "\n"
                s += '\n'.join(list(map(lambda x: userlist[x]['character'].short_display() + ' is here', world.ROOMS[char.x][char.y].users)))
                userlist[msg[0]]['client'].send(s.encode("utf8"))
            elif (msg[1] == 'status'):
                char = userlist[msg[0]]['character']
                userlist[msg[0]]['client'].send(char.stats_display().encode("utf8"))
            elif (msg[1] == 'ambush'):
                char = userlist[msg[0]]['character']
                Goblin.attack(char)
                userlist[msg[0]]['client'].send(f"Gobin hp: {Goblin.hp}!".encode("utf8"))
        except ConnectionResetError:
            print(f"Connection reset with {client_addr}!")
            client.close()
            break

server = socket(AF_INET, SOCK_STREAM)
server.bind((HOST_IP, APP_PORT))
server.listen(MAX_CLIENTS)

world = Map("Lodea")
world.fill_map()

threads = {}

while True:
    client, client_addr = server.accept()
    t = Thread(target=handle_client, args=(client, client_addr))
    threads[client_addr] = t
    threads[client_addr].start()

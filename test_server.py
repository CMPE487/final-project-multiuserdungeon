from socket import *
from config import *
from character import Character, JOBS
from enemy import Enemy, goblin_stats
from threading import Thread
from map import Map

userlist = {}
def move(ip, char, to):
    world.ROOMS[char.x][char.y].users.remove(ip)
    char.move(to)
    world.ROOMS[char.x][char.y].users.append(ip)

def handle_client(client, client_, client_addr):
    while True:
        try:
            if client_addr[0] in userlist:
                if not userlist[client_addr[0]]['character'].is_alive():
                    print("Some one died")
                    client_.send("You are dead".encode("utf8"))

            msg = client.recv(BUFFER_SIZE)
            msg = msg.decode("utf8").split(";", 3)
            if (msg[1] == 'create'):
                a = Character(json_data=msg[2])
                userlist[msg[0]] = {"character": a, "client": client}
                world.ROOMS[a.x][a.y].users.append(msg[0])
            elif (msg[1] == 'show'):
                msg = ""
                for k, v in userlist.items():
                    msg += f"{k} : {v['character'].name}\n"
                client.send(msg.encode("utf8"))
            elif (msg[1] == 'drink'):
                char = userlist[msg[0]]["character"]
                if (world.ROOMS[char.x][char.y].type == "Water"):
                    char.hp = char.maxhp
                    client.send(f"The water refreshes you. You now have {char.hp} hit points.".encode("utf8"))
                else:
                    client.send("There is no well here".encode("utf8"))
            elif (msg[1] == 'move'):
                char = userlist[msg[0]]["character"]
                move(msg[0], char, msg[2])
                enemy = world.ROOMS[char.x][char.y].enemy
                if enemy:
                    Thread(target=enemy.combat_ai, args=([char], client_)).start()
                print(char.position())
            elif (msg[1] == 'map'):
                char = userlist[msg[0]]['character']
                userlist[msg[0]]['client'].send(world.display_map(char.x, char.y).encode("utf8"))
            elif (msg[1] == 'look'):
                char = userlist[msg[0]]['character']
                s = world.ROOMS[char.x][char.y].description() + "\n"
                userswithoutme = world.ROOMS[char.x][char.y].users.copy()
                userswithoutme.remove(msg[0])
                s += '\n'.join(list(map(lambda x: userlist[x]['character'].short_display() + ' is here', userswithoutme)))
                userlist[msg[0]]['client'].send(s.encode("utf8"))
            elif (msg[1] == 'status'):
                char = userlist[msg[0]]['character']
                userlist[msg[0]]['client'].send(char.stats_display().encode("utf8"))
            elif (msg[1] == 'attack'):
                char = userlist[msg[0]]['character']
                enemy = world.ROOMS[char.x][char.y].enemy
                battle_string = ""
                if enemy:
                    print("aata")
                    battle_string = char.attack(enemy)
                    print("apsoefe")
                    if not enemy.is_alive():
                        world.ROOMS[char.x][char.y].enemy = None
                else:
                    battle_string = "There are no enemies here"
                userlist[msg[0]]['client'].send(battle_string.encode("utf8"))

        except ConnectionResetError:
            print(f"Connection reset with {client_addr}!")
            char = userlist[client_addr[0]]['character']
            world.ROOMS[char.x][char.y].users.remove(client_addr[0])
            userlist.pop(client_addr[0], None)
            client.close()
            break

server = socket(AF_INET, SOCK_STREAM)
server.bind((HOST_IP, APP_PORT))
server.listen(MAX_CLIENTS)

broadcast = socket(AF_INET, SOCK_STREAM)
broadcast.bind((HOST_IP, LIS_PORT))
broadcast.listen(MAX_CLIENTS)

world = Map("Lodea")
world.fill_map()
print("server initialized")

threads = {}

while True:
    client, client_addr = server.accept()
    client_, client_addr_ = broadcast.accept()
    if client_addr[0] == client_addr_[0]:
        t = Thread(target=handle_client, args=(client, client_, client_addr))
        threads[client_addr] = t
        threads[client_addr].start()
    else:
        print(" Who are these people? ")

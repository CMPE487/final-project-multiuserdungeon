from socket import *
from config import *
from character import Character, JOBS
from subprocess import call
from sys import stdin
from threading import Thread
import os

BATTLE_MSG = ""

def get_input():
    return stdin.readline().rstrip("\n\r")

def character_creation(server):
    print("You can only have 1 character. If you make a new character the old one will be gone.")
    print("\nEnter your name")
    name = get_input()
    print("Choose a class (1, 2..)")
    for i in range(0, len(JOBS)):
        print("{i}. {job}".format(i=i+1, job=JOBS[i].name))
    job = get_input()
    while not job.isdecimal():
        print("Please enter the number next to the class you want.")
        job = get_input()
    job = JOBS[int(job)-1]
    print("Here is the character you created:")
    a = Character(name, job)
    print(a.stats_display())
    print("Is this OK? (y/n)")
    ans = get_input()
    if ans.startswith('y'):
        server.send((HOST_IP + ";create;" + a.to_json()).encode("utf8"))

def test_commands(server):
    while True:
        call(clear, shell=True)
        server.send(f"{HOST_IP};look;".encode("utf8"))
        room_desc = server.recv(BUFFER_SIZE).decode("utf8")
        print(room_desc)
        print(BATTLE_MSG)
        BATTLE_MSG = ""
        _input = get_input()
        if _input.startswith('user'):
            server.send((HOST_IP + ";show;").encode("utf8"))
            print(server.recv(BUFFER_SIZE).decode("utf8"))
            get_input()
        elif _input.startswith('move'):
            print("Where?")
            dir = get_input()
            while not dir:
                print("Pleaes enter a direction. (West, North, East, South)")
                dir = get_input()
            server.send((HOST_IP + ";move;" + dir.upper()[0]).encode("utf8"))
        elif _input.startswith('map'):
            server.send((HOST_IP + ";map;").encode("utf8"))
            print(server.recv(BUFFER_SIZE).decode("utf8"))
            get_input()
        elif _input.startswith('status'):
            server.send((f'{HOST_IP};status;').encode("utf8"))
            print(server.recv(BUFFER_SIZE).decode("utf8"))
            get_input()
        elif _input.startswith('attack'):
            server.send(f'{HOST_IP};attack;'.encode("utf8"))
            print(server.recv(BUFFER_SIZE).decode("utf8"))
            get_input()
        elif _input.startswith('ambush'):
            server.send((f'{HOST_IP};ambush;').encode("utf8"))
            print(server.recv(BUFFER_SIZE).decode("utf8"))
            get_input()
        elif _input.startswith('help'):
            print("List of commands:")
            print("user: Shows the list of online users")
            print("move: This command allows you to move along the direction you specify. The directions are North, South, West, East")
            print("map: Shows the map and marks your position with *")
            get_input()
        elif _input == "exit":
            print("Goodbye!")
            os.__exit(0)

def listen_server(listen):
    global BATTLE_MSG
    while True:
        BATTLE_MSG += listen.recv(BUFFER_SIZE).decode("utf8") + "\n"

server = socket(AF_INET, SOCK_STREAM)
server.connect((SERVER_IP, APP_PORT)) # Should be SERVER_IP in real servers
listen = socket(AF_INET, SOCK_STREAM)
listen.connect((SERVER_IP, LIS_PORT))
Thread(target=listen_server, args=[listen]).start()

while True:
    call(clear, shell=True)
    print("Welcome!")
    print("1. Make a character")
    print("2. Start adventure")
    _input = get_input()
    if _input.startswith('1'):
        character_creation(server)
    elif _input.startswith('2'):
        test_commands(server)

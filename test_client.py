from socket import *
from config import *
from character import Character, JOBS
from subprocess import call
from sys import stdin

def get_input():
    return stdin.readline().rstrip(" \n\r")

def __a(word):
    if word[0] in "aeiouAEIOU":
        return "an"
    else:
        return "a"

def character_creation(client):
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
    print(f"{a.name} is {__a(a.jobname)} {a.jobname}")
    print(a.stats_display())
    print("Is this OK? (y/n)")
    input = get_input()
    if input.startswith('y'):
        client.send((HOST_IP + ";create;" + a.to_json()).encode("utf8"))

def test_commands(client):
    while True:
        call(clear, shell=True)
        print("1. Show userlist")
        print("2. Move")
        input = get_input()
        if input.startswith('1'):
            client.send((HOST_IP + ";show;").encode("utf8"))
        elif input.startswith('2'):
            print("Where?")
            dir = get_input()
            client.send((HOST_IP + ";move;" + dir.upper()[0]).encode("utf8"))

client = socket(AF_INET, SOCK_STREAM)
client.connect((HOST_IP, APP_PORT)) # Should be SERVER_IP in real clients

while True:
    call(clear, shell=True)
    print("Welcome!")
    print("1. Make a character")
    print("2. Start adventure")
    input = get_input()
    if input.startswith('1'):
        character_creation(client)
    elif input.startswith('2'):
        test_commands(client)

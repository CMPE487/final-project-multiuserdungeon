from socket import *
from config import *
from character import Character, JOBS
from subprocess import call
from sys import stdin

def get_input():
    return stdin.readline().rstrip(" \n\r")


client = socket(AF_INET, SOCK_STREAM)

client.connect((HOST_IP, APP_PORT)) # Should be SERVER_IP in real clients

while True:
    call(clear, shell=True)
    print("Welcome!")
    print("Would you like to make a character? (y/n)")
    input = get_input()
    if input.startswith('y'):
        print("Enter your name")
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
        print("{name} is a {job}".format(name=a.name, job=a.jobname))
        print(a.stats_display())
        print("Is this OK? (y/n)")
        input = get_input()
        if input.startswith('y'):
            client.send(a.to_json().encode("utf8"))
    else:
        pass

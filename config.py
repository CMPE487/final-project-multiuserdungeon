from socket import gethostname, gethostbyname
import os

HOST_IP = gethostbyname(gethostname())
# I don't want to do another discovery, but I guess we will have to
SERVER_IP = '192.168.4.114'
APP_PORT = 3726
LIS_PORT = 3727
BUFFER_SIZE = 1024
MAX_CLIENTS = 10

# I can make it work on Windows!
clear = 'clear'
if os.name == 'nt':
    clear = 'cls'

# Map variables
class MapConfig:
    WIDTH = 8
    HEIGHT = 8
    TOTAL_ROOM_TYPES = 3
    ROOM_GRASS = 1
    ROOM_ROCK =2
    ROOM_WATER = 3

BATTLE_STRING = ""

from socket import gethostname, gethostbyname
import os

HOST_IP = gethostbyname(gethostname())
# I don't want to do another discovery, but I guess we will have to
SERVER_IP = ''
APP_PORT = 3726
BUFFER_SIZE = 1024
MAX_CLIENTS = 10

# I can make it work on Windows!
clear = 'clear'
if os.name == 'nt':
    clear = 'cls'

from socket import *
from config import *
import character

server = socket(AF_INET, SOCK_STREAM)
server.bind(('127.0.0.1', 3726))
server.listen(MAX_CLIENTS)

while True:
    client, client_addr = server.accept()
    print(client.recv(BUFFER_SIZE).decode("utf8"))

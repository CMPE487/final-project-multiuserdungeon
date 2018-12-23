from socket import gethostname, gethostbyname
import os

HOST_IP = gethostbyname(gethostname())
# I don't want to do another discovery, but I guess we will have to
SERVER_IP = '192.168.4.114'
APP_PORT = 3726
LIS_PORT = 3727
BUFFER_SIZE = 1024
MAX_CLIENTS = 10

class Dead:
    check = False
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

class BattleConfig:
    MSG = ""

TITLE_SCREEN ="""
ooooooooo
 888    88o oo oooooo   ooooooo     oooooooo8  ooooooo  oo oooooo    oooooooo8
 888    888  888    888 ooooo888  888    88o 888     888 888   888  888ooooooo
 888    888  888      888    888   888oo888o 888     888 888   888          888
o888ooo88   o888o      88ooo88 8o 888     888  88ooo88  o888o o888o 88oooooo88
                                   888ooo888
                            o888o              `-/++o/-. ```.  `/osss+:-.
                 ooooooo  o888oo           -:/oooo+ss/.` o+y:- ``.-/s+o::/:-.
               888     888 888          ./+/++/o+:+:s    +hhh:`    s:+-+-/+:+/-
               888     888 888        :syyo+ooyssoo-//  -s:/-+h-  .o/+:+s:ossyyo-
                 88ooo88  o888o     -ymNmssyyhddhyssoso-` .-:om/ :ysyoshmosyyyhdh+`
                                   -hsNNdoooo::+hdyhdhyhhs/oydhsyhddhyh+-oyhhhymNNs:
ooooo                                    8888   :y/`.+dhs/ydooys:../+`  -ydmdydm.
 888          ooooooo  oo oooooo     ooooo888 -ooooooooo8//sooooooo     omNhyhds
 888        888     888 888    888 888    888 888oooooo88  ooooo888   .mo`   .-
 888      o 888     888 888        888    888 888        888    888   `s-
o888ooooo88   88ooo88  o888o         88ooo888o  88oooo888 88ooo88 8o  .
                                                       /h.    `-:`
                                                      `o+    :-``/+
                                                       /s        .s
                                                       `+o-```-://
                                                         `.---.`
"""

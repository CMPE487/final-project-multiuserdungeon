from random import randint
from config import MapConfig

class Room(object):
    def __init__(self,x,y,type=None, total=MapConfig.TOTAL_ROOM_TYPES):
        if type is None:
            self.type = randint(1, total)
        else:
            self.type = type
        if (self.type == MapConfig.ROOM_GRASS):
            self.name = "GRASS"
        elif (self.type == MapConfig.ROOM_ROCK):
            self.name = "ROCK"
        elif (self.type == MapConfig.ROOM_WATER):
            self.name = "WATER"
        else:
            self.name = "room"
        self.x , self.y = x,y

    def display(self):
        return f"Name: {self.name} X:{self.x} Y:{self.y} Type:{self.type}"

class Map(object):
    def __init__(self, name, height = MapConfig.HEIGHT, width = MapConfig.WIDTH):
        self.name = name
        self.height = height
        self.width = width
        self.ROOMS = [[Room(0,0,0) for x in range(self.width)] for y in range(self.height)]

    def fill_map(self):
        for dirX in range(self.width):
            for dirY in range(self.height):
                self.ROOMS[dirX][dirY] = Room(dirX,dirY)

    def stats_display(self):
        return "Name: {0} X:{1} Y:{2}".format(
            self.name, self.width , self.height)

    def print_map(self):
        for i in range(self.width*8):
            print("_", end="")
        print()

        for dirX in range(self.width):
            print(end="|  "),
            for dirY in range(self.height):
                print(self.ROOMS[dirX][dirY].name[0], end = "   |   ")
            print()

        for i in range(self.width*8):
            print("_", end="")
        print()

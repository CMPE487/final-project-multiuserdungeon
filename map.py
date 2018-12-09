from random import randint

class Room(object):
    def __init__(self,x,y,type):
        self.name = "Room"
        self.x , self.y = x,y
        self.type = type
        self.change_type(type)

    def stats_display(self):
        return "Name: {0} X:{1} Y:{2} Type:{3}".format(
            self.name, self.x , self.y, self.type)

    def change_type(self,type):
        if (type == ROOM_GRASS):
            self.name = "GRASS"
        elif (type == ROOM_ROCK):
            self.name = "ROCK"
        elif (type == ROOM_WATER):
            self.name = "WATER"


class Map(object):
    def __init__(self, name, height = MAP_HEIGHT, width = MAP_WIDTH):
        self.name = name
        self.height = height
        self.width = width
        self.fill_map(MAP_ROOMS,height,width)
        self.map_rooms = MAP_ROOMS

    def fill_map(self, rooms,height,width):
        for dirX in range(width):
            for dirY in range(height):
                rand = randint(1,TOTAL_ROOM_TYPES)
                rooms[dirX][dirY] = Room(dirX,dirY,rand)

    def stats_display(self):
        return "Name: {0} X:{1} Y:{2}".format(
            self.name, self.width , self.height)

    def print_map(self):
        for i in range(MAP_WIDTH*8):
            print("_", end="")
        print()

        for dirX in range(len(MAP_ROOMS)):
            print(end="|  "),
            for dirY in range(len(MAP_ROOMS[0])):
                print(MAP_ROOMS[dirX][dirY].name[0], end = "   |   ")
            print()

        for i in range(MAP_WIDTH*8):
            print("_", end="")
        print()

MAP_ROOMS = [[Room(0,0,0) for x in range(MAP_WIDTH)] for y in range(MAP_HEIGHT)]

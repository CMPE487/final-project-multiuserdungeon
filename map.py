from random import randint, randrange
from config import MapConfig

class Room(object):
    def __init__(self, x, y):
        self.name = "room"
        self.type = "empty"
        self.x , self.y = x, y
        self.users = []
    def description(self):
        return "This room is empty"
    def display(self):
        return f"Name: {self.name} X:{self.x} Y:{self.y} Type:{self.type}"

class Forest(Room):
    texts = [
      "Overgrown trees surround you. They are towering over the forest.",
      "There are several trees here. One of them is casting a shade on you.",
      "A comforting breeze blows between the leaves."
    ]
    def __init__(self, x, y):
        super().__init__(x, y)
        self.name = "Grassy Fields"
        self.type = "Grass"
        self.x, self.y = x, y
        self.text = self.texts[randrange(3)]
    def description(self):
        return self.text
class Well(Room):
    texts = [
      "There is a stone well here. You wonder if anything happens if you throw something inside.",
      "You see a well in front of you. Leave a penny, and maybe your wish will come true.",
      "There is a bucket hanging from a well in front of you, do you want to take some water?"
    ]
    def __init__(self, x, y):
        super().__init__(x, y)
        self.name = "A Sudden Well"
        self.type = "Water"
        self.x, self.y = x, y
        self.text = self.texts[randrange(3)]
    def description(self):
        return self.text
class Enemy(Room):
    texts = [
      "There is a foul beast here. Luckily it seems to not notice you.",
      "A monster can be heard rustling between the leaves. Be careful.",
      "Wild bird cries come from the skies. Cover your head."
    ]
    def __init__(self, x, y):
        super().__init__(x, y)
        self.name = "Unexpected Enemy"
        self.type = "Enemy"
        self.x, self.y = x, y
        self.text = self.texts[randrange(3)]
    def description(self):
        return self.text

ROOMTYPES = [Forest, Well, Enemy]

class Map(object):
    def __init__(self, name, height = MapConfig.HEIGHT, width = MapConfig.WIDTH):
        self.name = name
        self.height = height
        self.width = width
        self.ROOMS = [[Room(0,0) for x in range(self.width)] for y in range(self.height)]

    def fill_map(self):
        for dirX in range(self.width):
            for dirY in range(self.height):
                self.ROOMS[dirX][dirY] = ROOMTYPES[randrange(3)](dirX, dirY)

    def display_map(self, char_x, char_y):
        str = ""
        for y in range(self.height):
            for x in range(self.width):
                if (x, self.height-y-1) == (char_x, char_y):
                    str += "[*]"
                else:
                    str += "[ ]"
            str += "\n"
        return str

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

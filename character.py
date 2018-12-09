from config import MAP_WIDTH, MAP_HEIGHT

class Job(object):
    def __init__(self):
        self.name = "Adventurer"
        self.hp, self.mp = 10, 10
        self.str, self.end, self.int, self.spd = 5, 5, 5, 5
    def stats_display(self):
        return "HP: {0} MP: {1}\nStr:{2} End:{3} Int:{4} Spd:{5}".format(
            self.hp, self.mp, self.str, self.end, self.int, self.spd)

class Warrior(Job):
    def __init__(self):
        Job.__init__(self)
        self.name = "Warrior"
        self.hp  += 5
        self.str += 3
        self.end += 2

class Mage(Job):
    def __init__(self):
        Job.__init__(self)
        self.name = "Mage"
        self.mp  += 5
        self.int += 3
        self.spd += 2

class Character(object):
    def __init__(self, name, job):
        self.name = name
        self.job = job
        self.jobname = job.name
        self.x, self.y = 0, 0

    def stats_display(self):
        return self.job.stats_display() + "X:{0} Y:{1}".format(self.x, self.y)

    def move(self,dir):
        if((dir == 'N') & (self.y  < MAP_HEIGHT)):
            self.y +=1
        elif((dir == 'S') & (0 < self.y)):
            self.y -=1
        elif((dir == 'W') & (0 < self.x)):
            self.x -=1
        elif((dir == 'E') & (self.x  < MAP_WIDTH)):
            self.x +=1
        else:
            print("You can't move!")

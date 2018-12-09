import Map

class Job(object):
    def __init__(self):
        self.name = "Adventurer"
        self.hp, self.mp = 10, 10
        self.str, self.end, self.int, self.spd = 5, 5, 5, 5
        self.x, self.y = 0, 0
    def stats_display(self):
        return "HP: {0} MP: {1}\nStr:{2} End:{3} Int:{4} Spd:{5} \n X:{6} Y:{7}".format(
            self.hp, self.mp, self.str, self.end, self.int, self.spd, self.x , self.y)

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
    def stats_display(self):
        return self.job.stats_display()

    def move(self,dir):
        if((dir == 'N') & (self.job.y  < Map.MAP_HEIGHT)):
            self.job.y +=1
        elif((dir == 'S') & (0 < self.job.y)):
            self.job.y -=1
        elif((dir == 'W') & (0 < self.job.x)):
            self.job.x -=1
        elif((dir == 'E') & (self.job.x  < Map.MAP_WIDTH)):
            self.job.x +=1
        else:
            print("You can't move!")
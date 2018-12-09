import json
from config import MAP_WIDTH, MAP_HEIGHT

class Job:
    def __init__(self, copy=None):
        if copy is None:
            self.name = "Adventurer"
            self.hp, self.mp = 10, 10
            self.str, self.end, self.int, self.spd = 5, 5, 5, 5
        else:
            self.name = copy.name
            self.hp, self.mp = copy.hp, copy.mp
            self.str, self.end, self.int, self.spd = copy.str, copy.end, copy.int, copy.spd
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

class Character(Job):
    def __init__(self, name="Mark", job=Job(), json_data=None):
        if json_data:
            data = json.loads(json_data)
            name = data['name']
            job = JOBS[data['job_index']]
        Job.__init__(self, job)
        self.name = name
        self.jobname = job.name
        self.x, self.y = 0, 0

    def position(self):
        return "X{0} Y:{1}".format(self.x, self.y)

    def to_json(self):
        job_i = 0
        if self.jobname == "Warrior":
            job_i = 0
        elif self.jobname == "Mage":
            job_i = 1
        data = {'name': self.name, 'job_index': job_i}
        return json.dumps(data)

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

JOBS = [Warrior(), Mage()]

#a = Character("John", Warrior())
#b = Character("Jane", Mage())
#print("{name} is a {job}".format(name=a.name, job=a.jobname))
#print(a.stats_display())
#print("--~--~--~--~--~--")
#print("{name} is a {job}".format(name=b.name, job=b.jobname))
#print(b.stats_display())

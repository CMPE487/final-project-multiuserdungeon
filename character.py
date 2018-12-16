import json
from enemy import Battler
from character_jobs import *
from config import MapConfig

class Character(Job, Battler):
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

    def move(self,dir):
        if((dir == 'N') & (self.y  < MapConfig.HEIGHT)):
            self.y +=1
        elif((dir == 'S') & (0 < self.y)):
            self.y -=1
        elif((dir == 'W') & (0 < self.x)):
            self.x -=1
        elif((dir == 'E') & (self.x  < MapConfig.WIDTH)):
            self.x +=1
        else:
            print("You can't move!")

#a = Character("John", Warrior())
#b = Character("Jane", Mage())
#print("{name} is a {job}".format(name=a.name, job=a.jobname))
#print(a.stats_display())
#print("--~--~--~--~--~--")
#print("{name} is a {job}".format(name=b.name, job=b.jobname))
#print(b.stats_display())

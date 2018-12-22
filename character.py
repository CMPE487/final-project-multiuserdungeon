import json
from enemy import Battler
from character_jobs import *
from config import MapConfig
from threading import Timer

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
        self.__charge = 1

    def position(self):
        return "X{0} Y:{1}".format(self.x, self.y)

    def move(self,dir):
        if((dir == 'N') & (self.y  < MapConfig.HEIGHT-1)):
            self.y +=1
        elif((dir == 'S') & (0 < self.y)):
            self.y -=1
        elif((dir == 'W') & (0 < self.x)):
            self.x -=1
        elif((dir == 'E') & (self.x  < MapConfig.WIDTH-1)):
            self.x +=1
        else:
            print("You can't move!")

    def __gain_charge(self):
        self.__charge += 1

    def attack(self, other):
        if self.__charge > 0:
            self.__charge = 0
            Battler.attack(self, other)
            t = Timer(5 / self.spd, self.__gain_charge)
            t.start()
        else:
            print("You are out of balance!")

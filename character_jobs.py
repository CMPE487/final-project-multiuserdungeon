import util
import json
from enemy import Battler
from threading import Timer

class Job(Battler):
    def __init__(self, copy=None):
        self.desc = ""
        if copy is None:
            self.name = "Adventurer"
            self.hp, self.mp = 10, 10
            self.str, self.end, self.int, self.spd = 5, 5, 5, 5
        else:
            self.name = copy.name
            self.hp, self.mp = copy.hp, copy.mp
            self.str, self.end, self.int, self.spd = copy.str, copy.end, copy.int, copy.spd
        self.__charge = 1

    def stats_display(self):
        return f"{self.name} is {util.a_an(self.jobname)} {self.jobname}\nHP: {self.hp} MP: {self.mp}\nStr:{self.str} End:{ self.end} Int:{self.int} Spd:{self.spd}"
    def short_display(self):
        return f"{self.name} - {self.jobname}"

    def __gain_charge(self):
        self.__charge += 1

    def attack(self, other):
        if self.__charge > 0:
            self.__charge = 0
            str = Battler.attack(self, other)
            t = Timer(5 / self.spd, self.__gain_charge)
            t.start()
            return str
        else:
            return "You are out of balance"

    def to_json(self):
        job_i = 0
        if self.jobname == "Warlord":
            job_i = 0
        elif self.jobname == "Elementalist":
            job_i = 1
        elif self.jobname == "Dragon Knight":
            job_i = 2
        elif self.jobname == "Assassin":
            job_i = 3
        data = {'name': self.name, 'job_index': job_i}
        return json.dumps(data)

class Warlord(Job):
    def __init__(self):
        Job.__init__(self)
        self.name = "Warlord"
        self.hp  += 5
        self.str += 3
        self.end += 2
        self.desc = "A warrior from Crossing Sword Mountains who fights with amazing technique and physical strength."

class Elementalist(Job):
    def __init__(self):
        Job.__init__(self)
        self.name = "Elementalist"
        self.mp  += 5
        self.int += 3
        self.spd += 2
        self.desc = "A master of all elements who dominates the battlefield with storms and fire."

class DragonKnight(Job):
    def __init__(self):
        Job.__init__(self)
        self.name = "Dragon Knight"
        self.hp  += 5
        self.str += 3
        self.mp  += 2
        self.desc = "A proud knight of Alenfel who fights with draconic might and uses mystical powers of their blood."

class Assassin(Job):
    def __init__(self):
        Job.__init__(self)
        self.name = "Assassin"
        self.spd += 5
        self.str += 3
        self.hp  += 2
        self.desc = "A fast and skillful monster hunter who excels at striking their opponent's weak points in a flash."

JOBS = [Warlord(), Elementalist(), DragonKnight(), Assassin()]

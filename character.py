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
    def __init__(self, name, job):
        Job.__init__(self, job)
        self.name = name
        self.jobname = job.name

JOBS = [Warrior(), Mage()]

#a = Character("John", Warrior())
#b = Character("Jane", Mage())
#print("{name} is a {job}".format(name=a.name, job=a.jobname))
#print(a.stats_display())
#print("--~--~--~--~--~--")
#print("{name} is a {job}".format(name=b.name, job=b.jobname))
#print(b.stats_display())

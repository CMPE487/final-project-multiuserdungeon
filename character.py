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
    def stats_display(self):
        return self.job.stats_display()

a = Character("John", Warrior())
b = Character("Jane", Mage())
print("{name} is a {job}".format(name=a.name, job=a.jobname))
print(a.stats_display())
print("--~--~--~--~--~--")
print("{name} is a {job}".format(name=b.name, job=b.jobname))
print(b.stats_display())

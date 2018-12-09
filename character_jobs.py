class Job:
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
    def stats_display(self):
        return "HP: {0} MP: {1}\nStr:{2} End:{3} Int:{4} Spd:{5}".format(
            self.hp, self.mp, self.str, self.end, self.int, self.spd)

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

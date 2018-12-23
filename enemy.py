import json
import time
from threading import Timer, Thread
from random import randrange
from util import endl
from config import BATTLE_STRING

class Battler:
    def calc_damage(attacker, defender):
        return attacker.str / (1 + defender.end / attacker.str)
    def __init__(self, json_data):
        data = json.loads(json_data)
        self.name = data['name']
        self.hp = data['hp']
        self.str = data['str']
        self.end = data['end']

    def attack(self, other):
        dmg = Battler.calc_damage(self, other)
        other.take_damage(dmg)
        str = f"{self.name} attacks {other.name}!\n"
        str += f"Attack deals {dmg} damage.\n"
        str += f"{other.name} has {other.hp} hitpoints left."
        return str

    def take_damage(self, damage):
        self.hp = max(self.hp - damage, 0)

    def is_alive(self):
        return self.hp > 0

class Enemy(Battler):
    def __init__(self, json_data):
        Battler.__init__(self, json_data)
        self.target = None

    def attack(self):
        print(f"{self.target.name} has {self.target.hp} HP left")
        str = ""
        if self.target.hp > 0:
            str = Battler.attack(self, self.target)
        return str

    def change_target(self, targets):
        i = randrange(len(targets))
        while not targets[i].is_alive():
            i = randrange(len(targets))
        print(i)
        self.target = targets[i]

    def combat_ai(self, targets, client_):
        self.change_target(targets)
        ctr = 3
        while True:
            if not self.is_alive():
                print(f"{self.name} is dead")
                return True
            if not all(list(map(lambda x: x.is_alive(), targets))):
                return False
            if ctr == 0:
                t1 = Timer(6, self.change_target, [targets])
                t1.start()
            #t2 = Timer(2, self.attack)
            #t2.start()
            ctr -= 1
            time.sleep(2)
            str = self.attack()
            client_.send(str.encode("utf8"))

goblin_stats = json.dumps({'name': 'Goblin', 'hp': 5, 'str': 3, 'end': 3})

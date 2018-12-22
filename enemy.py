import json
from threading import Timer

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
        other.take_damage(Battler.calc_damage(self, other))

    def take_damage(self, damage):
        self.hp = max(self.hp - damage, 0)

class Enemy(Battler):
    def __init__(self, json_data):
        Battler.__init__(self, json_data)

    def attack(self, other):
        print(f"aaa : {other.hp}")
        if other.hp > 0:
            Battler.attack(self, other)
            t = Timer(2, self.attack, [other])
            t.start()
Goblin = Enemy(json.dumps({'name': 'Goblin', 'hp': 10, 'str': 5, 'end': 5}))

import Map
from character import *

m = Map.Map("World")
print(m.stats_display())
print(m.print_map())

a = Character("John", Warrior())
b = Character("Jane", Mage())
print("{name} is a {job}".format(name=a.name, job=a.jobname))
print(a.stats_display())
print("--~--~--~--~--~--")
print("{name} is a {job}".format(name=b.name, job=b.jobname))
print(b.stats_display())
print("--~--~--~--~--~--")
a.move('N')
print("{name} is a {job}".format(name=a.name, job=a.jobname))
print(a.stats_display())
print("--~--~--~--~--~--")
a.move('W')
print("{name} is a {job}".format(name=a.name, job=a.jobname))
print(a.stats_display())
print("--~--~--~--~--~--")

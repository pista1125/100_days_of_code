from list import data
import random
print(len(data))
def pick():
    pick_1 = random.choice(data)
    data.remove(pick_1)
    print(len(data))
pick()
print(len(data))


list = ["Ajefe", "ere"]
print(list)
def thinking():
    list.remove("ere")
    print(list)
thinking()
print(list)

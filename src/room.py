# Implement a class to hold room information. This should have name and
# description attributes.

import random
from monster import Monster

monster = {
    'Watcher in the Water': Monster("Watcher in the Water",
                                    20, "tentacles"),
    'Orc': Monster("Orc", 5, "sword"),
    'Cave troll': Monster("Cave troll", 40, "club"),
}

class Room:
    def __init__(self, title, description):
        randnum = random.randint(1,20)
        if randnum > 16:
            room_monster=monster['Cave troll']
        elif randnum > 7:
            room_monster=monster['Orc']
        else:
            room_monster=None
        print(randnum)

        self.title = title
        self.description = description
        self.monsters = [room_monster]
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
    def __str__(self):
        str = f"""
              \n----------------------------------
              \n{self.title}
              \n   {self.description}\n"""
        return str
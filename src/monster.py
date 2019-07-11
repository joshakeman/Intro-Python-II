class Monster:
    def __init__(self, name, HP, weapon):
        self.name = name
        self.HP = HP
        self.weapon = weapon
    def __str__(self):
        str = f"""
              \n A {self.title} appears and looks pissed!
              \n   {self.description}\n"""
        return str
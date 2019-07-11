class Monster:
    def __init__(self, name, description, HP):
        self.name = name
        self.description = description
        self.HP = HP
    def __str__(self):
        str = f"""
              \n A {self.title} appears and looks pissed!
              \n   {self.description}\n"""
        return str
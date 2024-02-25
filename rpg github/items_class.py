class Item:
    def __init__(self, name, info):
        self.name = name
        self.info = info

class Weapon(Item): #weapons deal damage to an enemy
    def __init__(self, name, info, atk):
        Item.__init__(self, name, info)
        self.atk = atk #later add magic attack
    def display(self):
        print("++----{}----++".format(self.name))
        print("""
{},
has {} atk """.format(self.info, str(self.atk)))

class Potion(Item):
    def __init__(self, name, info, hp_power):
        Item.__init__(self, name, info)
        self.hp_power = hp_power
    def display(self):
        print("++----{}----++".format(self.name))
        print("""{},
gives player {} health""".format(self.info, str(self.hp_power)))

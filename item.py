"""This is an item in Corban's Inventory"""


class Item:

    def __init__(self, name, description, cost, attack, health, durability):
        self.name = name
        self.description = description
        self.cost = cost
        self.attack = attack
        self.health = health
        self.durability = durability

    def use(self):
        self.durability -= 1
        return self.durability

    def use_attack(self):
        """Returns a tuple (the attack dealt, the remaining durability on the weapon)"""
        return self.attack, self.use()

    def use_health(self):
        """Returns a tuple (the health gained, the remaining durability on the weapon)"""
        return self.health, self.use()

    def __str__(self):
        return self.name + "\t\t\t\t\t\t" + str(self.cost) + "\t\t" + str(self.attack) + \
               "\t\t" + str(self.health) + \
               "\t\t" + str(self.durability)

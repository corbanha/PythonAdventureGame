"""Here is a very basic enemy shell to be used for the game"""


class Enemy:

    def __init__(self, name, health, armor, attack):
        self.name = name
        self.health = health
        self.armor = armor
        self.attack = attack

    def receive_attack(self, attack):
        print()
        if self.armor > attack:
            print(self.name + "'s armor blocked half of your attack")
            attack /= 2
            self.armor -= 2
        elif self.armor > 0:
            print(self.name + "'s armor blocked 2 pts of your attack")
            attack -= 2
            self.armor -= 1

        if self.armor < 0:
            self.armor = 0

        print("You got " + self.name + " with " + str(attack) + " attack pts")

        self.health -= attack

        if self.health < 0:
            self.health = 0


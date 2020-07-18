import random
class Creature:
    def __init__(self, name, level):
        self.level = level
        self.name = name

    def defensive_roll(self):
        roll = random.randint(1, 12)
        return roll * self.level


class Dragon(Creature):
    def __init__(self, name, level, magic_armor, breathing_fire=False):
        super().__init__(name, level)
        self.breathing_fire = breathing_fire
        self.magic_armor = magic_armor

    def defensive_roll(self):
        # value = super().defensive_roll()
        roll = random.randint(1, 12)
        roll += self.magic_armor
        if self.breathing_fire:
            roll *= 2
        return roll * self.level


class Wizard(Creature):

    def attack(self, other_creature):
        my_roll = self.defensive_roll()
        their_roll = other_creature.defensive_roll()

        return my_roll >= their_roll

hero = Wizard("Harry", 50)
monster = Creature("Bat", 1)
print(dir(monster))
print(hero.attack(monster))
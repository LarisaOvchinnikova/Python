import random

class Creature:
    def __init__(self, name, level = 1):
        self.name = name
        self.level = level

    # Кидаем кубик от 1 до 12 и атакой существа будет результат броска умноженый на левел
    def defensive_roll(self):
        roll = random.randint(1,12)
        return roll * self.level

class Dragon(Creature):
    def __init__(self, name, level, breaths_fire):
        # Добавляем еще один атрибут для класса Дракон breaths fire,
        # а name и level инициализируется в классе Creature
        super().__init__(name, level)
        self.breaths_fire = breaths_fire

    def defensive_roll(self):
        roll = super().defensive_roll()
        # Урон дракона будет умножаться на два если breaths_fire == True
        if self.breaths_fire:
            roll *= 2
        return roll

class Wizard(Creature):
    # Волшебник может атаковать. Функция принимает как параметр
    # другое существо и вызывает его такой же метод defensive_roll()
    # В случае победы возвращает True
    def attack(self, enemy):
        my_roll = self.defensive_roll()
        their_roll = enemy.defensive_roll()
        return my_roll

def print_header():
    # Просто красивый заголовок
    print("----------------------------------------------")
    print("                WIZARD GAME                   ")
    print("----------------------------------------------")
    print()

print_header()

# Создаем список существ для игры
creatures = [
    Creature("Bat", 5),
    Creature("Toad", 1),
    Creature("Tiger", 12),
    Dragon("Black Dragon", 50, False),
    Wizard("Evil Wizard", 1000)
]

hero = Wizard("Harry", 75)

while True:
    # Каждый ход выбирает случайное существо из списка
    active_creature = random.choice(creatures)
    print(f"A {active_creature.name} of level {active_creature.level} has appear from a dark and foggy forest...\n")

    cmd = input("Do you [a]ttack, [r]unaway, or [l]ook around? ")
    if cmd == "a":
        if hero.attack(active_creature):
            creatures.remove(active_creature)
            print(f"The wizard defeated {active_creature.name}")
        else:
            print(f"The wizard has been defeat by the powerful {active_creature.name}")

    elif cmd == "r":
        print("The wizard has become unsure of his power and flees!!!")

    elif cmd == "l":
        # Осматриваемся - печатаем список оставшихся существ.
        print(f"The wizard {hero.name} takes in the surroundings and sees: ")
        for c in creatures:
            print(f" * {c.name} of level {c.level}")

    else:
        # если ввели что-то другое
        print("OK, exiting game ... bye!")
        break

    if not creatures:
        # или уже победили всех существ
        print("You've defeated all the creatures, well done!")
        break

    print()







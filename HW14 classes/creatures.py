import random

class Creature:
    def __init__(self, name, level = 1):
        self.name = name
        self.level = level

    def greet(self):
        print(f"Hello I'm {self.name}, I have {self.level} level")

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
            print("DIE")
            roll *= 2
        return roll

class Wizard(Creature):
    # Волшебник может атаковать. Функция принимает как параметр
    # другое существо и вызывает его такой же метод defensive_roll()
    # В случае победы возвращает True
    def attack(self, enemy):
        my_roll = self.defensive_roll()
        print(my_roll)
        their_roll = enemy.defensive_roll()
        print(their_roll)
        return my_roll >= their_roll


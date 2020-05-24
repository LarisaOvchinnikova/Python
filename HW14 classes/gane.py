from creatures import Creature, Wizard, Dragon
import random

def print_header():
    print("----------------------------------------------")
    print("                WIZARD GAME                   ")
    print("----------------------------------------------")
    print()

def main():
    print_header()

    creatures = [
        Creature("Bat", 5),
        Creature("Toad", 1),
        Creature("Tiger", 12),
        Dragon("Black Dragon", 50, False),
        Wizard("Evil Wizard", 1000)
    ]

    hero = Wizard("Harry", 75)

    while True:
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
            print(f"The wizard {hero.name} takes in the surroundings and sees: ")
            for c in creatures:
                print(f" * {c.name} of level {c.level}")

        else:
            print("OK, exiting game ... bye!")
            break

        if not creatures:
            print("You've defeated all the creatures, well done!")
            break

    print()


main()
"""
Creature and creature subclass definitions.
"""

import random
import time


# TODO: Add Inventory
class Creature:
    """
    Base for Players and Monsters. This is where you define all things that are
    common to both players and monsters.
    """
    def __init__(self, name, hp, strength, speed, defense):
        self.name = name
        self.hp = hp
        self.strength = strength
        self.speed = speed
        self.defense = defense

    def attack(self, other):
        """Attack another creature."""
        damage_dealt = self.strength - other.defense
        other.hp -= damage_dealt
        print(
            "{} attacks {} -- {} damage dealt!".format(
                self.name, other.name, damage_dealt
            )
        )

    def use_item(self, used):
        used1 = used.hpboost
        used2 = used.strboost
        used3 = used.spdboost
        used4 = used.defboost
        print("{},{},{},{}".format(used1, used2, used3, used4))

    def run(self, other):
        getaway = self.speed - other.speed
        if getaway < 0:
            number2 = random.randint(0, 1)
            if number2 == 1:
                half_damage = self.strength/2 - other.defense
                other.hp -= half_damage
                print(
                    "{} couldn't get away and got attacked, {} damage dealt"
                    .format(self.name, half_damage)
                )

            elif number2 == 2:
                self.attack(other)
                print(
                    "{} has {} health left"
                    .format(other.name, other.hp)
                )

            else:
                print("ummm, there was an error.")
                time.sleep(5)
                print("sending you back now")

        elif getaway > 0:
            print("{} got away.".format(other.name))
            time.sleep(5)

        else:
            print("{} couldn't get away, but you avoided the counter attack.")


class Player(Creature):
    """
    Container for Player attributes.
    """

    def __init__(self, klass, name, hp, strength, speed, defense):
        # Call Creature initializer, which means we dont have to
        # set HP, strength, speed, and defense, manually
        super().__init__(name, hp, strength, speed, defense)

        # Do player specific setup
        self.klass = klass


class Fighter(Player):
    """Fighter Player Class."""
    HP = 16
    STRENGTH = 15
    SPEED = 5
    DEFENSE = 10
    CLASS = "Fighter"

    def __init__(self, name):
        super().__init__(
            self.CLASS, name, self.HP, self.STRENGTH, self.SPEED, self.DEFENSE
        )


class Rouge(Player):
    """Rouge Player Class."""
    HP = 15
    STRENGTH = 10
    SPEED = 15
    DEFENSE = 5
    CLASS = "Rouge"

    def __init__(self, name):
        super().__init__(
            self.CLASS, name, self.HP, self.STRENGTH, self.SPEED, self.DEFENSE
        )


class Mage(Player):
    """Mage Player Class."""
    HP = 10
    STRENGTH = 20
    SPEED = 5
    DEFENSE = 5
    CLASS = "Mage"

    def __init__(self, name):
        super().__init__(
            self.CLASS, name, self.HP, self.STRENGTH, self.SPEED, self.DEFENSE
        )


class Monster(Creature):
    """
    Container for monster attributes.
    """

    def __init__(self, home, name, hp, strength, speed, defense, gold):
        # Call creature initializer, which means that we don't have to
        # set hp, strength, speed, and defense manually here
        super().__init__(name, hp, strength, speed, defense)

        # Do monster specific setup
        self.home = home
        self.gold = gold

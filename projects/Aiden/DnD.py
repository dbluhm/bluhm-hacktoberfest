import random
import time
from collections import namedtuple

def accident:
    print("that wasn't an option, you have to type it as it is seen.")
    time.delay 30
    print("go on, type it correctly.")



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
        damage_dealt = self.strength - other.defense
        other.hp -= damage_dealt
        print("{} attacks {} -- {} damage dealt!".format(self.name, other.name, damage_dealt))

    def run(self, other):
        getaway = self.speed - other.speed
        if getaway < 0:
            number2 = random.uniform(0,3)
            number2 = int(number2)
            if number2 = 1:
                half_damage = self.strength/2 - other.defense
                other.hp -= half_damage
            print("{} couldn't get away and got attacked, {} damage dealt".format(self.name, half_damage)
            elif number2 = 2:
                self.attack(other)
                print("{} has {} health left".format(other.name, other.hp))
            elif int(number2) = 3:
                print("{} couldn't get away, but you avoided the counter attack.")
            elif number2 != 1, 2:
                print("ummm, there was an error.")
                time.delay 30
                print("sending you back now")
                #im not entirely sure how to send it back to the number2 random number generator...
        elif: getaway > 0:
            print("{} got away.")
            time.delay 30


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
# This is the Data structure that will hold our region info
class Region:
    """
    Container for region info.
    """
    def __init__(self, required, completed):
        self.required = required
        self.completed = completed

# Global variables for our players
player_fighter = Player("fighter", "Bob the Great", hp=15, strength=15, speed=5, defense=10)
player_rouge = Player("rouge", "Thievy McTheivface", hp=15, strength=10, speed=15, defense=5)
player_mage = Player("mage", "The Mad Hatter", hp=10, strength=20, speed=5, defense=5)

player_rouge.attack(player_mage)
print("{} has {} health left".format(player_mage.name, player_mage.hp))

# This is the global variable that is our Forest region
forest = Region(required=10, completed=0)




#this is the item define
class item:
    """
    container for item info
    """
    def __init__(self, hpboost, strboost, spdboost, defboost)
        self.hpboost = hpboost
        self.strboost = strboost
        self.spdboost = spdboost
        self.defboost = defboost

potion = item(hpboost=5, strboost=0, spdboost=0, defboost=0)



class market:
    """
    container for item costs
    """
    def __init__(self, cost)
        self.cost = cost



#this is the inventory
inventory = ()



#this is the Individual monster stats
Ogre = Monster(Creature)("hills","Ogre", hp=5, strength=5, speed=1, defense=3, gold=2)
Wolves = Monster(Creature)("forest", "wolves", hp=5, strength=5, speed=10, defense=5, gold=4)
Giant_Cobra = Monster(Creature)("Forest", "Giant Cobra", hp=5, strength=5, speed=5, defense=5, gold=3)
Terasque = Monster(Creature)("none", "Terasque", hp=20, strength=20, speed=5, defense=30, gold=20)
Bandits = Monster(Creature)("Forest", "Bandits", hp=5, strength=5, speed=5, defense=3, gold=3)
Bear = Monster(Creature)("Forest", "Bear", hp=10, strength=10, speed=5, defense=5, gold=5)


#this is the random number generator
EN = random.uniform(0, 20)
EN = int(EN)

def numberE ():
    return numberENC - forest.completed




potion = used
def use_item ():
    used1 = used.hpboost
    used2 = used.strboost
    used3 = used.spdboost
    used4 = used.defboost
    print("{},{},{},{}".format(used1, used2, used3, used4))



ForestIN = {
    "1":lambda Fcreature: "Ogre",
    "2":lambda Fcreature: "a giant cobra, Lose 2 HP",
    "3":lambda Fcreature: "a terasque, Lose 3 HP",
    "4":lambda Fcreature: "wolves, Lose 1 HP",
    "5":lambda Fcreature: "bandits, Lose 1 HP",
    "6":lambda Fcreature: "a bear, Lose 2 HP",
    "7":lambda Fcreature: "giant weasles, Lose 2 HP",
    "8":lambda Fcreature: "bandits, Lose 1 HP",
    "9":lambda Fcreature: "treants, Lose 2 HP",
    "10":lambda Fcreature: "bandits, Lose 1 HP",
    "11":lambda Fcreature: "a giant venus flytrap, lose 2 HP",
    "12":lambda Fcreature: "a eagle, Lose 2 HP",
    "13":lambda Fcreature: "a dragon, Lose 3 HP",
    "14":lambda Fcreature: "goblins, Lose 1 HP",
    "15":lambda Fcreature: "an imp, you lost your weapon",
    "16":lambda Fcreature: "dryad, Gain 1 HP",
    "17":lambda Fcreature: "a troll, Lose 2 HP",
    "18":lambda Fcreature: "goblins, Lose 1 HP",
    "19":lambda Fcreature: "bandits, Lose 1 HP",
    "20":lambda Fcreature: "sprites, You get distracted in the forest and get lost."
}
Fcreature = ForestIN




def encounter ():
    print("you encounter {}!".format(ForestIN[str(EN)](str(Fcreature))))


def regions ():
    encounter()
    forest.completed += 1
    numberE()

def Forestmain ():
    numberENC = 10
    if numberENC < 0:
        encounter()
        forest.completed += 1
        numberE()
    elif numberENC == 0:
        print("which region do you want to go to? ")

def choice ():


# This is the mian function this is the first function that the script
# will execute. All functions should be called from main
def main():
    print("Welcome to text legends!")
    time.delay 15
    print("This is a text based game where your goal is to survive as an adventurer as long as possible.")
    time.delay 15
    print("You may type exit at any time to exit the game.")
    time.delay 15
    print("Type start to begin.")
    action = input()
    action = action.lower

#here is the game loop
    action = ""
    while action != start:
        accident()
    else:
        choice()


if __name__ == "__main__":
    main()

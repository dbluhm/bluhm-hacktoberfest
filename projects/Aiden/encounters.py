"""Encounters and monsters."""

import random
from utils import uniquestr
from creatures import Monster


# This is the Data structure that will hold our region info
class Region:
    """
    Container for region info.
    """
    def __init__(self, required, completed):
        self.required = required
        self.completed = completed


#this is the Individual monster stats
Ogre = Monster("hills", "Ogre", hp=5, strength=5, speed=1, defense=3, gold=2)
Wolves = Monster("forest", "wolves", hp=5, strength=5, speed=10, defense=5, gold=4)
Giant_Cobra = Monster("Forest", "Giant Cobra", hp=5, strength=5, speed=5, defense=5, gold=3)
Terasque = Monster("none", "Terasque", hp=20, strength=20, speed=5, defense=30, gold=20)
Bandits = Monster("Forest", "Bandits", hp=5, strength=5, speed=5, defense=3, gold=3)
Bear = Monster("Forest", "Bear", hp=10, strength=10, speed=5, defense=5, gold=5)


#this is the random number generator
EN = random.uniform(0, 20)
EN = int(EN)

# This is the global variable that is our Forest region
forest = Region(required=10, completed=0)


ForestIN = {
    "1": lambda Fcreature: "Ogre",
    "2": lambda Fcreature: "Giant Cobra",
    "3": lambda Fcreature: "Terasque",
    "4": lambda Fcreature: "Wolves",
    "5": lambda Fcreature: "Bandits",
    "6": lambda Fcreature: "a bear, Lose 2 HP",
    "7": lambda Fcreature: "giant weasles, Lose 2 HP",
    "8": lambda Fcreature: "bandits, Lose 1 HP",
    "9": lambda Fcreature: "treants, Lose 2 HP",
    "10": lambda Fcreature: "bandits, Lose 1 HP",
    "11": lambda Fcreature: "a giant venus flytrap, lose 2 HP",
    "12": lambda Fcreature: "a eagle, Lose 2 HP",
    "13": lambda Fcreature: "a dragon, Lose 3 HP",
    "14": lambda Fcreature: "goblins, Lose 1 HP",
    "15": lambda Fcreature: "an imp, you lost your weapon",
    "16": lambda Fcreature: "dryad, Gain 1 HP",
    "17": lambda Fcreature: "a troll, Lose 2 HP",
    "18": lambda Fcreature: "goblins, Lose 1 HP",
    "19": lambda Fcreature: "bandits, Lose 1 HP",
    "20": lambda Fcreature: "sprites, You get distracted in the forest and get lost."
}
Fcreature = ForestIN


def encounter():
    print("you encounter {}!".format(ForestIN[str(EN)](str(Fcreature))))


def choice():
    print("you encounter an {}")
    print("would you like to attack or run?")
    decision = input()
    decision = decision.lower
    decision = uniquestr(
        '',
        "That doesnt appear to have been an option, type it correctly.",
        {'attack', 'run'}
    )

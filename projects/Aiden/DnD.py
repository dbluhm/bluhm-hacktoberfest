import random
import time

from creatures import Fighter, Mage, Rouge
from utils import uniquestr

def accident():
    print("that wasn't an option, you have to type it as it is seen.")
    time.sleep(5)
    print("go on, type it correctly.")


def intro():
    """Provide introduction, wait for player to start."""
    print("Welcome to text legends!")
    time.sleep(2)
    print(
        "This is a text based game where your goal is to survive as an "
        "adventurer as long as possible."
    )
    time.sleep(2)
    print("You may type exit at any time to exit the game.")
    time.sleep(2)
    print("Type start to begin.")
    uniquestr(
        '',
        "That wasn't an option! Type it corretly, please!",
        {'start'}
    )


def player_selection():
    """Prompt player."""
    print('PLAYER SELECTION HAPPENS HERE')
    return []


def game(players):
    print("DOING STUFF WITH PLAYERS {}".format(players))


def main():
    """
    This is the main function this is the first function that the script
    will execute. All functions should be called from main.
    """
    intro()
    players = player_selection()
    game(players)



if __name__ == "__main__":
    main()

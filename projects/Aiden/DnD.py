import random
import time

from creatures import Fighter, Mage, Rouge
from utils import uniquestr, inputstr

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
    print('Please select your player class.')
    print('Your options are Figher, Mage, or Rouge.')
    player_class = uniquestr(
        'Class (Fighter, Mage, or Rouge): ',
        "That wasn't right... Try again.",
        {'fighter', 'mage', 'rouge'}
    )
    name = inputstr('Enter your player name: ')
    player_class = player_class.lower()

    if player_class == 'fighter':
        player = Fighter(name)
    elif player_class == 'mage':
        player = Mage(name)
    elif player_class == 'rogue':
        player = Rogue(name)

    return player


def game(player):
    print("DOING STUFF WITH PLAYER {}".format(player.name))


def main():
    """
    This is the main function this is the first function that the script
    will execute. All functions should be called from main.
    """
    intro()
    player = player_selection()
    game(player)



if __name__ == "__main__":
    main()

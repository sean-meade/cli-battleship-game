import random
from player_board import LETTERS, NUMS, SHIP_CHARACTER
from termcolor import colored
import os
from time import sleep

def convert_coords(coords):
    """
    Converts the number and letter given from the user into usable ints
    
    coords = a string containing coordinates on the board (e.g. "5d")

    returns two integers that represent the position of the board
    """
    x_and_y = list(coords)
    x_coords = int(x_and_y[0])
    y_coords = 9 - (ord((x_and_y[1]).lower()) - 97)

    return x_coords, y_coords


def comp_random_choice_of_coords():
    """
    Choose random coords for comp

    returns a string of the coords with number and letter
    """
    coords = str(random.randint(0, 9)) + LETTERS[random.randint(0, 9)]

    return coords


def attack(opponents_board):
    """
    Attacks the opponents board
    players_board = current players PlayerBoard
    attack_coords = a string containing coordinates on the board (e.g. "5d")
    """
    clearConsole()
    print(f"{opponents_board.name} is being attacked!")
    opponents_board.print_board()

    # If player is attacking the computer
    if opponents_board.name == "comp":
        # prompt user to choose attack coordinates
        attack_coords = input(colored("Choose attach coords (e.g. 3e, 7f):\n", "green"))

        try:
            if (attack_coords[1].lower() in LETTERS) and (attack_coords[0] in NUMS):
                pass
            else:
                raise ValueError()
            # if not get player to try again
        except ValueError():
            clearConsole()
            print(colored(
                "Please choose coordinates with a number (0-9) followed by a letter (a-j)",
                "red"))
            sleep(1)
            attack(opponents_board)
        
    else:
        attack_coords = comp_random_choice_of_coords()

    x_coords, y_coords = convert_coords(attack_coords)
    target = opponents_board.board[y_coords][x_coords]

    if opponents_board.name != "comp":
        name = "Computer"
    else:
        name = "You"

    # Check if its a hit ("x"), a miss ("o"), or if player has already attacked there
    if target == opponents_board.symbol:
        clearConsole()
        opponents_board.board[y_coords][x_coords] = colored("o", "red")
        print(f"{name} Missed: o")
        opponents_board.print_board()
        sleep(2)
    elif target == SHIP_CHARACTER:
        clearConsole()
        opponents_board.board[y_coords][x_coords] = colored("X", "green")
        opponents_board.hits += 1
        print(colored(f"{name} Hit: X", "green"))
        opponents_board.print_board()
        sleep(2)
    else:
        print(colored("Sorry you've already attacked there", "red"))
        attack(opponents_board)


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

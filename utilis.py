import random
from player_board import LETTERS, NUMS, SHIP_CHARACTER
from termcolor import colored

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

    # If player is attacking the computer
    if opponents_board.name == "comp":
        # prompt user to choose attack coordinates
        attack_coords = input(colored("Choose attach coords (e.g. 3e, 7f):\n", "green"))

        # check to see if second character is a letter in LETTERS
        # if not get player to try again
        try:
            attack_coords[1].lower() in LETTERS
            attack_coords[0] in NUMS
        except:
            print(colored("Please choose a letter between a and j", "red"))
            attack(opponents_board)
    else:
        attack_coords = comp_random_choice_of_coords()

    x_coords, y_coords = convert_coords(attack_coords)
    target = opponents_board.board[y_coords][x_coords]

    # Check if its a hit ("x"), a miss ("o"), or if player has already attacked there
    if target == opponents_board.symbol:
        opponents_board.board[y_coords][x_coords] = "o"
    elif target == SHIP_CHARACTER:
        opponents_board.board[y_coords][x_coords] = "X"
        opponents_board.hits += 1
    else:
        print(colored("Sorry you've already attacked there", "red"))
        attack(opponents_board)







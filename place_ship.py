from player_board import DIRECTIONS, LETTERS, COLUMNS, SHIP_CHARACTER
from termcolor import colored
from utilis import comp_random_choice_of_coords, convert_coords
import random

def choose_placement_of_ship(players_board, size):
    """
    Function that gets users placement options
    players_board = current players PlayerBoard
    size = size of ship
    """

    # If it's the computer randomly choose placement options otherwise ask the user for theirs
    if players_board.name == "comp":
        starting_point = comp_random_choice_of_coords()
        direction = DIRECTIONS[random.randint(0, 3)]
    else:
        players_board.print_board()
        print(f"\n Place ship of size {size}")
        starting_point = input(colored("Choose starting point of ship (e.g. 6f):\n", "green"))
        if starting_point[1].lower() not in LETTERS:
            print(colored("Please choose a letter between a and j", "red"))
            choose_placement_of_ship(players_board, size)
            return
        direction = input(colored("\nChoose direction of the ship (e.g. UP, DOWN, LEFT, or RIGHT):\n", "green"))
    place_ship(players_board, starting_point, direction, size)


def ship_wont_fit_on_board(players_board, size):
    """ Called when ship wont fit on board """
    if players_board.name != "comp":
        print(colored("ship won't fit on board try again", "red"))
    choose_placement_of_ship(players_board, size)

def check_ship_already_placed(players_board, y_coord, x_coord, size):
    """
    Checks if another ship is in the way and if not return coords
    """
    space = players_board.board[y_coord][x_coord]
    if space != players_board.symbol:
        if players_board.name != "comp":
            print(colored("You already have a ship there try again", "red"))
        choose_placement_of_ship(players_board, size)
        return False
    else:
        return [y_coord, x_coord]

def place_ship(players_board, starting_point, direction, size):
    """
    Function takes a Board, a starting point on that Board, a direction
    and size of a ship and places it on the Board
    players_board = the current players PlayerBoard
    starting_point = a sting containing coords to place the ship (e.g. "7j")
    direction = the direction of the ship should go in (e.g. "up", "down", "left", "right")
    size = size of the ship being placed
    """

    # the starting point converted to integers
    x_coords, y_coords = convert_coords(starting_point)
    # the direction string converted to upper case
    direction_upper = direction.upper()
    # empty list used to check if a player has already placed a ship there
    spaces = []

    try:
        # Placing a ship in the up direction
        if direction_upper == "UP":
            # If the ship runs off the board try again
            if y_coords - (size - 1) < 0:
                ship_wont_fit_on_board(players_board, size)
                return
            # Check to see if there is a ship already in the way
            while True:
                for y_up in range(y_coords - (size - 1), y_coords + 1):
                    if not check_ship_already_placed(players_board, y_up, x_coords, size):
                        spaces = []
                        break
                    else:
                        space = check_ship_already_placed(players_board, y_up, x_coords, size)
                        spaces.append(space)
                break

        # Placing a ship in the down direction
        elif direction_upper == "DOWN":
            # If the ship runs off the board try again
            if y_coords + size > COLUMNS:
                ship_wont_fit_on_board(players_board, size)
                return
            # Check to see if there is a ship already in the way
            while True:
                for y_down in range(y_coords, y_coords + size):
                    if not check_ship_already_placed(players_board, y_down, x_coords, size):
                        spaces = []
                        break
                    else:
                        space = check_ship_already_placed(players_board, y_down, x_coords, size)
                        spaces.append(space)
                break

        # Placing a ship in the right direction
        elif direction_upper == "RIGHT":
            # If the ship runs off the board try again
            if x_coords + size > COLUMNS:
                ship_wont_fit_on_board(players_board, size)
                return
            # Check to see if there is a ship already in the way
            while True:
                for x_right in range(x_coords, x_coords + size):
                    if not check_ship_already_placed(players_board, y_coords, x_right, size):
                        spaces = []
                        break
                    else:
                        space = check_ship_already_placed(players_board, y_coords, x_right, size)
                        spaces.append(space)
                break


        # Placing a ship in the left direction
        elif direction_upper == "LEFT":
            # If the ship runs off the board try again
            if x_coords - (size - 1) < 0:
                ship_wont_fit_on_board(players_board, size)
                return
            # Check to see if there is a ship already in the way
            while True:
                for x_left in range(x_coords - (size - 1), x_coords + 1):
                    if not check_ship_already_placed(players_board, y_coords, x_left, size):
                        spaces = []
                        break
                    else:
                        space = check_ship_already_placed(players_board, y_coords, x_left, size)
                        spaces.append(space)
                break

        else:
            print(colored("You need to choose up, down, left, or right as a direction.", "red"))
            choose_placement_of_ship(players_board, size)
            

        # If it'll fit and no ships in the way place the ship
        for coords in spaces:
            players_board.board[coords[0]][coords[1]] = SHIP_CHARACTER

    except (AttributeError, ValueError):
        print(colored("Use valid coords a number (0-9) followed by a letter (a-j) e.g. 3e", "red"))
        choose_placement_of_ship(players_board, size)

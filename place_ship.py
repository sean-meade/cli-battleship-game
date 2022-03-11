from player_board import DIRECTIONS, LETTERS, NUMS, COLUMNS, SHIP_CHARACTER,COMP
from termcolor import colored
from utilis import comp_random_choice_of_coords, convert_coords
import random
from utilis import clear_console
from time import sleep


def choose_placement_of_ship(players_board, size):
    """
    Function that gets users placement options
    players_board = current players PlayerBoard
    size = size of ship
    """

    # If it's the computer randomly choose placement options
    # otherwise ask the user for theirs
    if players_board.name == COMP:
        starting_point = comp_random_choice_of_coords()
        direction = DIRECTIONS[random.randint(0, 3)]
    else:
        players_board.print_board()
        print(f"\n The ship you're currently placing needs {size} spaces")
        starting_point = input(
            colored("Choose starting point of ship (e.g. 6f):\n", "green")
        )
        # get direction from user
        direction = input(
            colored(
                "\nChoose the direction you want the ship to point (e.g. UP, DOWN, LEFT, or RIGHT):\n",
                "green",
            )
        )
        # In starting point check to see if there is an integer
        # in NUMS as the first character and letter in LETTERS
        try:
            letter = starting_point[1].lower()
            num = starting_point[0]
            direct_lower = direction.lower()
            if letter in LETTERS and num in NUMS and direct_lower in DIRECTIONS:
                pass
            else:
                raise ValueError()
        # if not get player to try again
        except (ValueError, IndexError):
            clear_console()
            print(
                colored(
                    """Please use coordinates on the board and a direction.
Coordinates: A number (0-9) followed by a letter (a-j) e.g 9c
Directions: up, down, right, or left""",
                    "red",
                )
            )
            sleep(1)
            choose_placement_of_ship(players_board, size)
            return
    # Place ship on board
    place_ship(players_board, starting_point, direction, size)


def ship_wont_fit_on_board(players_board, size):
    """
    Called when ship wont fit on board

    players_board = PlayerBoard: current players board
    size = int: spaces the ship takes up
    """
    # If the current player is user (not comp) then print
    if players_board.name != COMP:
        print(colored("That ship won't fit on board that way please try again",
                      "red"))
    # choose placement again
    choose_placement_of_ship(players_board, size)


def check_ship_already_placed(players_board, y_coord, x_coord, size):
    """
    Checks if another ship is in the way and if not return coords.
    y_coord & x_coord make the coordinates on the board that are
    being checked.

    players_board = PlayerBoard: current players board
    y_coord = int: coordinate on the y axis converted to 0 - 1
    x_coord = int: coordinate on the x axis
    size = int: spaces the ship takes up
    """

    # get the symbol of the location
    space_symbol = players_board.board[y_coord][x_coord]

    # if its different from the symbol the board was created with
    # then restart placement of ship otherwise return x and y coords
    if space_symbol != players_board.symbol:
        if players_board.name != COMP:
            clear_console()
            print(colored("You already have a ship there please try again",
                          "red"))
        choose_placement_of_ship(players_board, size)
        return False
    else:
        return [y_coord, x_coord]


def place_ship(players_board, starting_point, direction, size):
    """
    Function takes a Board, a starting point on that Board, a direction
    and size of a ship and places it on the Board.

    players_board = the current players PlayerBoard
    starting_point = a sting containing coords to place the ship (e.g. "7j")
    direction = the direction of the ship should go in
                    (e.g. "up", "down", "left", "right")
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
            # if not gather spaces to use to add ship
            while True:
                for y_up in range(y_coords - (size - 1), y_coords + 1):
                    ship_there = check_ship_already_placed(
                        players_board, y_up, x_coords, size
                    )
                    if not ship_there:
                        spaces = []
                        break
                    else:
                        spaces.append(ship_there)
                break
        # Placing a ship in the down direction
        elif direction_upper == "DOWN":
            # If the ship runs off the board try again
            if y_coords + size > COLUMNS:
                ship_wont_fit_on_board(players_board, size)
                return
            # Check to see if there is a ship already in the way
            # if not gather spaces to use to add ship
            while True:
                for y_down in range(y_coords, y_coords + size):
                    ship_there = check_ship_already_placed(
                        players_board, y_down, x_coords, size
                    )
                    if not ship_there:
                        spaces = []
                        break
                    else:
                        spaces.append(ship_there)
                break
        # Placing a ship in the right direction
        elif direction_upper == "RIGHT":
            # If the ship runs off the board try again
            if x_coords + size > COLUMNS:
                ship_wont_fit_on_board(players_board, size)
                return
            # Check to see if there is a ship already in the way
            # if not gather spaces to use to add ship
            while True:
                for x_right in range(x_coords, x_coords + size):
                    ship_there = check_ship_already_placed(
                        players_board, y_coords, x_right, size
                    )
                    if not ship_there:
                        spaces = []
                        break
                    else:
                        spaces.append(ship_there)
                break
        # Placing a ship in the left direction
        elif direction_upper == "LEFT":
            # If the ship runs off the board try again
            if x_coords - (size - 1) < 0:
                ship_wont_fit_on_board(players_board, size)
                return
            # Check to see if there is a ship already in the way
            # if not gather spaces to use to add ship
            while True:
                for x_left in range(x_coords - (size - 1), x_coords + 1):
                    ship_there = check_ship_already_placed(
                        players_board, y_coords, x_left, size
                    )
                    if not ship_there:
                        spaces = []
                        break
                    else:
                        spaces.append(ship_there)
                break
        # If it'll fit and no ships in the way place the ship
        for coords in spaces:
            players_board.board[coords[0]][coords[1]] = SHIP_CHARACTER
    # Catch any errors and ask user to go again
    except (AttributeError, ValueError, IndexError):
        print(
            colored(
                "Use valid coords a number (0-9) followed by a letter (a-j) e.g. 3e",
                "red",
            )
        )
        choose_placement_of_ship(players_board, size)

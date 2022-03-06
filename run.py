import random
from termcolor import colored
from player_board import PlayerBoard, SHIP_CHARACTER, LETTERS, DIRECTIONS, COLUMNS

ship_sizes = [2, 3, 3, 4, 5]

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


def comp_random_choice_of_coords():
    """
    Choose random coords for comp
    """
    coords = str(random.randint(0, 9)) + LETTERS[random.randint(0, 9)]

    return coords


def choose_placement_of_ship(players_board, size):
    """
    Function that gets users placement options
    players_board = current players PlayerBoard
    size = size of ship
    """

    # If it's the computer randomly choose placement options otherwise ask the user for theirs
    # if players_board.name == "comp":
    starting_point = comp_random_choice_of_coords()
    direction = DIRECTIONS[random.randint(0, 3)]
    # else:
    #     players_board.print_board()
    #     print(f"Place ship of size {size}")
    #     starting_point = input(colored("""Choose starting point of ship (e.g. 6f):\n""", "green"))
    #     direction = input(colored("""Choose direction of the ship (e.g. UP, DOWN, LEFT, or RIGHT):\n""", "green"))
    place_ship(players_board, starting_point, direction, size)


def convert_coords(coords):
    """
    Converts the number and letter given from the user into usable ints
    coords = a string containing coordinates on the board (e.g. "5d")
    """
    x_and_y = list(coords)
    x_coords = int(x_and_y[0])
    y_coords = 9 - (ord((x_and_y[1]).lower()) - 97)

    return x_coords, y_coords


def attack(players_board):
    """
    Attacks the opponents board
    players_board = current players PlayerBoard
    attack_coords = a string containing coordinates on the board (e.g. "5d")
    """
    if players_board.name == "comp":
        attack_coords = input(colored("Choose attach coords (e.g. 3e, 7f):\n", "green"))
    else:
        attack_coords = comp_random_choice_of_coords()

    x_coords, y_coords = convert_coords(attack_coords)
    target = players_board.board[y_coords][x_coords]

    # Check if its a hit ("x"), a miss ("o"), or if player has already attacked there
    if target == players_board.symbol:
        players_board.board[y_coords][x_coords] = "o"
    elif target == SHIP_CHARACTER:
        players_board.board[y_coords][x_coords] = "X"
        players_board.hits += 1
    else:
        print(colored("Sorry you've already attacked there", "red"))
        attack(players_board)

def menu():
    """
    Opening screen to the game
    """
    print("""
___  ____ ___ ___ _    ____ ____ _  _ _ ___  ____ 
|__] |__|  |   |  |    |___ [__  |__| | |__] [__  
|__] |  |  |   |  |___ |___ ___] |  | | |    ___] 
                                                  
""")
    while True:
        try:
            instruction = input(colored("Enter p to play or i for instructions:\n", "green")).upper()
            if instruction == "I":
                print(colored("""
    1. Enter the name you want to show on the leaderboard. You
        can use any characters you want
    2. Place your ships on the board:
        - You will be told the size of the ship you have to place 
        (there are 5 in total).
        - You will asked for a starting point this is a point on the 
        board that the ship starts at. You select this point with a
        number (0 - 9) and a letter (a - j), which represent the x 
        and the y axis respectively.
        - You will then be asked for a direction to place your your
        ship (e.g. "up", "down", "left", "right").
        - The ship will start at the starting point and will take up
        the size of the ship in direction input.
    3. Attack the computers side of the board. You can attack the 
        computer by using the coordinates similar to placing your
        ships. An x represents a hit and an o represents a miss.
    4. The game is won when a player get 17 hits on their opponents 
        board\n""", "yellow"))

            elif instruction == "P":
                break
            else:
                raise ValueError()
        except (AttributeError, ValueError):
            print(colored("Please type a proper command", "red"))

    # User pressed on p
    main()

def main():
    """
    Main function ran on execution of file
    """
    # Get username and create PlayerBoards for both player and computer
    name = input(colored("Please give your username:\n", "green"))
    if name == "comp":
        print(colored("That's the computers name sorry you'll have to pick another one", "red"))
        main()
    player = PlayerBoard("~", name)
    computer = PlayerBoard(" ")
    

    # Place the ships on the board
    for size in ship_sizes:
        choose_placement_of_ship(player, size)
        choose_placement_of_ship(computer, size)


    computer.print_board()
    player.print_board()

    # Set current player (may randomize this)
    current_player = player

    # While there are still ships (or parts of ships) to attack continue the attack back and forth
    while((player.hits < sum(ship_sizes)) and (computer.hits < sum(ship_sizes))):

        if current_player.name == "comp":
            attack(player)
            player.print_board()
            current_player = player

        else:
            
            attack(computer)
            computer.print_board()
            current_player = computer

    # Announce if the player wins or loses
    if current_player.name != "comp":
        print(colored("You lose", "red"))

    else:
        print(colored("Congrats!!", "green"))

menu()

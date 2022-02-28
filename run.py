import random

# Constant variables for choosing coords on the board (LETTERS) and 
# choosing a direction for placing a ship (DIRECTIONS)
LETTERS = ["j", "i", "h", "g", "f", "e", "d", "c", "b", "a"]
DIRECTIONS = ["up", "down", "right", "left"]


class PlayerBoard:
    """
    A class that creates a players side of the board and holds
    it's ships, hits, symbol, and name
    symbol = a single character string that fills out the side of the board
    name = a string that's comp by default
    """
    # Create player board, set name, symbol and hits
    def __init__(self, symbol, name="comp"):
        self.board = [[symbol] * 10,
                      [symbol] * 10,
                      [symbol] * 10,
                      [symbol] * 10,
                      [symbol] * 10,
                      [symbol] * 10,
                      [symbol] * 10,
                      [symbol] * 10,
                      [symbol] * 10,
                      [symbol] * 10]
        self.name = name
        self.symbol = symbol
        self.hits = 0


    def print_board(self):
        """
        print the players board to the terminal with letters
        on the y axis and numbers on the x axis
        """
        if self.name == "comp":
            whole_board = [[], [], [], [], [], [], [], [], [], []]
            for x in range(len(self.board)):
                for y in range(len(self.board)):
                    print(self.board[x][y], x, y)
                    if self.board[x][y] == '#':
                        whole_board[x].append(' ')
                    else:
                        whole_board[x].append(self.board[x][y])
        else:
            whole_board = self.board
        
        for line_num, line in enumerate(whole_board):
            # Prints the top line of the board
            if line_num == 0:
                print('    ________________________________')
                print('   |                                |')
                print(LETTERS[line_num] + "  " + "|  " +
                      '  '.join(line) + "  |")
                print('   |                                |')
            # Prints the bottom line of the board
            elif line_num == 9:
                print(LETTERS[line_num] + "  " + "|  " +
                      '  '.join(line) + "  |")
                print('   |________________________________|')
                print("      0  1  2  3  4  5  6  7  8  9")
            # Prints the lines between
            else:
                print(LETTERS[line_num] + "  " + "|  " +
                      '  '.join(line) + "  |")
                print('   |                                |')


def place_ship(players_board, starting_point, direction, size):
    """
    Function takes a Board, a starting point on that Board, a direction
    and size of a ship and places it on the Board
    players_board = the current players PlayerBoard
    starting_point = a sting containing coords to place the ship (e.g. "7j")
    direction = the direction of the ship should go in (e.g. "up", "down", "left", "right")
    size = size of the ship being placed
    """

    # Character that represents the ship
    SHIP = "#"
    # the starting point converted to integers
    x_coords, y_coords = convert_coords(starting_point)
    # the direction string converted to upper case
    direction_upper = direction.upper()
    # empty list used to check if a player has already placed a ship there
    spaces = []

    # BELOW NEEDS REFACTORING 
    # Placing a ship in the up direction
    if direction_upper == "UP":
        # If the ship runs off the board try again
        if y_coords - (size - 1) < 0:
            if players_board.name != "comp":
                print("ship won't fit on board try again")
            choose_placement_of_ship(players_board, size)
            return
        # Check to see if there is a ship already in the way
        for y_up in range(y_coords - (size - 1), y_coords + 1):
            space = players_board.board[y_up][x_coords]
            if space != players_board.symbol:
                if players_board.name != "comp":
                    print("You already have a ship there try again")
                choose_placement_of_ship(players_board, size)
                spaces = []
                break
            spaces.append([y_up, x_coords])
        # If it'll fit and no ships in the way place the ship
        for coords in spaces:
            players_board.board[coords[0]][coords[1]] = SHIP

    # Placing a ship in the down direction
    elif direction_upper == "DOWN":
        # If the ship runs off the board try again
        if y_coords + size > 9:
            if players_board.name != "comp":
                print("ship won't fit on board try again")
            choose_placement_of_ship(players_board, size)
            return
        # Check to see if there is a ship already in the way
        for y_down in range(y_coords, y_coords + size):
            space = players_board.board[y_down][x_coords]

            if space != players_board.symbol:
                if players_board.name != "comp":
                    print("You already have a ship there try again")
                choose_placement_of_ship(players_board, size)
                spaces = []
                break
            spaces.append([y_down, x_coords])
        # If it'll fit and no ships in the way place the ship
        for coords in spaces:
            players_board.board[coords[0]][coords[1]] = SHIP

    # Placing a ship in the right direction
    elif direction_upper == "RIGHT":
        # If the ship runs off the board try again
        if x_coords + size > 9:
            if players_board.name != "comp":
                print("ship won't fit on board try again")
            choose_placement_of_ship(players_board, size)
            return
        # Check to see if there is a ship already in the way
        for x_right in range(x_coords, x_coords + size):
            space = players_board.board[y_coords][x_right]
            if space != players_board.symbol:
                if players_board.name != "comp":
                    print("You already have a ship there try again")
                choose_placement_of_ship(players_board, size)
                spaces = []
                break
            spaces.append([y_coords, x_right])
        # If it'll fit and no ships in the way place the ship
        for coords in spaces:
            players_board.board[coords[0]][coords[1]] = SHIP

    # Placing a ship in the left direction
    elif direction_upper == "LEFT":
        # If the ship runs off the board try again
        if x_coords - (size - 1) < 0:
            if players_board.name != "comp":
                print("ship won't fit on board try again")
            choose_placement_of_ship(players_board, size)
            return
        # Check to see if there is a ship already in the way
        for x_left in range(x_coords - (size - 1), x_coords + 1):
            space = players_board.board[y_coords][x_left]
            if space != players_board.symbol:
                if players_board.name != "comp":
                    print("You already have a ship there try again")
                choose_placement_of_ship(players_board, size)
                spaces = []
                break
            spaces.append([y_coords, x_left])
        # If it'll fit and no ships in the way place the ship
        for coords in spaces:
            players_board.board[coords[0]][coords[1]] = SHIP


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
    if players_board.name == "comp":
        starting_point = comp_random_choice_of_coords()
        direction = DIRECTIONS[random.randint(0, 3)]
    else:
        starting_point = input("""Choose starting point of ship (e.g. 6f):\n""")
        direction = input("""Choose direction of the ship (e.g. UP, DOWN, LEFT, or RIGHT):\n""")
    place_ship(players_board, starting_point, direction, size)


def convert_coords(coords):
    """
    Converts the number and letter given from the user into usable ints
    coords = a string containing coordinates on the board (e.g. "5d")
    """
    x_and_y = list(coords)
    x_coords = int(x_and_y[0])
    y_coords = 9 - (ord(x_and_y[1]) - 97)

    return x_coords, y_coords


def attack(players_board, attack_coords):
    """
    Attacks the opponents board
    players_board = current players PlayerBoard
    attack_coords = a string containing coordinates on the board (e.g. "5d")
    """
    x_coords, y_coords = convert_coords(attack_coords)
    target = players_board.board[y_coords][x_coords]

    # Check if its a hit ("x"), a miss ("o"), or if player has already attacked there
    if target == players_board.symbol:
        players_board.board[y_coords][x_coords] = "o"
    elif target == "#":
        players_board.board[y_coords][x_coords] = "X"
        players_board.hits += 1
    else:
        print("Sorry you've already attacked there")


def menu():
    """
    Opening screen to the game
    """
    print("""
___  ____ ___ ___ _    ____ ____ _  _ _ ___  ____ 
|__] |__|  |   |  |    |___ [__  |__| | |__] [__  
|__] |  |  |   |  |___ |___ ___] |  | | |    ___] 
                                                  
""")
    instruction = input("Enter p to play or i for instructions:\n").upper()
    if instruction == "I":
        print("""1. Enter the name you want to show on the leaderboard. You
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
                    board""")
        input("Press enter to go back to the main menu.\n")
        menu()
    elif instruction == "P":
        main()
    else:
        print("Please type a proper command")
        menu()

def main():
    """
    Main function ran on execution of file
    """
    # Get username and create PlayerBoards for both player and computer
    name = input("Please give your username:\n")
    player = PlayerBoard("~", name)
    computer = PlayerBoard(" ")
    ship_sizes = [2, 3, 3, 4, 5]

    # Place the ships on the board
    for size in ship_sizes:
        choose_placement_of_ship(player, size)
        player.print_board()
        choose_placement_of_ship(computer, size)

    computer.print_board()
    player.print_board()

    # Set current player (may randomize this)
    current_player = player

    # While there are still ships (or parts of ships) to attack continue the attack back and forth
    while((player.hits < 24) and (computer.hits < 24)):

        if current_player.name == "comp":
            attack(player, comp_random_choice_of_coords())
            player.print_board()
            current_player = player

        else:
            attack_coords = input("Choose attach coords (e.g. 3e, 7f):\n")
            attack(computer, attack_coords)
            computer.print_board()
            current_player = computer

    # Announce if the player wins or loses
    if current_player.name != "comp":
        print("You lose")

    else:
        print("Congrats!!")

menu()

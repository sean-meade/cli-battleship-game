import random
# Write your code to expect a terminal of 80 characters wide and 24 rows high
LETTERS = ["j", "i", "h", "g", "f", "e", "d", "c", "b", "a"]
DIRECTIONS = ["up", "down", "right", "left"]


class PlayerBoard:
    """
    A class that creates a players side of the board and holds
    it's ships, hits and misses
    """
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
        """ print the players board to the screen """

        for line in range(len(self.board)):
            if line == 0:
                print('    ________________________________')
                print('   |                                |')
                print(LETTERS[line] + "  " + "|  " +
                      '  '.join(self.board[line]) + "  |")
                print('   |                                |')
            elif line == 9:
                print(LETTERS[line] + "  " + "|  " +
                      '  '.join(self.board[line]) + "  |")
                print('   |________________________________|')
                print("      0  1  2  3  4  5  6  7  8  9")
            else:
                print(LETTERS[line] + "  " + "|  " +
                      '  '.join(self.board[line]) + "  |")
                print('   |                                |')


def place_ship(players_board, starting_point, direction, size):
    """
    Function takes a Board, a starting point on that Board, a direction
    and size of a ship and places it on the Board
    """
    SHIP = "#"
    x_coords, y_coords = convert_coords(starting_point)

    direction_upper = direction.upper()
    spaces = []
    if direction_upper == "UP":
        if y_coords - (size - 1) < 0:
            if players_board.name != "comp":
                print("ship won't fit on board try again")
            choose_placement_of_ship(players_board, size)
            return
        for y_up in range(y_coords - (size - 1), y_coords + 1):
            # print("here 1:", players_board.name, y_up, x_coords)
            space = players_board.board[y_up][x_coords]
            if space != players_board.symbol:
                if players_board.name != "comp":
                    print("You already have a ship there try again")
                choose_placement_of_ship(players_board, size)
                spaces = []
                break
            spaces.append([y_up, x_coords])
        for coords in spaces:
            players_board.board[coords[0]][coords[1]] = SHIP

    elif direction_upper == "DOWN":
        if y_coords + size > 9:
            if players_board.name != "comp":
                print("ship won't fit on board try again")
            choose_placement_of_ship(players_board, size)
            return
        for y_down in range(y_coords, y_coords + size):
            # print("here 2:", players_board.name, y_down, x_coords)
            space = players_board.board[y_down][x_coords]

            if space != players_board.symbol:
                if players_board.name != "comp":
                    print("You already have a ship there try again")
                choose_placement_of_ship(players_board, size)
                spaces = []
                break
            spaces.append([y_down, x_coords])
        for coords in spaces:
            players_board.board[coords[0]][coords[1]] = SHIP

    elif direction_upper == "RIGHT":
        if x_coords + size > 9:
            if players_board.name != "comp":
                print("ship won't fit on board try again")
            choose_placement_of_ship(players_board, size)
            return
        for x_right in range(x_coords, x_coords + size):
            # print("here 3:", players_board.name, y_coords, x_right)
            space = players_board.board[y_coords][x_right]
            if space != players_board.symbol:
                if players_board.name != "comp":
                    print("You already have a ship there try again")
                choose_placement_of_ship(players_board, size)
                spaces = []
                break
            spaces.append([y_coords, x_right])
        for coords in spaces:
            players_board.board[coords[0]][coords[1]] = SHIP

    elif direction_upper == "LEFT":
        if x_coords - (size - 1) < 0:
            if players_board.name != "comp":
                print("ship won't fit on board try again")
            choose_placement_of_ship(players_board, size)
            return
        for x_left in range(x_coords - (size - 1), x_coords + 1):
            # print("here 4:", players_board.name, y_coords, x_left)
            space = players_board.board[y_coords][x_left]
            if space != players_board.symbol:
                if players_board.name != "comp":
                    print("You already have a ship there try again")
                choose_placement_of_ship(players_board, size)
                spaces = []
                break
            spaces.append([y_coords, x_left])
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
    """

    if players_board.name == "comp":
        # Choose randomly
        starting_point = comp_random_choice_of_coords()
        direction = DIRECTIONS[random.randint(0, 3)]
    # else:
        starting_point = input("""
                               Choose starting point of ship (e.g. 6f):\n
                               """)
        direction = input("""
                          Choose direction of the ship
                          (e.g. UP, DOWN, LEFT, or RIGHT):\n
                          """)
    place_ship(players_board, starting_point, direction, size)


def convert_coords(coords):
    """
    Converts the number and letter given from the user into usable ints
    """
    x_and_y = list(coords)
    x_coords = int(x_and_y[0])
    y_coords = 9 - (ord(x_and_y[1]) - 97)
    # print(x_coords, y_coords)
    return x_coords, y_coords


def attack(players_board, attack_coords):
    """
    Attacks the opponents board
    """
    x_coords, y_coords = convert_coords(attack_coords)

    target = players_board.board[y_coords][x_coords]
    if target == players_board.symbol:
        players_board.board[y_coords][x_coords] = "o"
    elif target == "#":
        players_board.board[y_coords][x_coords] = "X"
        players_board.hits += 1
    else:
        print("Sorry you've already attacked there")


def main():
    """
    Main function ran on execution of file
    """
    name = input("Please give your username:\n")
    player = PlayerBoard("~", name)
    computer = PlayerBoard(" ")
    ship_sizes = [3, 3, 4, 4, 5, 5]

    for size in ship_sizes:
        choose_placement_of_ship(player, size)
        player.print_board()
        choose_placement_of_ship(computer, size)

    computer.print_board()
    player.print_board()

    current_player = player
    print("player name", current_player.name)
    while((player.hits < 24) and (computer.hits < 24)):

        if current_player.name == "comp":
            attack(player, comp_random_choice_of_coords())
            player.print_board()
            print(player.hits)
            current_player = player

        else:
            attack_coords = input("Choose attach coords (e.g. 3e, 7f):\n")
            attack(computer, attack_coords)
            computer.print_board()
            print(computer.hits)
            current_player = computer

    if current_player.name != "comp":
        print("You lose")

    else:
        print("Congrats!!")

main()

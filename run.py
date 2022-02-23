# Write your code to expect a terminal of 80 characters wide and 24 rows high
class PlayerBoard:
    """
    A class that creates a players side of the board and holds it's ships, hits and misses
    """
    def __init__(self, symbol, name = "comp"):
        self.board = [[symbol] * 10,
                      [symbol] * 10,
                      [symbol] * 10,
                      [symbol] * 10,
                      [symbol] * 10,
                      [symbol] * 10,
                      [symbol] * 10,
                      [symbol] * 10,
                      [symbol] * 10,
                      [symbol] * 10,]
                    #   [[symbol] * 10] * 10
        self.name = name
        self.symbol = symbol

    def print_board(self):
        """ print the players board to the screen """
        letters = ["j", "i", "h", "g", "f", "e", "d", "c", "b", "a"]
        for line in range(len(self.board)):
            if line == 0:
                print('    ________________________________')
                print('   |                                |')
                print(letters[line] + "  " + "|  " + '  '.join(self.board[line]) + "  |")
                print('   |                                |')
            elif line == 9:
                print(letters[line] + "  " + "|  " + '  '.join(self.board[line]) + "  |")
                print('   |________________________________|')
                print("      0  1  2  3  4  5  6  7  8  9")
            else:
                print(letters[line] + "  " + "|  " + '  '.join(self.board[line]) + "  |")
                print('   |                                |')


def place_ship(players_board, starting_point, direction, size):
    """
    Function takes a Board, a starting point on that Board, a direction
    and size of a ship and places it on the Board
    """
    SHIP = "#"

    x_coords, y_coords = convert_coords(starting_point)

    # x_and_y = list(starting_point)

    # x_coords = int(x_and_y[0])
    # y_coords = 9 - (ord(x_and_y[1]) - 97)
    # print("x", x_coords, "y", y_coords, "x and y", x_and_y)

    direction_upper = direction.upper()
    spaces = []
    if direction_upper == "UP":
        if y_coords - (size - 1) < 0:
            print("ship won't fit on board try again")
            choose_placement_of_ship(players_board, size)
            
        for y_up in range(y_coords - (size - 1), y_coords + 1):
            space = players_board.board[y_up][x_coords]
            if space != players_board.symbol:
                print("You already have a ship there try again")
                players_board.print_board()
                choose_placement_of_ship(players_board, size)
                spaces = []
                break
            spaces.append([y_up, x_coords])
        for coords in spaces:
            players_board.board[coords[0]][coords[1]] = SHIP

    elif direction_upper == "DOWN":
        if y_coords + size > 9:
            print("ship won't fit on board try again")
            choose_placement_of_ship(players_board, size)
        for y_down in range(y_coords, y_coords + size):
            space = players_board.board[y_down][x_coords]
            if space != players_board.symbol:
                print("You already have a ship there try again")
                players_board.print_board()
                choose_placement_of_ship(players_board, size)
                spaces = []
                break
            spaces.append([y_down, x_coords])
        for coords in spaces:
            players_board.board[coords[0]][coords[1]] = SHIP

    elif direction_upper == "RIGHT":
        if x_coords + size > 9:
            print("ship won't fit on board try again")
            choose_placement_of_ship(players_board, size)
        for x_right in range(x_coords, x_coords + size):
            space = players_board.board[y_coords][x_right]
            if space != players_board.symbol:
                print("You already have a ship there try again")
                players_board.print_board()
                choose_placement_of_ship(players_board, size)
                spaces = []
                break
            spaces.append([y_coords, x_right])
        for coords in spaces:
            players_board.board[coords[0]][coords[1]] = SHIP

    elif direction_upper == "LEFT":
        if x_coords  - (size - 1) < 0:
            print("ship won't fit on board try again")
            choose_placement_of_ship(players_board, size)
        for x_left in range(x_coords  - (size - 1), x_coords + 1):
            space = players_board.board[y_coords][x_left]
            if space != players_board.symbol:
                print("You already have a ship there try again")
                players_board.print_board()
                choose_placement_of_ship(players_board, size)
                spaces = []
                break
            spaces.append([y_coords, x_left])
        for coords in spaces:
            players_board.board[coords[0]][coords[1]] = SHIP

    players_board.print_board()

def choose_placement_of_ship(players_board, size):
    """
    Function that gets users placement options
    """
    starting_point = input("Choose starting point of ship (e.g. 6f, 7y, 3i):\n")
    direction = input("Choose direction of the ship (e.g. UP, DOWN, LEFT, or RIGHT):\n")
    place_ship(players_board, starting_point, direction, size)

def convert_coords(starting_point):
    """
    Converts the number and letter given from the user into usable ints
    """
    x_and_y = list(starting_point)

    x_coords = int(x_and_y[0])
    y_coords = 9 - (ord(x_and_y[1]) - 97)

    return x_coords, y_coords

def main():
    """
    Main function ran on execution of file
    """
    # name = input("Please give your username:\n")
    player_one = PlayerBoard("~", "sean")

    player_one.print_board()
    ship_sizes = [3, 4, 5]

    for size in ship_sizes:
        choose_placement_of_ship(player_one, size)

    # computer = PlayerBoard("O")

    # computer.print_board()

main()

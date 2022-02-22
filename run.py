# Write your code to expect a terminal of 80 characters wide and 24 rows high
class PlayerBoard:
    """
    A class that creates a players side of the board and holds it's ships, hits and misses
    """
    
    def __init__(self, player, name = "comp"):
        self.board = [["w"] * 10,
                      ["g"] * 10,
                      ["h"] * 10,
                      ["j"] * 10,
                      ["k"] * 10,
                      ["l"] * 10,
                      ["a"] * 10,
                      ["s"] * 10,
                      ["d"] * 10,
                      ["r"] * 10,]
        # [[player] * 10] * 10
        self.name = name

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
    Function takes a Board, a starting point on that Board, a direction and size of a ship and places it on the Board
    """
    SHIP = "#"

    x_and_y = list(starting_point)

    x_direction = int(x_and_y[0])
    y_direction = 9 - (ord(x_and_y[1]) - 97)
    # print("x", x_direction, "y", y_direction, "x and y", x_and_y)

    direction_upper = direction.upper()

    match direction_upper:
        case "UP":
            for y_up in range(y_direction - (size - 1), y_direction + 1):
                players_board.board[y_up][x_direction] = SHIP

        case "DOWN":
            for y_down in range(y_direction, y_direction + size):
                players_board.board[y_down][x_direction] = SHIP

        case "RIGHT":
            for x_right in range(x_direction, x_direction + size):
                players_board.board[y_direction][x_right] = SHIP

        case "LEFT":
            for x_left in range(x_direction  - (size - 1), x_direction + 1):
                players_board.board[y_direction][x_left] = SHIP

    players_board.print_board()


def main():
    """
    Main function ran on execution of file
    """
    name = input("Please give your username:\n")
    player_one = PlayerBoard("~", name)
    starting_point = input("Choose starting point of ship (e.g. 6f, 7y, 3i):\n")
    direction = input("Choose direction of the ship (e.g. UP, DOWN, LEFT, or RIGHT):\n")
    place_ship(player_one, starting_point, direction, 2)

    

    # computer = PlayerBoard("O")

    # computer.print_board()

main()
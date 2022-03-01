# Constant variables for choosing coords on the board (LETTERS) and 
# choosing a direction for placing a ship (DIRECTIONS)
LETTERS = ["j", "i", "h", "g", "f", "e", "d", "c", "b", "a"]
DIRECTIONS = ["up", "down", "right", "left"]

ROWS = COLUMNS = 10
SHIP_CHARACTER = "#"


class PlayerBoard:
    """
    A class that creates a players side of the board and holds
    it's ships, hits, symbol, and name
    symbol = a single character string that fills out the side of the board
    name = a string that's comp by default
    """
    # Create player board, set name, symbol and hits
    def __init__(self, symbol, name="comp"):
        self.board = [[symbol] * COLUMNS for _ in range(ROWS)]
        self.name = name
        self.symbol = symbol
        self.hits = 0


    def print_board(self):
        """
        print the players board to the terminal with letters
        on the y axis and numbers on the x axis
        """
        if self.name == "comp":
            whole_board = [[] * COLUMNS for _ in range(ROWS)]
            for x in range(len(self.board)):
                for y in range(len(self.board)):
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
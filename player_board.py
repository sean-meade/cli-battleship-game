# Constant variables for choosing coords on the board (LETTERS) and
# choosing a direction for placing a ship (DIRECTIONS)

LETTERS = ["j", "i", "h", "g", "f", "e", "d", "c", "b", "a"]
DIRECTIONS = ["up", "down", "right", "left"]
NUMS = [str(x) for x in list(range(0, 10))]

ROWS = COLUMNS = 10
SHIP_CHARACTER = "#"

COMP = "computer"

line_spacer = f"\t|{' '*32}|"
bottom_of_board = f"\t|{'_'*32}|"
top_of_board = f"\t {'_'*32}"


class PlayerBoard:
    """
    A class that creates a players side of the board and holds
    it's ships, hits, symbol, and name
    symbol = a single character string that fills out the side of the board
    name = a string that's comp by default
    """
    # Create player board, set name, symbol and hits
    def __init__(self, symbol, name=COMP):
        self.board = [[symbol] * COLUMNS for _ in range(ROWS)]
        self.name = name
        self.symbol = symbol
        self.hits = 0

    def print_board(self):
        """
        print the players board to the terminal with letters
        on the y axis and numbers on the x axis
        """

        # Hides the computers ships when printed to the terminal
        if self.name == COMP:
            # create list to hold hidden board while printing
            whole_board = [[] * COLUMNS for _ in range(ROWS)]
            # if there is a ship symbol on the comp board replace
            # it with a blank space (" ") when printing
            for x in range(len(self.board)):
                for y in range(len(self.board)):
                    if self.board[x][y] == '#':
                        whole_board[x].append(' ')
                    else:
                        whole_board[x].append(self.board[x][y])
        else:
            whole_board = self.board

        # print the board to the screen
        for line_num, line in enumerate(whole_board):
            # Prints the top line of the board
            if line_num == 0:
                print(f"""{top_of_board}
{line_spacer}
     {LETTERS[line_num]}  |  {'  '.join(line)}  |
{line_spacer}""")
            # Prints the bottom line of the board
            elif line_num == 9:
                print(f"""     {LETTERS[line_num]}  |  {'  '.join(line)}  |
{bottom_of_board}
\t   {'  '.join(NUMS)}""")
            # Prints the lines between
            else:
                print(f"""     {LETTERS[line_num]}  |  {'  '.join(line)}  |
{line_spacer}""")

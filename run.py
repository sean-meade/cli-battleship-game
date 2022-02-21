# Write your code to expect a terminal of 80 characters wide and 24 rows high
class PlayerBoard:
    """
    A class that creates a players side of the board and holds it's ships, hits and misses
    """
    
    def __init__(self, player):
        self.board = [[player] * 10] * 10

    def print_board(self):
        """ print the players board to the screen """
        for line in range(len(self.board)):
            if line == 0:
                print(' ___________________')
                print("|" + ' '.join(self.board[line]) + "|")
            elif line == 9:
                print("|" + ' '.join(self.board[line]) + "|")
                print(' \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305 \u0305')
            else:
                print("|" + ' '.join(self.board[line]) + "|")

player_one = PlayerBoard("~")

player_one.print_board()

computer = PlayerBoard("o")

computer.print_board()
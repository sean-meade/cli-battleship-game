import gspread
from google.oauth2.service_account import Credentials
from termcolor import colored

# Set scope for google sheets
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

# Create credentials for the scope and create a 'client'
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

# Open the google sheet
SHEET = GSPREAD_CLIENT.open('leader-board')


def add_name_and_time_to_leaderboard(name, time, secs):
    """
    Adds a winner and their time to the google sheet

    name = string: name of player
    time = timedelta: time taken to win the game
    secs = time taken to win the game in seconds
    """
    # Add user and time to googlesheet
    leader_board = SHEET.worksheet('scores')
    leader_board.append_row([name, time, secs])


def print_top_players():
    """
    A function that prints the 3 players with the fastest time
    """
    # first reorders the google sheet by time
    SHEET.worksheet('scores').sort((3, 'asc'))
    # gets values in the google sheet
    leader_board = SHEET.worksheet('scores').get_all_values()

    # Tries to print the leaderboard and if it cant prints the statement:
    # 'No players have played yet'
    try:
        if leader_board[0]:
            # Leaderboard Heading
            print(" " * 15, "Leaderboard")
            # Titles
            print("{:5s} {:20s} {:30s}".format("", "Name:", "Time:\n"))
            # Pick top 3 players and display
            for player in range(3):
                player_n = leader_board[player]
                print(
                    colored(
                        "{:20s} {:30s}".format(" " * 5 + player_n[0],
                                               player_n[1] + "\n"), "blue"))
        else:
            raise IndexError()
    # Otherwise tell the user no players to show
    except IndexError:
        print(" " * 15, "No players to show")

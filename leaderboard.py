import gspread
from datetime import timedelta
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('leader-board')

# data = SHEET.worksheet('scores').get_all_values()

def add_name_and_time_to_leaderboard(name, time, secs):
    leader_board =  SHEET.worksheet('scores')
    leader_board.append_row([name, time, secs])

def print_top_players():
    SHEET.worksheet('scores').sort((3, 'asc'))
    leader_board =  SHEET.worksheet('scores').get_all_values()
    print("Name:", "Time")
    for player in range(3):
        print(leader_board[player][0], leader_board[player][1])

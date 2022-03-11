from datetime import datetime
from leaderboard import add_name_and_time_to_leaderboard, print_top_players
from termcolor import colored
from player_board import PlayerBoard, COMP
from place_ship import choose_placement_of_ship
from utilis import attack, clear_console
from time import sleep

ship_sizes = [2, 3, 3, 4, 5]


def menu():
    """
    Opening screen to the game
    """
    clear_console()
    print(
        """
___  ____ ___ ___ _    ____ ____ _  _ _ ___  ____
|__] |__|  |   |  |    |___ [__  |__| | |__] [__
|__] |  |  |   |  |___ |___ ___] |  | | |    ___]\n
"""
    )
    print_top_players()

    while True:
        try:
            # ask the user for an input
            instruction = input(
                colored(
                    "Type p to play or i for instructions and press Enter:\n", "green"
                )
            ).upper()
            # if its i give the instructions
            if instruction == "I":
                print(
                    colored(
                        """
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
        board\n""",
                        "yellow",
                    )
                )
            # if its p break the while loop and start the game
            elif instruction == "P":
                break
            # otherwise raise an error
            else:
                raise ValueError()
        # if there is an error prompt the user to use a proper command
        except (AttributeError, ValueError):
            print(
                colored(
                    "Please type p to play or i for instructions and press Enter", "red"
                )
            )
    # User pressed on p
    clear_console()


def main():
    """
    Main function ran after the player has chosen to play
    """
    # Get username and create PlayerBoards for both player and computer
    name = input(colored("Please give your username:\n", "green"))
    # check to see if the user used the same name as computer and retry
    if name == COMP:
        print(
            colored(
                "That's the computers name sorry you'll have to pick another one", "red"
            )
        )
        main()
        return
    # create boards for player and computer
    player = PlayerBoard("~", name)
    computer = PlayerBoard(" ")

    clear_console()
    # Place the ships on the board
    for size in ship_sizes:
        choose_placement_of_ship(player, size)
        choose_placement_of_ship(computer, size)
        clear_console()
    # Set current player (may randomize this)
    current_player = player

    # Get the time of when the game starts
    start_time = datetime.now()
    # While there are still ships (or parts of ships) to
    # attack continue the attack back and forth
    while (player.hits < sum(ship_sizes)) and (computer.hits < sum(ship_sizes)):

        # The user and computer attack each other, print the
        # board of opponent and then change to next player
        if current_player.name == COMP:
            attack(player)
            current_player = player
        else:
            attack(computer)
            sleep(2)
            current_player = computer
    # get the time when the game ends
    end_time = datetime.now()

    # Announce if the player wins or loses
    if current_player.name != COMP:
        print(colored("You lose...", "red"))
    # If the player wins get the time taken to win and update
    # google sheets with the name and time
    else:
        time_taken = end_time - start_time
        complete_time = str(time_taken)
        time_in_seconds = time_taken.total_seconds()
        add_name_and_time_to_leaderboard(name, complete_time, time_in_seconds)
        print(
            colored("\tCongratulations you won!!\nYour time has been recorded", "green")
        )
    input("Press any key to start again.")


while True:
    menu()
    main()

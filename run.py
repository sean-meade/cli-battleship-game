from datetime import datetime
from leaderboard import add_name_and_time_to_leaderboard, print_top_players
from termcolor import colored
from player_board import PlayerBoard
from place_ship import choose_placement_of_ship
from utilis import attack

ship_sizes: list = [2, 3, 3, 4, 5]


def menu():
    """
    Opening screen to the game
    """
    print("""
___  ____ ___ ___ _    ____ ____ _  _ _ ___  ____ 
|__] |__|  |   |  |    |___ [__  |__| | |__] [__  
|__] |  |  |   |  |___ |___ ___] |  | | |    ___] 
                                                  
""")
    print_top_players()
    while True:
        try:
            instruction = input(colored("Enter p to play or i for instructions:\n", "green")).upper()
            if instruction == "I":
                print(colored("""
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
        board\n""", "yellow"))

            elif instruction == "P":
                break
            else:
                raise ValueError()
        except (AttributeError, ValueError):
            print(colored("Please type a proper command", "red"))

    # User pressed on p
    main()

def main():
    """
    Main function ran on execution of file
    """
    # Get username and create PlayerBoards for both player and computer
    name = input(colored("Please give your username:\n", "green"))
    if name == "comp":
        print(colored("That's the computers name sorry you'll have to pick another one", "red"))
        main()
    player = PlayerBoard("~", name)
    computer = PlayerBoard(" ")
    

    # Place the ships on the board
    for size in ship_sizes:
        choose_placement_of_ship(player, size)
        choose_placement_of_ship(computer, size)

    player.print_board()
    # Set current player (may randomize this)
    current_player = player

    start_time = datetime.now()
    # While there are still ships (or parts of ships) to attack continue the attack back and forth
    while((player.hits < sum(ship_sizes)) and (computer.hits < sum(ship_sizes))):

        if current_player.name == "comp":
            attack(player)
            player.print_board()
            current_player = player

        else:
            attack(computer)
            computer.print_board()
            current_player = computer

    end_time = datetime.now()

    # Announce if the player wins or loses
    if current_player.name != "comp":
        print(colored("You lose", "red"))

    else:
        time_taken = end_time - start_time
        complete_time = str(time_taken)
        time_in_seconds = time_taken.total_seconds()
        add_name_and_time_to_leaderboard(name, complete_time, time_in_seconds)
        print(colored("Congrats!!", "green"))

menu()

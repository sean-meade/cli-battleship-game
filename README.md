[Live site](https://battleship-31i4.onrender.com/)

# Battleship

![hosted site](docs/features/hosted-site.png)

## Table of contents
1. [Introduction](#introduction)
2. [How To play](#how-to-play)
3. [Features](#features)
    * [Existing Features](#existing-features)
    * [Future Features](#future-features)
4. [Data Model](#data-model)
5. [Testing](#testing)
    * [Solved Bugs](#solved-bugs)
    * [Validator testing](#validator-testing)
    * [Unfixed bugs](#unfixed-bugs)
5. [Deployment](#deployment)
6. [Credits](#credits)
    * [Content](#content)
    * [Acknowledgements](#acknowledgements)


## Introduction 

This is a command line version of the classic game battleships. The program allows the user to place their ships on their side of the board and then attack the computers ships on its board. The first to make 17 hits wins the game.

## How To Play

CLI Battleship is my take on the classic battleship game but played on the command line.

In this version, the player chooses a username and their board is created. The board has letters a to j in the y direction and number 0 to 9 in the x. A number followed by a letter make up a coordinate on the board.

It then prompts the player to place their ships on the board. There are 5 ships in total of sizes 2, 3, 3, 4, and 5. The player must choose a starting point which is done by giving coordinates a number and a letter (e.g. 3e), followed by the direction they would like to place the ship (i.e. up, down, left, and right).

Once all ships are placed the player will be prompted to make the first attack. This means you are attacking the computers board, which shows on the screen as blank. Using the same coordinate system as placing the ships you can attack (e.g. 8f). The computer has the same size ships as the player and places tem randomly.

The computer will make its move and will continue back and forth until one player has sunk all the other players ships.

If the user wins their username and time is added to the leader board and if they are in the top 3 they will show teh next time the opening screen is loaded.

## Features

### Existing features

1. Opening Screen

The opening screen shows the title, leader board, and asks if you want to play or get instructions. 

![Opening Screen](docs/features/1-opening-screen.png "Image showing the opening screen")

2. Instructions

The instruction screen gives the user instructions on how to play the game

![Instructions](docs/features/instructions.png "Image showing Input Username")

2. Input Username

After typing p and pressing enter the user is asked for their username

![Input Username](docs/features/2-username.png "Image showing Input Username field")

3. Player board

The player board is the visual representation of the board, showing ships (#) and ocean (~ for player and nothing for computer):

![Player board](docs/features/3-player-board.png "Image showing the Player board")

4. Placing a ship

The player is then asked to place 5 ships of lengths 2, 3, 3, 4, and 5 in that order. By first inputting coordinates and then a direction.

![Placing a ship](docs/features/4-place-ship.png "Image showing how to place a ship")

5. Attacking The Computer

Once all ships are placed the player is then asked to pick attack coordinates of the opponents board (e.g. 5c)

![Attacking The Computer](docs/features/6-attack-computer.png "Image showing how to attack the computer")

6. Player and Computer Missing

Each time there is a miss (hitting ocean character) the following prompts are shown for player and computer

- Player missing

![Player missing](docs/features/7-player-misses.png "Image showing Player missing")

- Computer missing

![Computer missing](docs/features/8-computer-misses.png "Image showing Computer missing")


7. Player and Computer Hitting

Each time there is a hit (hitting a ship character) the following prompts are shown for player and computer

- Player Hits

![Player Hits](docs/features/9-player-hits.png)

- Computer Hits

![Computer Hits](docs/features/10-computer-hits.png "Image showing Computer Hits")

8. Player or Computer Winning

The following shows the screen when a player wins and the computer wins respectively

- Player Wins

![Player Wins](docs/features/13-player-wins.png "Image showing Player Wins")

- Computer Wins

![Computer Wins](docs/features/12-computer-wins.png "Image showing Computer Wins")



### Future Features

Given more time to develop this project here are features I would have liked to implement:

1. Use N, S, E, W instead of up, down, left, right

I think this would have fit in a lot better with the theme of battleship. To implement this I would change the DIRECTIONS list to N, S, E, W and change where ever there are comparisons to mirror this change.

2. "You sunk my battleship!!"

I would have liked to add the feature where by when a whole ship is destroyed that there is a prompt to say so. I would do this by creating a list that contained lists that hold the position of the ships on the board. For example:

```
ship_placements = [['3a', '3b', '3c'], ['0h', '1h', '2h', '3h']]
```

Where each list item in ship_placement represents a ships placement on the board. Then each time an attack is made the the game will loop through this list to check if a ship has been sunk.

3. Smarter Computer

I would have also liked to implement a weighted system, where by the computer after making a hit will focus around that hit until a ship has been sunk.

I would have also like to have tracked the computers moves to allow the computer to make quicker moves as the game goes on.

4. Functions inside class

It might not be a feature but I would have liked to add the function for placing ships into the PlayerBoard class.

## Data Model

Two types of data models were used in this project. A PlayerBoard class and an Google sheet. 

The PlayerBoard class holds the board, the name associated with the board, the symbol used to fill the board when created. It also holds a function used to print the current state of the board, in the case of the computer it prints a blank board and only shows hits and misses.

The Google sheet could be seen as a relational database (albeit a very small one), or a visual representation of a csv file. Either way the Goggle sheet stores The username given at the start of the game and the time the user took to win the game.

## Testing

### Solved Bugs

Inputs:

For all input testing the following types of inputs were tested: Numeric, alphanumeric, a mix of both, special characters, and no input at all. The player can also use uppercase and lowercase for the proper inputs. For each input if anything except the correct input is entered the following prompts are shown to guide the player.

1. Choosing p or i at the opening screen:

![Play or Instructions](docs/testing/p_or_i_input.png "Play or Instructions")

2. Placing ship input

![Use correct coords when placing ship](docs/testing/placing_ship.png "Use correct coords when placing ship")

3. Attack Coordinates input

![Use correct coords when attacking](docs/testing/attack_coords.png "Use correct coords when attacking")

Functional

1. Ship wont fit on the board

If a player tries to place a ship where it will spill out over the board the following prompt is printed

![Ship Wont Fit On the Board](docs/testing/ship_wont_fit.png "Ship Wont Fit On the Board")

2. Ship already placed there

If a player tries to place a ship where a ship has already been placed the following prompt is printed

![Ship already placed there](docs/testing/ship_already_there.png "Ship already placed there")

3. Already attacked these coordinates

If a player tries to attack coordinates they have already attacked the following prompt is printed

![Already attacked these coordinates](docs/testing/already_attacked_here.png "Already attacked these coordinates")

### Unfixed bugs 

1. First line of the board is printing above board

For some reason the first line of the board is printing above the board every time it's printed, as shown below:

![First Line of board reprinting](docs/bugs/print_bug.png)

I have tried 3 different ways of writing the clearing function and also different placement of the clearing function throughout the flow of the game. Nothing has seemed to stop this bug. I have also failed to find the error in my logic, if that is what is causing this bug.

2. Computer takes longer to attack

The computer currently has no way of known what moves it has made before. The less spaces left to attack the longer it can take the computer to choose valid coordinates. See Future Features section for my intended fix of this bug.

### Validator testing

All Python files have been ran through a PEP8 validator at pep8online.com - The following files meet all PEP8 requirements according to this validator:

- leaderboard.py
- player_board.py
- utilis.py

Validator result for above
![Validator result for above](docs/validating/player_board_val.png "Validator result for above")

The following Python files have 'line too long' on one or more line.

- place_ship.py
- run.py

Here I wish to explain my reasoning behind leaving the these as they are.

The majority of errors are due to a print statement going 2 or 3 characters over. This is even after setting the print, colour, and text on different line. As this does not impede the understanding of the code I have left them as is. Below is an example of what I mean:

![Line too long by 2 or 3 chars](docs/validating/run_line_too_long_print.png "Line too long by 2 or 3 chars")

One print statement at line 30 in place_ship.py is 24 characters too long for PEP8. This is even after setting the print, colour, and text on different line. I have used the same reasoning as above in regards to this line. Below is an image of said line:

![Line too long PEP 8 validator](docs/validating/place_ship_line_too_long_print.png "Line too long PEP 8 validator")

The last two lines that don't meet PEP8 are 112 in run.py (a while loop):

![While loop a character too long](docs/validating/run_line_too_long_while.png "While loop a character too long")

and line 40 in place_ship.py (an if statement):

![if statement 1 character too long](docs/validating/place_ship_line_too_long_if.png "if statement 1 character too long")

Both are one character too long and after trying to reduce the size of both I have decided to leave as is for the sake of one character.

*Here are the results from the validator for these files*:

**place_ship.py:**

![place_ship.py PEP8 validator result](docs/validating/place_ship_val.png "place_ship.py PEP8 validator result")

**run.py**

![run.py PEP8 validator result](docs/validating/run_val.png "run.py PEP8 validator result")


## Deployment

This program was deployed to Heroku, following the below steps:

1) Push most up-to-date code to Github

2) Create a list of requirements by typing the following into the terminal:
pip3 freeze > requirements.txt

3) Push the requirements to Github

4) Logon to Heroku

5) Select create new app 

6) Add app name 

7) Add app region

8) Select 'Create app'

9) Open up the Settings tab, on the top ribbon

10) In 'Config Vars' select 'Reveal Config Vars'

11) Add 'PORT' as a key and '8000' as a value

12) In 'Buildpacks' select 'Add buildpack' and choose python. Then, repeat for nodejs (order is important; python first followed by nodejs) 

13) Navigate to 'Deploy' on the top ribbon

14) In 'Deployment method', select 'Github', once clicked it should say 'connected'

15) Enter a repository in Github to connect to and click 'Search'

16) Once repository has been found, click 'Connect' to link new app to Github repository

17) In 'Automatic deploys', select the 'Enable Automatic Deploy' option

18) To view your command line on the Heroku platform, once a new code has been pushed to Github, log on to Heroku

19) Select the required app that appears on your home screen

20) Select 'Open app' on the right hand side of the screen 

21) The app should appear in a new tab on the web browser

## Credits 

### Content

I would like to acknowledge the below organizations:

* Code institute for providing a python essentials template to work from and a terminal on Heroku to deploy my project.
* [The Spruce Crafts](https://www.thesprucecrafts.com/the-basic-rules-of-battleship-411069) for the rules of battle ships 
* To create a flowchart for my project, [diagrams.net](https://app.diagrams.net/). 
* The external python library [termcolor](https://pypi.org/project/termcolor/) to import colour to text.
* [Pep8 online](http://pep8online.com/), for code validation checking.
* [Black PEP8](https://black.vercel.app/) for helping format code to PEP8 standards
* [ShareX](https://getsharex.com/) for taking screenshots
* [Patorjk](https://patorjk.com/software/taag/#p=display&f=Cybermedium&t=Battleships) for the ASCI used for the opening title

### Acknowledgements

* I would like to thank my mentor Reuben for his consistent good advice and guidance. 

* My family for all their love and support.

* My class and our Cohort Facilitator Kasia in Code Institute for making this a fun experience.

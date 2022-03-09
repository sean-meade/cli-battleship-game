To Do:

Programming:
- Nice to have:
    - make it so someone can use 3e or e3
    - Add place ship function to class
    - create unit test to periodically check the board functionality (not required for grading)

README:
- Existing features
- Features left to implement
- Testing: User needs
- Testing: Challenges
- Validator testing
- Unfixed bugs
- Content
- Acknowledgements

Other:
- Nicer version of the flow chart (nice to have)
- Maybe put button in beside the terminal rather then below it? - It would mean the whole thing would fit on the screen without scrolling. What about title and button under it on the left and the terminal on the right?


Link to live site: https://cli-battleship-game.herokuapp.com/

# Battleship

![responsive-layout]()

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

This is a command line version of the classic game battleships. The program allows the user to place their ships on their side of the board and then attack the computers ships on the computers board. The first to make 17 hits wins the game.

## How To Play

CLI Battleship is a command line take on the classic battleship game.

In this version, the player chooses a username and their board is created. The board has letters a to j in the y direction and number 0 to 9 in the x.

It then prompts the player to place their ships on the board. There are 5 ships in total of sizes 2, 3, 3, 4, and 5. The player must choose a starting point which is done by giving coordinates which is a number and letter pairing (e.g. 3e). Then they are asked what direction they would like to place the ship (i.e. up, down, left, and right).

Once all ships are placed the player will be prompted to make the first attack. This means you are attacking the computers board, which shows on the screen as blank. Using the same coordinate system as placing the ships you can attack (e.g. 8f).

The computer will make its move and will continue back and forth until one player has sunk all the other players ships.

If the user wins their username and time is added to the leader board and if they are in the top 3 they will show up on the opening screen.

## Features

### Existing features

1. Structure and formatting
* The main body of text  

* The program code structure was developed based on the following process flow diagram, which was drafted before any of the code was written. 

![flowchart]()

2. Title and intro
* The title is 
* The welcoming statement prompts the user for a name 

![title-intro]()

2. <list features>

![]()

### Future Features

If I had further time on this project I would like to add 

- N, S, E, W instead of up, down, left, right
- you sunk my battleship
- Add a weighted system where if the computer gets a hit it will attack around that space

## Data Model

## Testing

### Solved Bugs

### Validator testing

In this project, the errors that I mostly came across were the following:

1. Pep8 E501 - line too long:
* This error was rectified either by using either a backslash or quotation marks to split a long piece of text into two and separating them out onto two lines. 

![]()

2. 

### Unfixed bugs 


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

22) The link to my Heroku app is:
<insert link>


## Credits 

### Content

I would like to acknowledge the below organizations:

* Code institute for providing a python essentials template to work from and a terminal on Heroku to deploy my project.
* The following site for the rules of battle ships []()
* To create a flowchart for my project, [diagrams.net](https://app.diagrams.net/). 
* The external python library [termcolor](https://pypi.org/project/termcolor/) to import colour to text.
* [Pep8 online](http://pep8online.com/), for code validation checking.

### Acknowledgements


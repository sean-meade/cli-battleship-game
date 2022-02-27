To Do:

Programming:
- Add proper welcome page
- Add instructions
- Add rules
- Print empty board for computer (that shows hits and misses)
- 

README:
- Elaborate Intro
- Site owner goals
- User needs
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
2. [UX](#ux)
    * [Site owner goals](#site-owner-goals)
    * [User needs](#user-needs)
3. [Features](#features)
    * [Existing features](#existing-features)
    * [Features left to implement](#features-left-to-implement)
4. [Testing](#testing)
    * [User needs](#user-needs)
    * [Challenges](#challenges)
    * [Validator testing](#validator-testing)
    * [Unfixed bugs](#unfixed-bugs)
5. [Deployment](#deployment)
6. [Credits](#credits)
    * [Content](#content)
    * [Acknowledgements](#acknowledgements)


## Introduction 

This is a command line version of the classic game battleships. <short description> 

## UX

### Site owner goals

The objectives of the site owner are: 
1. To create an attractive, command line program, adhering to good UX design principles.
2. To create a fun game.

### User needs

User would like:

1. To 

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

### Features left to implement

If I had further time on this project I would like to add 

## Testing

### User needs

Here I will identify a user need and run through how this is being met by the program.

1. 

![]()

### Challenges

1. Code structure

explain challenges

![]()

2. 

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


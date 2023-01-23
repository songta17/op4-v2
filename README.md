# Chess Tournament Memories (Python using the MVC pattern).


## CONTENTS

1. [Project initialization](#id-section1)
    1. [Windows](#id-section1-1)
    1. [MacOS / Linux](#id-section1-2)
    3. [Generate flake8 report](#id-section1-3)
2. [Menu Options](#id-section2)
    1. [Main Menu](#section2-1)
    2. [Reports Menu](#section2-2)
3. [Examples of display](#section3)


<div id='id-section1'></div>

## 1. Project initialization

<div id='id-section1-1'></div>


#### i. Windows :
In Windows Powershell, go to the folder where you want to copy the application.

###### Clone the project
    $ git clone https://github.com/songta17/op4-v2.git

###### Enable virtual environment
    $ cd op4-v2
    $ python -m venv env 
    $ ~env\scripts\activate
    
###### Install required packages
    $ pip install -r requirements.txt

###### Start the program
    $ python chess_tournament_memories.py


<div id='id-section1-2'></div>

---------

#### ii. MacOS / Linux :
In the terminal, go to the folder where you want to copy the application.
###### Clone the project
    $ git clone https://github.com/songta17/op4-v2.git

###### Enable virtual environment
    $ cd op4-v2
    $ python3 -m venv env 
    $ source env/bin/activate
    
###### Install required packages
    $ pip install -r requirements.txt

###### Start the program
    $ python3 chess_tournament_memories.py


<div id='id-section1-3'></div>

----------

#### iii. Generate flake8 report

    $ flake8 --format=html --htmldir=flake-report
open flake-report/index.html

**Vous trouverez le rapport dans le dossier _'flake8-report'_.**

_Dernier rapport exporté :_

![latest_report](img/latest_report.png)

<div id='id-section2'></div>

## 2. Options des menus

<div id='id-section2-1'></div>

#### i. Main Menu 
![main_menu](img/main_menu.png)

<div id='id-section2-2'></div>

#### ii. Reports Menu
![main_menu](img/reports_menu.png)

<div id='id-section3'></div>

## 3. Exemples d'affichage
#### Matchs d'une ronde :
![round](img/round_example.png)

#### Rapport des joueurs :
![player_report](img/players_report.png)

#### Rapport des rondes :
![round_report](img/rounds_report.png)
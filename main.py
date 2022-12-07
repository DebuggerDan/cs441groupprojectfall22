import time
import random as rnd
import sys

from platform import python_version as identifypy
from warops import sitrep

from board import Board as bd

## I. Global Constants & Initializations

Hidden_Pattern=[[' ']*10 for x in range(10)]
Guess_Pattern=[[' ']*10 for x in range(10)]

TURNS = 10


## II. Main WOBR Battleship Simulation Function.

def main():
    bd.create_ships(Hidden_Pattern)
    bd.print_board(Hidden_Pattern)
    #turns = 10 # converted to global variable
    turnnum = TURNS
    print("./WOBR.sh: WELCOME, GENERAL.")
    while (turnnum > 0):
        # print("./WOBR.sh: WELCOME, GENERAL.") # realized this was iteratively-looped lul
        print("./WOBR.sh: COMMENCING DUAL-PARTICIPANT NAVAL WAR GAMES THEATER SIMULATION...")
        bd.print_board(Guess_Pattern)
        row,column = bd.get_ship_location()
        if (Guess_Pattern[row][column] == '-'):
            print(
                "./WOBR.sh: [ALERT #1] SELECTED COMBAT AREA ALREADY CLEARED.\n[INSERT REMAINING #] ENEMY VESSELS REMAIN OPERATIONAL IN COMBAT AREA.")
        elif (Hidden_Pattern[row][column] =='X'):
            print(
                "./WOBR.sh: [ALERT #2] OPPONENT NAVAL VESSEL SUCCESSFULLY DESTROYED.\n[INSERT REMAINING #] ENEMY VESSELS REMAIN OPERATIONAL IN COMBAT AREA.")
            Guess_Pattern[row][column] = 'X'
            turnnum -= 1
        else:
            print("./WOBR.sh: [ALERT #3] PRE-EMPTIVE NAVAL STRIKE UNSUCCESSFUL.\n[INSERT REMAINING #] ENEMY VESSELS REMAIN OPERATIONAL IN COMBAT AREA.")
            Guess_Pattern[row][column] = '-'
            turnnum -= 1
        if  (bd.count_hit_ships(Guess_Pattern) == 5):
            print("./WOBR.sh: [ALERT #4] CONGRATULATIONS. OPPONENT HAS BEEN TOTALLY ANNIHILATED.\n[INSERT WINNER'S NAME] HAS ACHIEVED NAVAL SUPERIORITY.")
            sys.sleep(3)
            break
        print("./WOBR.sh: OPPONENT [INSERT NAME] HAS:\n#" + str(turnnum) + " AGM-84H/K STANDOFF LAND ATTACK MISSILE-EXPANDED RESPONSE 'SLAM-ER' HARPOON CRUISE MISSILES REMAINING .") # realistic battleship-situation munitions lore for immersion
        if (turnnum == 0):
            print('Game Over ')
            break

if (__name__ == "__main__"):
    
    if sys.version_info.major >= 3:
        print("./WOBR.sh: ADEQUATE SYSTEM FRAME LEVEL OF AT LEAST THREE [3] DETECTED: " + identifypy() + "...")
        sys.sleep(1)
        print("./WOBR.sh: CONTINUING...")
        sys.sleep(3)
        
    elif sys.version_info.major <= 2:
        print("./WOBR.sh: [ALERT] SYSTEM FRAME LEVEL BELOW AT LEAST [3] MAY CAUSE OPERATIONAL CONFLICTS.")
        sys.sleep(1)
        print("./WOBR.sh: DETECTED SYSTEM FRAME LEVEL: " + identifypy() + ". CONSIDER USING {PYTHON 3} OR HIGHER.")
        sys.sleep(5)
        print("./WOBR.sh: CONTINUING...")
        sys.sleep(3)
    
    # shameless War Games reference here (WOPR; "War Operations Plan Response")
    print("./WOBR.sh: INITIALIZING WAR OPERATIONS BATTLESHIP REACTOR...")
    time.sleep(2)
    
    main()
    pass

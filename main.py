import time
import random as rnd
import sys

from platform import python_version as identifypy
from warops import sitrep
from board import Board

## I. Global Constants & Initializations

TURNS = 10


## II. Main WOBR Battleship Simulation Function.

def main():
    bd = Board()
    complete = False
    turnnum = TURNS
    print("./WOBR.sh: WELCOME, GENERAL.")

    bd.create_ships()
    bd.print_board(False)

    while not complete:
        # print("./WOBR.sh: WELCOME, GENERAL.") # realized this was iteratively-looped lul
        print("./WOBR.sh: COMMENCING DUAL-PARTICIPANT NAVAL WAR GAMES "
              "THEATER SIMULATION...")
        bd.print_board()

        row, col = bd.get_ship_location()
        success = bd.guess(row, col)

        if success == 1:
            print("./WOBR.sh: [ALERT #2] OPPONENT NAVAL VESSEL SUCCESSFULLY "
                  "DESTROYED.")
        elif success == 0:
            print("./WOBR.sh: [ALERT #3] PRE-EMPTIVE NAVAL STRIKE UNSUCCESSFUL.")
        else:
            print("./WOBR.sh: [ALERT #1] SELECTED COMBAT AREA ALREADY CLEARED.")

        print(f"{bd.remaining_ships()} ENEMY VESSELS REMAIN OPERATIONAL IN "
              f"COMBAT AREA.")

        turnnum -= 1

        # realistic battleship-situation munitions lore for immersion
        print(f"./WOBR.sh: PLAYER 1 HAS {str(turnnum)} AGM-84H/K STANDOFF "
              f"LAND ATTACK MISSILE-EXPANDED RESPONSE 'SLAM-ER' HARPOON CRUISE "
              f"MISSILES REMAINING.")

        if bd.complete():
            print("./WOBR.sh: [ALERT #4] CONGRATULATIONS. OPPONENT HAS BEEN "
                  "TOTALLY ANNIHILATED.\nPLAYER 1 HAS ACHIEVED NAVAL SUPERIORITY.")
            complete = True

        if turnnum == 0:
            print('Game Over')
            complete = True

if __name__ == "__main__":
    if sys.version_info.major >= 3:
        print(f"./WOBR.sh: ADEQUATE SYSTEM FRAME LEVEL OF AT LEAST THREE [3] "
              f"DETECTED: {identifypy()}...")
    elif sys.version_info.major <= 2:
        print("./WOBR.sh: [ALERT] SYSTEM FRAME LEVEL BELOW AT LEAST [3] MAY "
              "CAUSE OPERATIONAL CONFLICTS.")
        print(f"./WOBR.sh: DETECTED SYSTEM FRAME LEVEL: {identifypy()}. "
              f"CONSIDER USING {{PYTHON 3}} OR HIGHER.")

    # shameless War Games reference here (WOPR; "War Operations Plan Response")
    print("./WOBR.sh: INITIALIZING WAR OPERATIONS BATTLESHIP REACTOR...")

    main()

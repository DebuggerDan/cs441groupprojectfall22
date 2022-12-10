### CS 441, Fall 2022 - Group Project: Battleships - Main Program
### Primary Objectives: main(), initialization, etc.
### Alana G., Dan J., & Evan L.

import time
import random as rnd
import sys

from platform import python_version as identifypy
# from warops import sitrep
from board import Board
from genetic_algorithm import GeneticAlgorithm
from hill_climbing import HillClimbing

## I. Global Constants & Initializations

TURNS = 10

## Ia. Genetic Algorithm Constants & Initializations
POPULATIONSIZE = 100
MUTATION_RATE = 1
CROSSOVER_RATE = 0.5
ELITES = 2
TOURNAMENT = 5
GENERATIONS = 100

# Opponent values coorrelate to the following:
# 0 = Manual (User-Input)
# 1 = Genetic Algorithm
# 2 = Hill-Climbing Algorithm

OPPONENT_ONE = 1

## II. Main WOBR Battleship Simulation Function.

def main():
    # bd = Board()
    complete = False
    turnnum = TURNS
    print("./WOBR.sh: WELCOME, GENERAL.")

    ## Part A: Genetic Algorithm
    genalgo = GeneticAlgorithm(POPULATIONSIZE, MUTATION_RATE, CROSSOVER_RATE, ELITES, TOURNAMENT)
    genalgo.run(GENERATIONS)
    #print("\n./WOBR.sh: The Genetic Algorithmic Solution: " + str(geneticResults))
    #print("./WOBR.sh: Fitness (Note: Lower Value = Higher Fitness): " + str(genalgo.getFit(geneticResults)))
    
    ## Part B: Hill-Climbing Algorithm
    print("\n./WOBR.sh: Hill-Climbing Algorithmic Solution: ")
    
    hill_climbing = HillClimbing()
    hill_climbing.run()

    # bd.create_ships()
    # bd.print_board(False)

    # while not complete:
    #     # print("./WOBR.sh: WELCOME, GENERAL.") # realized this was iteratively-looped lul
    #     print("./WOBR.sh: COMMENCING DUAL-PARTICIPANT NAVAL WAR GAMES "
    #           "THEATER SIMULATION...")
    #     bd.print_board()

    #     row, col = bd.get_ship_location()
    #     success = bd.guess(row, col)

    #     if success == 1:
    #         print("./WOBR.sh: [ALERT #2] OPPONENT NAVAL VESSEL SUCCESSFULLY "
    #               "DESTROYED.")
    #     elif success == 0:
    #         print("./WOBR.sh: [ALERT #3] PRE-EMPTIVE NAVAL STRIKE UNSUCCESSFUL.")
    #     else:
    #         print("./WOBR.sh: [ALERT #1] SELECTED COMBAT AREA ALREADY CLEARED.")

    #     print(f"{bd.remaining_ships()} ENEMY VESSELS REMAIN OPERATIONAL IN "
    #           f"COMBAT AREA.")

    #     turnnum -= 1

    #     # realistic battleship-situation munitions lore for immersion
    #     print(f"./WOBR.sh: PLAYER 1 HAS {str(turnnum)} AGM-84H/K STANDOFF "
    #           f"LAND ATTACK MISSILE-EXPANDED RESPONSE 'SLAM-ER' HARPOON CRUISE "
    #           f"MISSILES REMAINING.")

    #     if bd.complete():
    #         print("./WOBR.sh: [ALERT #4] CONGRATULATIONS. OPPONENT HAS BEEN "
    #               "TOTALLY ANNIHILATED.\nPLAYER 1 HAS ACHIEVED NAVAL SUPERIORITY.")
    #         complete = True

    #     if turnnum == 0:
    #         print('Game Over')
    #         complete = True

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

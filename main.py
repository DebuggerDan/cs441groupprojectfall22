### CS 441, Fall 2022 - Group Project: Battleships - Main Program
### Primary Objectives: main(), initialization, etc.
### Alana G., Dan J., & Evan L.

import sys

from platform import python_version as identifypy
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
    print("./WOBR.sh: WELCOME, GENERAL.")

    ## Part A: Genetic Algorithm
    genalgo = GeneticAlgorithm(POPULATIONSIZE, MUTATION_RATE, CROSSOVER_RATE,
                               ELITES, TOURNAMENT)
    genalgo.run(GENERATIONS)

    ## Part B: Hill-Climbing Algorithm
    print()
    print("./WOBR.sh: Hill-Climbing Algorithmic Solution: ")

    hill_climbing = HillClimbing()
    hill_climbing.run()

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

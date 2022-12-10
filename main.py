### CS 441, Fall 2022 - Group Project: Battleships - Main Program
### Primary Objectives: main(), initialization, etc.
### Alana G., Dan J., & Evan L.

import sys

from platform import python_version
from genetic_algorithm import GeneticAlgorithm
from hill_climbing import HillClimbing
from warops import sitrep

## I. Global Constants & Initializations

TURNS = 10
ITERATIONS = 10

## Ia. Genetic Algorithm Constants & Initializations
POPULATIONSIZE = 100
MUTATIONRATE = 1
CROSSOVERRATE = 0.5
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

    x1points = list(range(1, ITERATIONS + 1))
    x2points = list(range(1, ITERATIONS + 1))
    y1points = []
    y2points = []

    ## Part A: Genetic Algorithm
    for idx in range(ITERATIONS):
        print(f"./WOBR.sh: A.) [Genetic Algorithmic] Solution for Iteration "
              f"#{str(idx + 1)}:")
        genalgo = GeneticAlgorithm(POPULATIONSIZE, MUTATIONRATE, CROSSOVERRATE,
                                ELITES, TOURNAMENT)

        y1points.append(genalgo.run(GENERATIONS))

    print()

    ## Part B: Hill-Climbing Algorithm
    for idx in range(ITERATIONS):
        print()
        print(f"./WOBR.sh: B.) [Hill-Climbing Algorithmic] Solution for "
              f"Iteration #{str(idx + 1)}:")

        y2points.append(HillClimbing.run())

    print("./WOBR.sh: BOTH GENETIC & HILL-CLIMBING ALGORITHMS COMPLETE.")
    print("./WOBR.sh: GENERATING SITUATIONAL REPORT...")

    sitrep(x1points, x2points, y1points, y2points)

    print("./WOBR.sh: SITUATIONAL REPORT GENERATED. SEE wobr.png FOR RESULTS.")
    print("./WOBR.sh: SHUTTING DOWN... (END)")

if __name__ == "__main__":
    if sys.version_info.major >= 3:
        print(f"./WOBR.sh: ADEQUATE SYSTEM FRAME LEVEL OF AT LEAST THREE [3] "
              f"DETECTED: {python_version()}...")

        # shameless War Games reference here (WOPR; "War Operations Plan Response")
        print("./WOBR.sh: INITIALIZING WAR OPERATIONS BATTLESHIP REACTOR...")

        main()
    # skip running if out of date Python version
    elif sys.version_info.major <= 2:
        print("./WOBR.sh: [ALERT] SYSTEM FRAME LEVEL BELOW AT LEAST [3] MAY "
              "CAUSE OPERATIONAL CONFLICTS.")
        print(f"./WOBR.sh: DETECTED SYSTEM FRAME LEVEL: {python_version()}. "
              f"CONSIDER USING {{PYTHON 3}} OR HIGHER.")

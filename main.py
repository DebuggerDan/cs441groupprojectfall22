### CS 441, Fall 2022 - Group Project: Battleships - Main Program
### Primary Objectives: main(), initialization, etc.
### Alana G., Dan J., & Evan L.

import sys
import numpy as np

from platform import python_version as identifypy
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

    x1points = []
    x2points = []
    y1points = []
    y2points = []
    
   # x1points = np.append(x1points, 0)
    #y1points = np.append(y1points, 0)
    # y1points = list(range(1, ITERATIONS + 1))]
    # y2points = list(range(1, ITERATIONS + 1))

    ## Part A: Genetic Algorithm
    #geneticresults = []
    print("./WOBR.sh: A.) [Genetic Algorithmic] Solution (with first & last initial guess-boards displayed, rest redacted for brevity) for Iteration #" + str(1) + ":")
    genalgo = GeneticAlgorithm(POPULATIONSIZE, MUTATIONRATE, CROSSOVERRATE,
                                ELITES, TOURNAMENT)
        
    x1points = np.append(x1points, 1)
    y1points = np.append(y1points, genalgo.run(GENERATIONS))
    
    for idx in range(ITERATIONS - 1):
        print("./WOBR.sh: A.) [Genetic Algorithmic] Solution for Iteration #" + str(idx + 2) + ":")
        genalgo = GeneticAlgorithm(POPULATIONSIZE, MUTATIONRATE, CROSSOVERRATE,
                                ELITES, TOURNAMENT)
        
        x1points = np.append(x1points, idx + 2)
        y1points = np.append(y1points, genalgo.run(GENERATIONS))
        
    # for x1 in range(int(len(geneticresults) / ITERATIONS)):
    #     x1point = x1 * ITERATIONS
    #     y1point = 0
        
    #     for y1 in range(ITERATIONS):
    #         y1point += geneticresults[x1 * ITERATIONS + y1]
        
    #     y1point /= ITERATIONS
        
    #     x1points.append(x1point)
    #     y1points.append(y1point)

    ## Part B: Hill-Climbing Algorithm
    #hillresults = []
    
    print()
    print("./WOBR.sh: B.) [Hill-Climbing Algorithmic] Solution for Iteration #" + str(idx + 1) + ":")

    hill_climbing = HillClimbing()
    
    x2points = np.append(x2points, 1)
    y2points = np.append(y2points, hill_climbing.run())
    
    for idx in range(ITERATIONS - 1):
        print()
        print("./WOBR.sh: B.) [Hill-Climbing Algorithmic] Solution for Iteration #" + str(idx + 2) + ":")

        hill_climbing = HillClimbing()
        
        x2points = np.append(x2points, idx + 2)
        y2points = np.append(y2points, hill_climbing.run())
        
    # for x2 in range(int(len(hillresults) / ITERATIONS)):
    #     x2point = x2 * ITERATIONS
    #     y2point = 0
        
    #     for y2 in range(ITERATIONS):
    #         y2point += hillresults[x2 * ITERATIONS + y2]
        
    #     y2point /= ITERATIONS
        
    #     x2points.append(x2point)
    #     y2points.append(y2point)

    
    print("./WOBR.sh: BOTH GENETIC & HILL-CLIMBING ALGORITHMS COMPLETE.")
    print("./WOBR.sh: GENERATING SITUATIONAL REPORT...")
    
    sitrep(x1points, x2points, y1points, y2points)#, supercowmode="ye")

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

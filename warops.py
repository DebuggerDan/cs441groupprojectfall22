### CS 441, Fall 2022 - Group Project: Battleships - War Operations
### Primary Objectives: Plotting, Strategy, & Miscellaneous Battleship Components)
### Alana G., Evan L., & Dan J.

import numpy as np
import matplotlib
from matplotlib import pyplot as p

matplotlib.use('Agg')

# Graph Implementation - Takes in two .csv files and plots the data (can be made
# to just take in two lists of x & y coordinates too {or tuples})
def sitrep(x1, x2, y1, y2, supercowmode=None):
    if supercowmode is None:
        #x1,y1 = np.loadtxt(player1, delimiter = ',', unpack=True)
        #x2,y2 = np.loadtxt(player2, delimiter = ',', unpack=True)

        p.plot(x1, y1, label = 'Player #1 (Genetic Algorithm) Results')
        p.plot(x2, y2, label = 'Player #2 (Hill-Climbing Algorithm) Results')

        p.title('WOBR: Player #1 (Genetic) vs. Player #2 (Hill-Climbing)')
        p.xlabel('# [Iteration(s)] of Game(s) Played')
        p.ylabel('Fitness (# ship-squares left) (lower = better)')

        p.xlim([1, 10])
        p.ylim([0, 25])
        
        p.legend()
        # p.show()

        p.savefig('wobr.png')
        p.close()

    else:
        print(x1)
        print(y1)
        print(x2)
        print(y2)
        
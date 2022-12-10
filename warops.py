### CS 441, Fall 2022 - Group Project: Battleships - War Operations
### Primary Objectiveds: Plotting, Strategy, & Miscellaneous Battleship Components)
### Alana G., Evan L., & Dan J.

import numpy as np
import matplotlib

matplotlib.use('Agg')

# Graph Implementation - Takes in two .csv files and plots the data (can be made
# to just take in two lists of x & y coordinates too {or tuples})
def sitrep(player1, player2):
    x1,y1 = np.loadtext(player1, delimiter = ',', unpack=True)
    x2,y2 = np.loadtext(player2, delimiter = ',', unpack=True)

    np.plot(x1, y1, label = "Player 1 Results")
    np.plot(x2, y2, label = "Player 2 Results")

    np.title('WOBR: Player 1 vs. Player 2')
    np.xlabel('# [Iteration(s)] of Game(s) Played')
    np.ylabel('Performance (y-axis)')

    np.legend()
    np.show()

    np.savefig('wobr.png')


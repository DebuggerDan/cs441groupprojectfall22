### CS 441, Fall 2022 - Group Project: Battleships - Board Initialization & Setup
### Primary Objectives: class Board(), initialization of ships, turns, & other game miscellany.
### Alana G., Dan J., & Evan L.

from random import randint, shuffle, randrange


## I. Initialization:

# Number of the initial 'guess' boards as the starting population
POPULATION = 100

ROWS = 10
COLUMNS = 10

MUTATIONRATE = 1

# I. Helper Functions

def genPos(boardtype):
    return genRows(boardtype)

def genRows(boardtype):
    if boardtype == 1: # 1 = Genetic Algorithm
        pos = list(range)
        shuffle(pos)
        
        return pos
    # if boardtype == 2: #2 = Hill-Climbing Algorithm
    
# def genFitness(boardtype):
#     if boardtype == 1: # 1 = Genetic Algorithm


# II. Board Class

class Board:
    def __init__(self, boardtype=None, pos=None, fitness=None):
        self.reset()
        self.remainingsquares = 0
        self.totalsquares = 0
        self.boardtype = boardtype if boardtype else 1
        self.pos = pos if pos else genPos(self.boardtype)
        self.fitness = fitness if fitness else 0

    def _check_ship_placement(self, row, col, orientation, length):
        """Checks whether a ship can be placed in a location without colliding
        with other ships or falling off the board.

        Args:
            row (int): row to place ship in
            col (int): column to place ship in
            orientation (int): whether ship is horizontal (0) or vertical (1)
            length (int): length of ship

        Returns:
            bool: whether ship can be placed in that location safely
        """
        if orientation == 0:
            if col + length > 10:
                return False
        else:
            if row + length > 10:
                return False

        # swap 0 -> 1 and 1 -> 0 such that if orientation == 0 (horizontal),
        # r = 0 and c = 1, and vice versa for orientation == 1.
        r, c = orientation, orientation ^ 1

        for i in range(length):
            # if r == 1, it will add i to the row
            # if c == 1, it will add i to the col
            if self.board[row + (i * r)][col + (i * c)] == "X":
                return False

        return True

    def reset(self):
        """Resets the board."""
        self.board = [[' '] * 10 for _ in range(10)]
        self.guesses = [[' '] * 10 for _ in range(10)]
        self.remainingships = 0
        self.totalsquares = 0

    def print_board(self, guesses=True):
        """Prints the board to the command line.

        Args:
            guesses (bool, optional): Whether to print guess board instead of
                hidden board. Defaults to True.
        """
        print('   0 1 2 3 4 5 6 7 8 9')
        print('  *********************')
        letters = "ABCDEFGHIJ"

        for i in range(len(self.board)):
            print(f"{letters[i]} |"
                  f"{'|'.join(self.guesses[i] if guesses else self.board[i])}|")

        print('  *********************')

    def get_ship_location(self):
        """Gets location of ship from command line input.

        Returns:
            int, int: row and column of ship as integers
        """
        # Enter the row from A to J
        row = input('Please enter a ship row A-J: ').upper()

        while row not in 'ABCDEFGHIJ' or len(row) > 1:
            row = input("Please enter a valid row A-J:")

        # Enter the column from 0 to 9
        column = input('Please enter a ship column 0-9: ').upper()

        while column not in '0123456789' or len(column) > 1:
            column = input("Please enter a valid column 0-9: ")

        return ord(row) - ord('A'), int(column)

    # Function that creates the ships
    def create_ships(self):
        """Generates ships on board."""
        ship_sizes = [2, 3, 3, 4, 5]

        for ship in ship_sizes:
            generated = False

            while not generated:
                ship_pos = randint(0, 99)
                col, row = ship_pos % 10, ship_pos // 10
                orientation = randint(0, 1) # 0 = horizontal, 1 = vertical

                if self._check_ship_placement(row, col, orientation, ship):
                    # swap 0 -> 1 and 1 -> 0 such that if orientation == 0 (horizontal),
                    # r = 0 and c = 1, and vice versa for orientation == 1.
                    r, c = orientation, orientation ^ 1

                    for i in range(ship):
                        # if r == 1, it will add i to the row
                        # if c == 1, it will add i to the col
                        self.board[row + (i * r)][col + (i * c)] = "X"

                    generated = True
                    
        self.remainingsquares, self.totalsquares = self.remaining_ships()

    def remaining_ships(self):
        """Counts ships remaining on the board."""
        count = 0

        for row in self.guesses:
            count += row.count("X")

        return count

    def complete(self):
        """Checks if game is complete (all ships sunk).

        Returns:
            bool: whether there are ships remaining
        """
        return self.remaining_ships() == 0

    def guess(self, row, col):
        """Takes a turn to guesses whether a ship is on the board.

        Args:
            row (int): row of ship
            col (int): column of ship

        Returns:
            int: -1 if already guessed; 0 if not hit; 1 if hit
        """
        if self.guesses[row][col] != " ":
            return -1

        if self.board[row][col] == " ":
            self.guesses[row][col] = "-"
            return 0
        else:
            self.guesses[row][col] = "X"
            self.remainingsquares -= 1
            return 1

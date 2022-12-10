### CS 441, Fall 2022 - Group Project: Battleships - Board Initialization & Setup
### Primary Objectives: class Board(), initialization of ships, turns, & other game miscellany.
### Alana G., Dan J., & Evan L.

from random import randint


class Board:
    ship_sizes = [2, 3, 3, 4, 5]
    ship_total = 17 # sum of ship_sizes

    def __init__(self, other_board=None):
        self.reset()

        if other_board:
            for i in range(len(other_board.board)):
                self.board[i] = other_board.board[i].copy()

    @staticmethod
    def _check_ship_placement(board, row, col, orientation, length):
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
            if board[row + (i * r)][col + (i * c)] == "X":
                return False

        return True

    def reset(self):
        """Resets the board."""
        self.board = [[' '] * 10 for _ in range(10)]

    def copy(self):
        result = Board()

        for i in range(len(self.board)):
            result.board[i] = self.board[i].copy()

        return result

    def print_board(self):
        """Prints the board to the command line."""
        print('   0 1 2 3 4 5 6 7 8 9')
        print('  *********************')
        letters = "ABCDEFGHIJ"

        for i in range(len(self.board)):
            print(f"{letters[i]} |"
                  f"{'|'.join(self.board[i])}|")

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
        for ship in Board.ship_sizes:
            generated = False

            while not generated:
                ship_pos = randint(0, 99)
                col, row = ship_pos % 10, ship_pos // 10
                orientation = randint(0, 1) # 0 = horizontal, 1 = vertical

                if Board._check_ship_placement(self.board, row, col,
                                               orientation, ship):
                    # swap 0 -> 1 and 1 -> 0 such that if orientation == 0 (horizontal),
                    # r = 0 and c = 1, and vice versa for orientation == 1.
                    r, c = orientation, orientation ^ 1

                    for i in range(ship):
                        # if r == 1, it will add i to the row
                        # if c == 1, it will add i to the col
                        self.board[row + (i * r)][col + (i * c)] = "X"

                    generated = True

    def remaining_squares(self):
        """Counts squares remaining on the board."""
        count = 0

        for row in self.board:
            count += row.count("X")

        return Board.ship_total - count

    def complete(self):
        """Checks if game is complete (all ships sunk).

        Returns:
            bool: whether there are ships remaining
        """
        return self.remaining_squares() == 0

    def guess(self, other_board, row, col):
        """Takes a turn to guesses whether a ship is on the board.

        Args:
            other_board (Board): other board to compare against
            row (int): row of ship
            col (int): column of ship

        Returns:
            int: -1 if already guessed; 0 if not hit; 1 if hit
        """
        if self.board[row][col] != " ":
            return -1

        if other_board.board[row][col] == " ":
            self.board[row][col] = "-"
            return 0
        else:
            self.board[row][col] = "X"
            return 1

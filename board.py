from random import randint, choice


class Board:
    def __init__(self):
        self.reset()

    def _check_ship_placement(self, row, col, orientation, length):
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
        self.board = [[' '] * 10 for _ in range(10)]
        self.guesses = [[' '] * 10 for _ in range(10)]

    def print_board(self, guesses=True):
        print('   0 1 2 3 4 5 6 7 8 9')
        print('  *********************')
        letters = "ABCDEFGHIJ"

        for i in range(len(self.board)):
            print(f"{letters[i]} |"
                  f"{'|'.join(self.guesses[i] if guesses else self.board[i])}|")

        print('  *********************')

    def get_ship_location(self):
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

    def remaining_ships(self):
        count = 0

        for row in self.guesses:
            count += row.count("X")

        return 5 - count

    def complete(self):
        return self.remaining_ships() == 0

    def guess(self, row, col):
        if self.board[row][col] == "X":
            self.guesses[row][col] = "X"
            return 1
        elif self.board[row][col] == " ":
            self.guesses[row][col] = "-"
            return 0

        return -1

from random import randint


class Board:
    def __init__(self):
        self.reset()

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
        for ship in range(5):
            generated = False

            while not generated:
                ship_pos = randint(0, 99)
                col, row = ship_pos % 10, ship_pos // 10

                print(ship_pos)
                print(row, col)

                if self.board[row][col] == " ":
                    self.board[row][col] = "X"
                    generated = True

    def count_hit_ships(board):
        count = 0

        for row in board:
            for column in row:
                if column == 'X':
                    count += 1

        return count

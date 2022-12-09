from random import randint


# let_to_num={'A':0,'B':1, 'C':2,'D':3,'E':4,'F':5,'G':6,'H':7}
class Board:
    def print_board(board):
        print('  1 2 3 4 5 6 7 8 9 10')
        print('  *********************')
        row_num = 1
        for row in board:
            if row_num <= 9:
                print(f"{row_num} |{'|'.join(row)}|")
                row_num += 1
            else:
                row_num = 0
                print(f"{row_num} |{'|'.join(row)}|")
        print('  *********************')

    def get_ship_location():
        # Enter the row number between 1 to 10
        row = input('Please enter a ship row 0-9: ').upper()

        while row not in '0123456789':
            row = input("Please enter a valid row 0-9:")

        # Enter the Ship column from A TO H
        column = input('Please enter a ship column 0-9: ').upper()

        while column not in '0123456789':
            column = input("Please enter a valid column 0-9: ")

        # return int(row)-1,let_to_num[column]
        return int(row)-1, int(column)-1

    # Function that creates the ships
    def create_ships(board):
        for ship in range(5):
            ship_r, ship_cl = randint(0, 9), randint(0, 9)
            while board[ship_r][ship_cl] == 'X':
                ship_r, ship_cl = randint(0, 9), randint(0, 9)
            board[ship_r][ship_cl] = 'X'

    def count_hit_ships(board):
        count = 0

        for row in board:
            for column in row:
                if column == 'X':
                    count += 1

        return count

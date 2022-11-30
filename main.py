from board import Board as bd
Hidden_Pattern=[[' ']*10 for x in range(10)]
Guess_Pattern=[[' ']*10 for x in range(10)]

def main():
    bd.create_ships(Hidden_Pattern)
    bd.print_board(Hidden_Pattern)
    turns = 10
    while (turns > 0):
        print('Welcome to Battleship')
        bd.print_board(Guess_Pattern)
        row,column = bd.get_ship_location()
        if (Guess_Pattern[row][column] == '-'):
            print(' You already guessed that ')
        elif (Hidden_Pattern[row][column] =='X'):
            print(' Congratulations you have hit the battleship ')
            Guess_Pattern[row][column] = 'X'
            turns -= 1
        else:
            print('Sorry,You missed')
            Guess_Pattern[row][column] = '-'
            turns -= 1
        if  (bd.count_hit_ships(Guess_Pattern) == 5):
            print("Congratulations you have sunk all the battleships ")
            break
        print(' You have ' +str(turns) + ' turns remaining ')
        if (turns == 0):
            print('Game Over ')
            break

if (__name__ == "__main__"):
    main()
    pass

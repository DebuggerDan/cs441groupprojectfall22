### CS 441, Fall 2022 - Group Project: Battleships - Hill-Climbing Algorithm
### Primary Objectives: class HillClimbing(), helper functions, & misc. data-processing functions.
### Alana G., Evan L., & Dan J.

from board import Board
from random import randint


class HillClimbing:
    @staticmethod
    def _generate_best_successor(hidden_board, guess_board):
        previous = []
        square = -1
        last_remaining = guess_board.remaining_squares()

        for _ in range(100):
            while square == -1 or square in previous:
                square = randint(0, 99)

            previous.append(square)
            row, col = square // 10, square % 10
            successor = Board(guess_board)
            successor.guess(hidden_board, row, col)

            if last_remaining > successor.remaining_squares():
                return len(previous), successor

        return None

    @staticmethod
    def run():
        cycles = 100
        current_cycle = 0
        all_tries = []
        guess = Board()
        hidden = Board()

        hidden.create_ships()
        hidden.print_board()

        while not guess.complete() and current_cycle < cycles:
            tries, guess = HillClimbing._generate_best_successor(hidden, guess)
            all_tries.append(tries)
            current_cycle += 1

        sum_tries = sum(all_tries)
        print(f"./WOBR.sh: [HILL-CLIMBING ALGORITHM] Completed in {sum_tries} tries, with an average of "
              f"{round(sum_tries / len(all_tries), 1)} per successor. "
              f"Final result:")
        guess.print_board()
        
        avgfitness = round(sum_tries) / len(all_tries)
        return avgfitness

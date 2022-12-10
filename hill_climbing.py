### CS 441, Fall 2022 - Group Project: Battleships - Hill-Climbing Algorithm
### Primary Objectives: class HillClimbing(), helper functions, & misc. data-processing functions.
### Alana G., Evan L., & Dan J.

# function Hill-Climbing(problem) returns a state that is a local maximum
#     current <- Make-Node(problem.Initial-State)
#     loop do
#         neighbor <- a highest-value successor of current
#         if neighbor.Value <= current.Value then return current.State
#         current <- neighbor

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
                return successor

        return None

    @staticmethod
    def run():
        cycles = 100
        hidden = Board()
        hidden.create_ships()
        hidden.print_board()

        guess = Board()

        current_cycle = 0

        while not guess.complete() and current_cycle < cycles:
            guess = HillClimbing._generate_best_successor(hidden, guess)
            current_cycle += 1

        print(f"Completed in {current_cycle} cycles. Final result:")
        guess.print_board()

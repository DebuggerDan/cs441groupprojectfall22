### CS 441, Fall 2022 - Group Project: Battleships - Genetic Algorithm
### Primary Objectives: class GeneticAlgorithm(), helper functions, & misc. data-processing functions.
### Alana G., Dan J., & Evan L.

from board import Board
import random as rnd

## I. Initialization:

# Number of the initial 'guess' boards as the starting population
POPULATION = 100
TURNS = 100

ROWS = 10
COLUMNS = 10

MUTATIONRATE = 1

## III. Genetic Algorithm:

class GeneticAlgorithm:
    def __init__(self, populationsize=None, mutagenrate=None, crossoverrate=None,
                 elites=None, tournamentsize=None):
        self.populationsize = populationsize if populationsize else POPULATION
        self.mutagenrate = mutagenrate if mutagenrate else MUTATIONRATE / 100
        self.crossoverrate = crossoverrate if crossoverrate else self.mutagenrate
        self.elites = elites if elites else 2
        self.tournamentsize = tournamentsize if tournamentsize else 5
        self.childlength = 10
        self.population = self.init_population()

    def init_population(self):
        population = []
        for idx in range(0, self.populationsize):
            population.append(self.genChild(idx))
        return population

    def genChild(self, num):
        newguessboard = Board()
        newguessboard.create_ships()
        if num == 0 or num == 99:
            print("./WOBR.sh: [GENETIC ALGORITHM] INITIAL POPULATION GUESSBOARD #" +
                f"{str(num + 1)}:")
            newguessboard.print_board()
        return newguessboard

    def randMove(self):
        return self.population[rnd.randint(0, len(self.population) - 1)]

    def guessMove(hboard, gboard):
        guessPos = rnd.randint(0, 99)
        prev = []
        remainingsquares = Board.remaining_squares()

        for _ in range(100):
            while square == -1 or square in prev:
                square = rnd.randint(0, 99)
                prev.append(square)

            row, col = guessPos // 10, guessPos % 10
            successor = Board(gboard)
            successor.guess(hboard, row, col)

            if remainingsquares > successor.remaining_squares():
                return successor

        return None

    # IIIa. Genetic Algorithm: Calculation Helper Functions

    def getFit(self, child):
        return child.remaining_squares()

    def getAvgFit(self):
        avgFit = 0

        for i in range(len(self.population)):
            avgFit += self.getFit(self.population[i])

        result = avgFit / len(self.population)
        return result

    def getBestChild(self):
        best = None
        for idx in range(0, len(self.population)):
            if best is None or self.getFit(self.population[idx]) < self.getFit(best):
                best = self.population[idx]
        return best

    # IIIb. Genetic Algorithm: Mutation, Selection, & Crossover-Evolution Functions

    def mutate(self, child):
        child.reset()
        child.create_ships()
        return child

    def selection(self):
        newpopulation = []

        for idx in range(self.elites):
            newpopulation.append(self.population[idx])

        for _ in range(self.elites, self.populationsize):
            parent1 = self.tourny()
            parent2 = self.tourny()
            child = self.crossover(parent1, parent2)

            if rnd.randint(0, len(self.population) - 1) < self.mutagenrate:
                child = self.mutate(child)

            newpopulation.append(child)
        self.population = newpopulation
        return self.population

    def tourny(self):
        highlander = None
        for _ in range(self.tournamentsize):
            idx = rnd.randint(0, len(self.population) - 1)
            if highlander is None or self.getFit(self.population[idx]) > self.getFit(highlander):
                highlander = self.population[idx]
        return highlander

    def crossover(self, parent1, parent2):
        child = Board()
        for idx1 in range(len(parent1.board)):
            for idx2 in range(len(parent1.board[idx1])):
                if rnd.randint(0, len(self.population) - 1) < self.crossoverrate:
                    child.board[idx1][idx2] = parent1.board[idx1][idx2]
                else:
                    child.board[idx1][idx2] = parent2.board[idx1][idx2]

        return child

    # IIIc. Genetic Algorithm: Initialization Functions

    def algo(self, generations):
        bestfitdata = []
        avgfitdata = []
        best = None

        for _ in range(0, generations):
            self.selection()

        bestfitdata = self.getFit(self.getBestChild())
        avgfitdata = self.getAvgFit()
        best = self.getBestChild()

        return bestfitdata, avgfitdata, best

    def run(self, generations):
        bestfitdata, avgfitdata, best = self.algo(generations)

        print("./WOBR.sh: Best Battleship Solution:")
        best.print_board()
        print()
        print("./WOBR.sh: Best Fitness Score:")
        print(str(bestfitdata))
        print()
        print("./WOBR.sh: Average Genetic Algorithm Population Fitness "
              "(Note: Lower Value = Higher Fitness):")
        print(str(avgfitdata))

        return avgfitdata
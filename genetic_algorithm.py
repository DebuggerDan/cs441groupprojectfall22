### CS 441, Fall 2022 - Group Project: Battleships - Genetic Algorithm
### Primary Objectives: class GeneticAlgorithm(), helper functions, & misc. data-processing functions.
### Alana G., Dan J., & Evan L.

from board import Board
import random as rnd

# From Class Textbook, Russel, Norvig, 3rd Ed., pg 137:
# function Genetic-Algorithm(population, Fitness-Fn) returns an individual
#     inputs: population, a set of individuals
#             Fitness-Fn, a function that measures the fitness of an individual
#     repeat
#         new_population <- empty set
#         for i = 1 to Size(population) do
#             x <- Random-Selection(population, Fitness-Fn)
#             y <- Random-Selection(population, Fitness-Fn)
#             child <- Reproduce(x, y)
#             if(small random probability) then child <- Mutate(child)
#             add child to new_population
#         population <- new_population
#     until some individual is fit enough, or enough time has elapsed
#     return the best individual in population, according to Fitness-Fn

# function Reproduce(x, y) returns an individual
#     inputs: x, y, parent individuals
#     n <- Length(x)
#     c <- random number from 1 to n
#     return Append(Substring(x, 1, c), Substring(y, c + 1, n))

## I. Initialization:

# Number of the initial 'guess' boards as the starting population
POPULATION = 100
TURNS = 100

ROWS = 10
COLUMNS = 10

MUTATIONRATE = 1

## II. Helper Functions:
# def genPos():
#     return genRows()

# def genRows():
#     pos = list(range(ROWS))
#     rnd.shuffle(pos)
    
#     return pos

## III. Genetic Algorithm:
# class GeneticAlgorithm(self, (if available parameters to follow:) initialBoard, initialPopulation, population, mutagen, rownum, colnum)
# class GeneticAlgorithm:
#     def __init__(self, initialBoard=None, popsize=None, initialPopulation=None, mutagen=None, rownum=None, colnum=None):
#         self.initialBoard = initialBoard if initialBoard else genBoard()
#         self.popsize = popsize if popsize else POPULATION
#         self.initialPopulation = initialPopulation if initialPopulation else initialPopulation(self.popsize)
#         self.mutagen = mutagen if mutagen else MUTATIONRATE
#         self.rownum = rownum if rownum else ROWS
#         self.colnum = colnum if colnum else COLUMNS
#         self.shipsquares = 0
    
    # def random(self):
    #     randompos = []

    #     for _ in range(self.rownum):
    #         randompos.append(rnd.randrange(0, self.colnum))
    
class GeneticAlgorithm:
    def __init__(self, populationsize=None, mutagenrate=None, crossoverrate=None, elites=None, tournamentsize=None):#, childlength=C):
        self.populationsize = populationsize if populationsize else POPULATION
        self.mutagenrate = mutagenrate if mutagenrate else MUTATIONRATE / 100
        self.crossoverrate = crossoverrate if crossoverrate else self.mutagenrate
        self.elites = elites if elites else 2
        self.tournamentsize = tournamentsize if tournamentsize else 5
        self.childlength = 10 
        self.population = self.init_population()
        #genRows()
        
    def init_population(self):
        population = []
        for _ in range(0, self.populationsize):
            population.append(self.generate_child())
        return population
    
    def generate_child(self):
        child = []
        for _ in range(0, self.childlength):
            child.append(rnd.randint(0, 1))
        return child
    
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
        fitness = 0
        for idx in range(0, len(child)):
            if child[idx] == 1:
                fitness += 1
        return fitness

      
    def getPopFit(self, population):
        population_fitness = 0
        for idx in range(0, len(population)):
            population_fitness += self.getFit(population[idx])
        return population_fitness
    
    
    def getBestChild(self, population):
        best = population[0]
        for idx in range(0, len(population)):
            if self.getFit(population[idx]) > self.getFit(best):
                best = population[idx]
        return best
    
    # IIIb. Genetic Algorithm: Mutation, Selection, & Crossover-Evolution Functions
    
    def mutate(self, child):
        for idx in range(0, len(child)):
            if rnd.random() < self.mutagenrate:
                if child[idx] == 0:
                    child[idx] = 1
                else:
                    child[idx] = 0
        return child

    def selection(self, population):
        currpopulation = []
        mutagenrate = 0
        if self.elites:
            currpopulation.append(self.getBestChild(population))
            mutagenrate = 1
        for _ in range(mutagenrate, len(population)):
            parent1 = self.tourny(population)
            parent2 = self.tourny(population)
            child = self.crossover(parent1, parent2)
            currpopulation.append(self.mutate(child))
        return currpopulation

    def tourny(self, population):
        tourny = []
        for _ in range(0, self.tournamentsize):
            random_id = rnd.randint(0, len(population) - 1)
            tourny.append(population[random_id])
        tournament_best = tourny[0]
        for idx2 in range(0, len(tourny)):
            if self.getFit(tourny[idx2]) > self.getFit(tournament_best):
                tournament_best = tourny[idx2]
        return tournament_best

    def crossover(self, parent1, parent2):
        child = []
        for idx in range(0, len(parent1)):
            if rnd.random() < self.crossoverrate and idx > 0:
                child.append(parent1[idx])
            else:
                child.append(parent2[idx])
        return child
    
    # IIIc. Genetic Algorithm: Initialization Functions
    
    def run(self, epochs):
        population = self.init_population()
        for _ in range(0, epochs):
            population = self.selection(population)
            
        print("./WOBR.sh: Initial Genetic Algorithm Population Fitness: " + str(self.getPopFit(population)))
        return self.getBestChild(population)

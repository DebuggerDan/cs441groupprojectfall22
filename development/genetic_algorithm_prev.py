#### [PREVIOUS FILE]

### CS 441, Fall 2022 - Group Project: Battleships - Genetic Algorithm
### Primary Objectives: class GeneticAlgorithm(), helper functions, & misc. data-processing functions.
### Alana G., Dan J., & Evan L.

import numpy as np
import math
import board as board
import random as rnd

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

ROWS = 10
COLUMNS = 10

MUTATIONRATE = 1

# class Moves:

## II. Helper Functions:

# class Guess:
#     def __init__(self, pos=None):
#         self.pos = pos if pos else genPos()
#         self.fitness = genFit(self.pos)

def genPos():
    return genRows()

def genRows():
    pos = list(range(ROWS))
    rnd.shuffle(pos)
    
    return pos

def genBoard():
    #if self.initialBoard is None:
    #    newboard = Board()
    #    print("./WOBR.sh: INITIALIZATION OF GENETIC ALGORITHM...")
    #    newboard.create_ships()
    #    print("./WOBR.sh: INITIAL BOARD GENERATED AS FOLLOWS:")
    #   newboard.print_board(False)
    #    return newboard
    #else:
        newboard = board.Board()
        newboard.create_ships()
        return newboard

def random():
    randompos = []

    for _ in range(ROWS):
        randompos.append(rnd.randrange(0, COLUMNS))

def initialPopulation(populationsize):
    #initBoard = initialBoard if initialBoard else self.initialBoard
    thehighseas = []
    
    for _ in range(populationsize):
        thehighseas.append(board.Board())

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
            
def genRows():#self):
    pos = list(range(ROWS))
    rnd.shuffle(pos)
    return pos

def attackCrossover(col1, col2, row1, row2):
    return (row1 + col1) == (row2 + col2) or \
        ((ROWS - 1 - row1) + col1) == ((ROWS - 1 - row2) + col2)
        
def attackHorizontal(row1, row2):
    return row1 == row2

def attack(col1, col2, row1, row2):
    return attackCrossover(col1, col2, row1, row2) \
        or attackHorizontal(row1, row2)
        
def concurrentAttacks(pos, currboard):
    attacks = 0
    
    for idx1 in range(currboard.totalsquares):
        for idx2 in range(idx1 + 1, currboard.totalsquares):
            if attack(idx1, idx2, pos[idx1], pos[idx2]):
                attacks += 1

    return attacks

def maxConcurrentAttacks(currboard):
    return math.comb(currboard.totalsquares)
        
def genFit(pos, currboard):
    return maxConcurrentAttacks(currboard) - concurrentAttacks(pos, currboard) + 1        

def crossOver(firstparent, secondparent):
    firstchild, secondchild = uniqueCriss(firstparent, secondparent)
    
    firstchild = mutation(firstchild)
    secondchild = mutation(secondchild)
    
    return board.Board(1, firstchild), board.Board(1, secondchild)
    
def uniqueCriss(firstparent, secondparent):
    
    randpos = rnd.randrange(1, COLUMNS - 1)
    
    firstchild = []
    secondchild = []
    
    for idx1 in range(0, COLUMNS):
        for idx2 in range(0, randpos):
            if secondparent.pos[idx1] == firstparent.pos[idx2]:
                firstchild.append(secondparent.pos[idx1])
    
    for idx in range(randpos, COLUMNS):
        firstchild.append(firstparent.pos[idx])
        
    for idx in range(0, randpos):
        secondchild.append(secondparent.pos[idx])
        
    
    for idx1 in range(0, COLUMNS):
        for idx2 in range(randpos, COLUMNS):
            if firstparent.pos[idx1] == secondparent.pos[idx2]:
                secondchild.append(firstparent.pos[idx1])
                
    return firstchild, secondchild


#@staticmethod
def mutation(self, child):
    if rnd.uniform(0,1) < MUTATIONRATE / 100:
        idx = rnd.sample(range(0, COLUMNS), 2)
        curr = child[idx[0]]
        
        child[idx[0]] = child[idx[1]]
        child[idx[1]] = curr
        
        return child

# #@staticmethod
# def _reproduce():
#     pass

# #@staticmethod
# def run():
#     pass

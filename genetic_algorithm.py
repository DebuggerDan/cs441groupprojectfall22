### CS 441, Fall 2022 - Group Project: Battleships - Genetic Algorithm
### Primary Objectives: class GeneticAlgorithm(), helper functions, & misc. data-processing functions.
### Alana G., Dan J., & Evan L.

import numpy as np
import math
import board
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

def genFit(pos):
    return max

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
        newboard = Board()
        newboard.create_ships()
        return newboard

def random():
    randompos = []

    for _ in range(self.rownum):
        randompos.append(rnd.randrange(0, self.colnum))

def initialPopulation(populationsize):
    #initBoard = initialBoard if initialBoard else self.initialBoard
    thehighseas = []
    
    for _ in range(populationsize):
        thehighseas.append(Board())

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
    pos = list(range(self.rownum))
    rnd.shuffle(pos)
    return pos

def attackCrossover(col1, col2, row1, row2):
    return (row1 + col1) == (row2 + col2) or \
        ((self.rownum - 1 - row1) + col1) == ((self.rownum - 1 - row2) + col2)
        
def attackHorizontal(row1, row2):
    return row1 == row2

def attack(col1, col2, row1, row2):
    return self.attackCrossover(col1, col2, row1, row2) \
        or self.attackHorizontal(row1, row2)
        
def uniqueCrossover(firstparent, secondparent):
    firstchild, secondchild = uniqueCriss(firstparent, secondparent)
    
    firstchild = mutation(firstchild)
    secondchild = mutation(secondchild)
    
    return GuessPos(firstchild), GuessPos(secondchild)
    
#@staticmethod
def mutation(self, child):
    if rnd.uniform(0,1) < self.mutagen / 100:
        idx = rnd.sample(range(0, self.colnum), 2)
        curr = child[idx[0]]
        
        child[idx[0]] = child[idx[1]]
        child[idx[1]] = curr
        
        return child
    pass

#@staticmethod
def _reproduce():
    pass

#@staticmethod
def run():
    pass

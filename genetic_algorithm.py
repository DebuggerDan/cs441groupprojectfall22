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

class GeneticAlgorithm:
    @staticmethod
    def _mutate():
        pass

    @staticmethod
    def _reproduce():
        pass

    @staticmethod
    def run():
        pass

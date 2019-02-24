"""
The travelling Salesman Problem solved by local searches (Hill Climbing and Simulated Annealing)

@author: ss63
@date: February 23, 2019
@purpose: for CS 344

"""
from search import Problem, hill_climbing, simulated_annealing, \
    exp_schedule, genetic_search
from random import randrange
import random
import math
import time


class TSP(Problem):

    def __init__(self, initial, distances):
        self.initial = initial
        self.distances = distances

    #returns a list containing pairs of cities
    def actions(self, state):
       actions = []
     # return a pair of two cities from our path
       for i in range(3):
           pair = random.sample(range(1, len(self.initial)-1), 2)
           actions.append(pair)
       return actions

    # For each state, swap cities and return a  new state
    def result(self, state, move):
        #create a copy of current state that will be manipulated
        new_state = state[:]

        city_1 = state[move[0]]
        city_2 = state[move[1]]
        #swap cities
        new_state[move[0]] = city_2
        new_state[move[1]] = city_1
        return new_state

    # returns the path cost of given states
    def value(self, state):
        total_cost = 0
        for x in range(len(state) - 1):
            dist = [state[x], state [x +1]]
            dist.sort()
            total_cost += self.distances[tuple(dist)]
        total_cost = -total_cost
        return total_cost

if __name__ == '__main__':

    #intialize path and distances
    initial_path = [0, 1, 2, 3, 4, 5, 6, 0]
    distances = {(0, 1): 1, (0, 2): 2, (0, 3): 3, (0, 4): 4, (0, 5): 5, (0, 6): 6,
                 (1, 2): 7, (1, 3): 8, (1, 4): 9, (1, 5): 10, (1, 6): 11,
                 (2, 3): 12, (2, 4): 13, (2, 5): 14, (2, 6): 15,
                 (3, 4): 17, (3, 5): 18, (3, 6): 19,
                 (4, 5): 20, (4, 6): 21,
                 (5, 6): 22}


    # Initialize the TSP problem
    problem = TSP( initial_path,distances)
    print('Value of initial path: ' + str(problem.value(initial_path)))

    # Solve TSP using hill climbing
    hill_solution = hill_climbing(problem)
    print('Hill-climbing results:')
    print('\tThe path is: ' + str(hill_solution))
    print('\tThe value of this path is: ' + str(problem.value(hill_solution)))

    # Solve TSP using simulated annealing.
    annealing_solution = simulated_annealing(
        problem,
        exp_schedule(k=20, lam=0.005, limit=10000)
    )
    print('Simulated annealing results:')
    print('\tThe path is: ' + str(annealing_solution))
    print('\tThe value of this path is: ' + str(problem.value(annealing_solution)))

# I have noticed that, most of the time, Simulated annealing gives a better solution than hill climbing. This could be because hill-climbing is perhaps getting stuck only looking for local optimums, while simulated annealing is looking for global optimums.

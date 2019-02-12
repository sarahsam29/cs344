"""
This module implements local search on a simple abs function variant.
The function is a linear function  with a single, discontinuous max value
(see the abs function variant in graphs.py).

@author: kvlinden and ss63
@version 6feb2013
"""
from tools.aima.search import Problem, hill_climbing, simulated_annealing, \
    exp_schedule, genetic_search
from random import randrange
import math
import time


class AbsVariant(Problem):
    """
    State: x value for the abs function variant f(x)
    Move: a new x value delta steps from the current x (in both directions)
    """

    def __init__(self, initial, maximum=30.0, delta=0.001):
        self.initial = initial
        self.maximum = maximum
        self.delta = delta

    def actions(self, state):
        return [state + self.delta, state - self.delta]

    def result(self, stateIgnored, x):
        return x

    def value(self, x):
        return self.maximum / 2 - math.fabs(self.maximum / 2 - x)


if __name__ == '__main__':
    # Formulate a problem with a 2D hill function and a single maximum value.
    hill_x = 0
    hill_max = 0
    sa_x = 0
    sa_max = 0

    for x in range (50):
        maximum = 30.0
        initial = randrange(0, maximum)
        p = AbsVariant(initial, maximum, delta=2.0)

        # Solve the problem using hill climbing solution
        hstarttime = time.time()

        hill_solution = hill_climbing(p)
        if p.value(hill_solution) > hill_max:
            hill_x = hill_solution
            hill_max = p.value(hill_solution)

        hendtime = time.time()

        # Solve the problem using simulated annealing.
        astarttime = time.time()

        annealing_solution = simulated_annealing(
            p,
            exp_schedule(k=20, lam=0.005, limit=1000)
        )
        if p.value(annealing_solution) > sa_max:
            sa_x = annealing_solution
            sa_max = p.value(annealing_solution)
        aendtime = time.time()

print('Hill-climbing solution       x: ' + str(hill_x)
      + '\tvalue: ' + str(p.value(hill_max))
      + '\nhill_climbing time: ' + str(hendtime - hstarttime)
      )

print('Simulated annealing solution x: ' + str(sa_x)
      + '\tvalue: ' + str(p.value(sa_max))
      + '\nSimulated annealing time: ' + str(aendtime - astarttime)
      )

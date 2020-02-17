"""
This module implements local search on a simple sine function variant.
@author: kvlinden
@version 6feb2013
"""

from search import Problem, hill_climbing, simulated_annealing, \
    exp_schedule, genetic_search
from random import randrange
import math
from statistics import mean 


class SineVariant(Problem):
    """
    State: x value for the sin function variant f(x)
    Move: a new x value delta steps from the current x (in both directions) 
    """
    
    def __init__(self, initial,delta=0.001):
        self.initial = initial
        self.delta = delta
        
    def actions(self, state):
        return [state + self.delta, state - self.delta]
    
    def result(self, stateIgnored, x):
        return x
    
    def value(self, x):
        return abs(x * math.sin(x))


if __name__ == '__main__':

    # Formulate a problem with a 2D hill function and a global maximum and many local minimums.
    
    
    list_SA = []
    list_HC = []
    maximum = 30

    runs = 1000 # number of trials

    for i in range(runs):
        
        initial = randrange(0, maximum)

        p = SineVariant(initial, delta= 10)
        
        annealing_solution = simulated_annealing(
            p,
            exp_schedule(k=20, lam=0.005, limit=1000)
        )

        hill_solution = hill_climbing(p)

        # run and store the results using simulated annealing
        list_SA.append( {
            'initial': {'x': p.initial, 'value': p.value(initial) }, 
            'final': {'x': annealing_solution, 'value': p.value(annealing_solution) } 
            })
        
        # run and store the results using hill-climbing
        list_HC.append({
            'initial': {'x': p.initial, 'value': p.value(initial)}, 
            'final': {'x': hill_solution, 'value': p.value(hill_solution) }
            })

    # calculate and store the max and averages for the the two algorithms    
    SA = { 'max': max(trial['final']['value'] for trial in list_SA), 
        'avg':  mean(trial['final']['value'] for trial in list_SA) }
    HC = { 'max': max(trial['final']['value'] for trial in list_HC), 
        'avg':  mean(trial['final']['value'] for trial in list_HC) }
    
    #Display results
    print("After", runs, "trials, Hill Climbing finished with a max of:", HC['max'], 
        "and an average of", HC['avg'], '.\n Simulated Annealing finished with a max of:', SA['max'], 
        "and an average of", SA['avg'])
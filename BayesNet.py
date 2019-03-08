'''
This module implements the Bayesian network shown in Exercise 5.3 of lab05
It's taken from the AIMA Python code.

@author: kvlinden, and ss63
@version updated on March 1, 2019
'''

from probability import BayesNet, enumeration_ask, elimination_ask

# Utility variables
T, F = True, False

cloudy = BayesNet([
    ('Cloudy', '', 0.5),
    ('Sprinkler', 'Cloudy', {T: 0.10, F: 0.50}),
    ('Rain', 'Cloudy', {T: 0.80, F: 0.20}),
    ('WetGrass', 'Sprinkler Rain', {(T, T): 0.99, (T, F):0.90, (F, T):0.90, (F, F):0.00})
    ])

print("\nP(Cloudy):")
print( enumeration_ask('Cloudy', dict(), cloudy).show_approx())

print("\nP(Sprinkler|cloudy):")
print( enumeration_ask('Sprinkler', dict(Cloudy = T), cloudy).show_approx())

print("\nP(Cloudy|sprinkler and -rain):")
print( enumeration_ask('Cloudy', dict(Sprinkler = T, Rain = F), cloudy).show_approx())

print("\nP(Wet Grass|cloudy and sprinkler and rain):")
print(enumeration_ask('WetGrass', dict(Cloudy = T, Sprinkler = T, Rain = T), cloudy).show_approx())

print("\nP(Cloudy|- wet grass):")
print( enumeration_ask('Cloudy', dict(WetGrass = F), cloudy).show_approx())
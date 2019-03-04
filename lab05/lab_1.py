'''
This module implements the Bayesian network shown in the text, Figure 14.2.
It's taken from the AIMA Python code.

@author: kvlinden, and ss63
@version updated on March 1, 2019
'''

from probability import BayesNet, enumeration_ask, elimination_ask

# Utility variables
T, F = True, False

# From AIMA code (probability.py) - Fig. 14.2 - burglary example
burglary = BayesNet([
    ('Burglary', '', 0.001),
    ('Earthquake', '', 0.002),
    ('Alarm', 'Burglary Earthquake', {(T, T): 0.95, (T, F): 0.94, (F, T): 0.29, (F, F): 0.001}),
    ('JohnCalls', 'Alarm', {T: 0.90, F: 0.05}),
    ('MaryCalls', 'Alarm', {T: 0.70, F: 0.01})
    ])

#Compute probabilities using enumeration-ask algorithm (I decided to not include the elimination_ask results because they were the same).

# Compute P(Alarm | burglary and -earthquake)
# for this problem, I just referenced the table where it was hard-coded.
print("\nP(Alarm | burglary and no earthquake):")
print(enumeration_ask('Alarm', dict(Burglary=T, Earthquake=F), burglary).show_approx())


#Compute P(John | burglary and -earthquake)
# this problem takes into account that John may call with or without the alarm going off, and the probability of the alarm going off despite the chances of an earthquake not occuring
print("\nP(John | burglary and no earthquake):")
print(enumeration_ask('\nJohnCalls', dict(Burglary=T, Earthquake=F), burglary).show_approx())


#Compute P(Burglary | alarm)
# this problem takes into account the probability of an alarm going off from a burlgary and events that weren't a burglary (i.e earthquake, or some other triggering event).
print("\nP(Burglary | alarm):")
print(enumeration_ask('Burglary', dict(Alarm=T), burglary).show_approx())


#Compute P(Burglary | John and Mary)
#this problem considers the bulgaries in the context of both John and Mary calling, but that burgalries can occur even without the calls
print("\nP(Alarm | John and Mary called):")
print(enumeration_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())

'''
This module implements the Bayesian network shown in Exercise 5.3 of lab05
It's taken from the AIMA Python code.

@author: kvlinden, and ss63
@version updated on March 1, 2019
'''

from probability import BayesNet, enumeration_ask, elimination_ask

# Utility variables
T, F = True, False

# From AIMA code (probability.py) - Fig. 14.2 - burglary example
happiness = BayesNet([
    ('Sunny', '', 0.7),
    ('Raise', '', 0.01),
    ('Happy', 'Sunny Raise', {(T, T): 1.0, (T, F): 0.7, (F, T): 0.9, (F, F): 0.1})
    ])

# Compute P(Raise | sunny)
print("\nP(Raise | sunny):")
print("enumeration_ask results: " + enumeration_ask('Raise', dict(Sunny=T), happiness).show_approx())
print("elimination_ask results: " + elimination_ask('Raise', dict(Sunny=T), happiness).show_approx())

'''
The probability of getting a raise given that it was sunny would actually just be the probability of 
getting a raise (0.01), because raise is independent of the weather according to the diagram. 
'''

# Compute P(Raise | sunny and happy)
print("\nP(Raise | sunny and happy):")
print("enumeration_ask results: " + enumeration_ask('Raise', dict(Sunny=T, Happy=T), happiness).show_approx())
print("elimination_ask results: " + elimination_ask('Raise', dict(Test1=T, Test2=T), happiness).show_approx())

'''
The actual probability that you get a raise given that it is sunny outside and you are happy is not intuitive.
One would be led to believe that if you're both happy and the weather is nice, then you're able to be efficient 
in your work, therefore increasing the probability of a raise. However, the influence diagram is measuring happiness
based on raise and weather. Just like in the previous problem, the raise and sunny are independent of each other, but 
the probability of raise is affected by happiness which increases the probability of raise (in comparison to the previous
problem).
'''

# Compute P(Raise | happy).
print("\nP(Raise | happy): ")
print(enumeration_ask('Raise', dict(Happy=T), happiness).show_approx())
print(elimination_ask('Raise', dict(Happy=T), happiness).show_approx())

'''
The results make sense because happiness does not affect a raise as much as a raise affecting happiness. In comparison to 
the precious probability problem, you no longer happy sunny being factored in (sunny is independent of a raise), in this 
problem you have a mildly higher probability of a raise that is purely due to the condition of being happy).
'''

# Compute P(Raise | happy and -sunny)
print("\nP(Raise | happy and not sunny): ")
print("enumeration_ask results: " + enumeration_ask('Raise', dict(Happy=T, Sunny =F), happiness).show_approx())
print("elimination_ask results: " + elimination_ask('Raise', dict(Happy=T, Sunny =F), happiness).show_approx())

'''
This problem is also complex to understand intuitively. But this problem increases the probability of a raise  
because, we are eliminating one of the causes of happiness (sunny),and therefore raise is only depending on happy. 
'''
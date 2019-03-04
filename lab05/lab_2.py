'''
This module implements the Bayesian network shown Exercise 5.2 of lab05
It's taken from the AIMA Python code.

@author: kvlinden, and ss63
@date March 1, 2019
'''

from probability import BayesNet, enumeration_ask, elimination_ask

# Utility variables
T, F = True, False

# From AIMA code (probability.py) - Fig. 14.2 - burglary example
cancer = BayesNet([
    ('Cancer', '', 0.01),
    ('Test1', 'Cancer', {T: 0.90, F: 0.2}),
    ('Test2', 'Cancer', {T: 0.90, F: 0.2})
    ])

# Compute P(Cancer | positive results on both tests)
print("\nP(Cancer | positive results on both tests):")
print("enumeration_ask results: " + enumeration_ask('Cancer', dict(Test1=T, Test2=T), cancer).show_approx())
print("elimination_ask results:" + elimination_ask('Cancer', dict(Test1=T, Test2=T), cancer).show_approx())

# Compute P(Cancer | test1 and -test2)
print("\nP(Cancer | test 1 is positive and test 2 is negative):")
print("enumeration_ask results: " + enumeration_ask('Cancer', dict(Test1=T, Test2=F), cancer).show_approx())
print("elimination_ask results: " + elimination_ask('Cancer', dict(Test1=T, Test2=F), cancer).show_approx())

'''
While intuitively I am led to believe that if 2 credible tests came back positive, a person has a very high chance of 
having cancer. However, because the prevalence of cancer is very low to begin with (0.01), that needs to be factored in
with the tests to calculate the probability of having cancer. Therefore, the results, after some analyzing, make sense. 
After you start to understand how the 0.01 is related to the probability of cancer it makes more sense that the probability
decreases to an even lower number of 0.0057 when one of the two tests return negative. 
In epidemiology, I am learning about the thresholds (based on several components such as the prevalence of the disease 
and population size) for tests that decide their credibility. Therefore, a test with seemingly high specificity and 
sensitivity should not be judged merely on their high or low percentages. 
'''
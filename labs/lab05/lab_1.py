'''
This module implements the Bayesian network shown in the text, Figure 14.2.
It's taken from the AIMA Python code.

@author: kvlinden
@version Jan 2, 2013
'''

from probability import BayesNet, enumeration_ask, elimination_ask, gibbs_ask, rejection_sampling, likelihood_weighting

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



#1) Compute P(Alarm | burglary ∧ ¬earthquake)
print(enumeration_ask('Alarm', dict(Burglary=T, Earthquake=F), burglary).show_approx())

#2) Compute P(John | burglary ∧ ¬earthquake).
print(enumeration_ask('JohnCalls', dict(Burglary=T, Earthquake=F), burglary).show_approx())

#3) Compute P(Burglary | alarm)
print(enumeration_ask('Burglary', dict(Alarm=T), burglary).show_approx())

#4) P(Burglary | john ∧ mary)

print("Enumeration ask Method:")
print(enumeration_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx(), '\n\n')

print("Rejection Sampling:")
print(elimination_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx(), '\n\n')

print("gibbs Sampling:")
print(gibbs_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx(), '\n\n')

'''
These algortihms generate different resutls because they use
random sampling. They aim reduce the run time by using sampling
to generate a model that apporixmates the distribution as opposed
to calculating all the values. They succeed in running faster
and also generate accurate models
'''
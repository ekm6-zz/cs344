'''
This module implements the Bayesian network shown in the text, Figure 14.2.
It's taken from the AIMA Python code.

@author: kvlinden
@version Jan 2, 2013
'''

from probability import BayesNet, enumeration_ask, elimination_ask, gibbs_ask

# Utility variables
T, F = True, False

# From AIMA code (probability.py) - Fig. 14.2 - cancer example
cancer = BayesNet([
    ('Cancer', '', 0.01),
    ('Test1', 'Cancer', {T: 0.90, F: 0.20}),
    ('Test2', 'Cancer', {T: 0.90, F: 0.20})
    ])



# Compute P(Cancer | positive results on both tests)
print(enumeration_ask('Cancer', dict(Test1=T, Test2=T), cancer).show_approx())
'''
Does this make sense?:
    Yes, his make sense because the probability of a patient having cancer is so low
    that the the patient more likely to get false positives on both of the tests
Work: 
  Given: 
    P(Cancer) = .01 so P(¬ Cancer) = .99
    P(Test1 | Cancer) = .9 so 
      P(¬Test1 | Cancer) = .1
    P(Test1 | ¬Cancer) = .2 so  
      P(¬Test1 | ¬Cancer) = .8
    P(Test2 | Cancer) = .9 so 
      P(¬Test2 | Cancer) = .1
    P(Test2 | ¬Cancer) = .2 so 
      P(¬Test1 | ¬Cancer) = .8

  Solution:
    P(Cancer | Test1 ^ Test2) = alpha * <P(Cancer) * P(Test1 | Cancer) * P(Test2 | Cancer), P(¬Cancer) * P(Test1 | ¬Cancer), P(Test2 | ¬Cancer)>

    P(Cancer | Test1 ^ Test2) = alpha * <.01 * .9 * .9, .99 * .2 * .2>
    P(Cancer | Test1 ^ Test2) = alpha * <.0081, .0396>
    P(Cancer | Test1 ^ Test2) = <.17, .83>
'''

# Compute P(Cancer | a positive result on test 1, but a negative result on test 2)
print(enumeration_ask('Cancer', dict(Test1=T, Test2=F), cancer).show_approx())
'''
Does this make sense:
    Yes, Especially considering the outcome of the previous scenario. If one of the
    tets comes out negative, there is even a less of a chance of the patient having cancer 
Work: 
  Given: 
      P(Cancer) = .01 so P(¬ Cancer) = .99
      P(Test1 | Cancer) = .9 so 
        P(¬Test1 | Cancer) = .1
      P(Test1 | ¬Cancer) = .2 so  
        P(¬Test1 | ¬Cancer) = .8
      P(Test2 | Cancer) = .9 so 
        P(¬Test2 | Cancer) = .1
      P(Test2 | ¬Cancer) = .2 so 
        P(¬Test1 | ¬Cancer) = .8

    Solution:
      P(Cancer | Test1 ^ ¬Test2) = alpha * <P(Cancer) * P(Test1 | Cancer) * P(¬Test2 | Cancer), P(¬Cancer) * P(Test1 | ¬Cancer), P(¬Test2 | ¬Cancer)>

P(Cancer | Test1 ^ ¬Test2) = alpha * <.01 * .9 * .1, .99 * .2 * .8>
P(Cancer | Test1 ^ ¬Test2) = alpha * <.0009, .1584>
P(Cancer | Test1 ^ ¬Test2) = <.00565, .994>
'''
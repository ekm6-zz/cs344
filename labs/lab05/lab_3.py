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
happiness = BayesNet([
    ('Sunny', '', 0.7),
    ('Raise', '', 0.01),
    ('Happy', 'Sunny Raise', {(T, T): 1.0, (T, F): 0.7, (F, T): 0.9, (F, F): 0.1}),
    ])


# EXERCISE 5.3 A:

#1)Compute P(Raise | sunny)
print(enumeration_ask('Raise', dict(Sunny=T), happiness).show_approx())
'''

Does is make sense: 
    Yes, this shows that a raise is idependent of a whether or not it rained.
    A condition of bayesian networks is that if they don't have an arrow between
    them on a bayesian network graph, then they not not a factor in each other's probablities. In other words, they are independent. 
Work: 
  Given:
    P(Sunny) = .7 
      so P(¬Sunny) = .3
    P(Raise) = .01 
      so P(¬Raise) = .99
      
    P(Happy | Sunny ^ Raise) = 1.0
      so P(¬Happy | Sunny ^ Raise) = .0

    P(Happy | Sunny ^ ¬Raise) =  .7
      so P(¬Happy | Sunny ^ ¬Raise) = .3

    P(Happy | ¬Sunny ^ Raise) =  .9
      so P(¬Happy | ¬Sunny ^ Raise) = .1
    
    P(Happy | ¬Sunny ^ ¬Raise) =  .1
      so P(¬Happy | ¬Sunny ^ ¬Raise) = .9

  Solution:
    P(Raise | Sunny) = alpha * <P(Raise) * P(Sunny), P(¬Raise) * P(Sunny)>
    P(Raise | Sunny) = alpha * P(Sunny) * <.01, .99>
    P(Raise | Sunny) = <.01, .99>
'''


#2) Compute P(Raise | happy ∧ sunny)
print(enumeration_ask('Raise', dict(Happy=T, Sunny=T), happiness).show_approx())
'''

Does is make sense: 
  Yes, There is still a good probability that the person will be happy without
  the raise. However since a raise almost always leads to happiness, the 
  propobability of raise is just a little bit higher when we know that happy
  is true.
Work: 
  Given:
    P(Sunny) = .7 
      so P(¬Sunny) = .3
    P(Raise) = .01 
      so P(¬Raise) = .99
      
    P(Happy | Sunny ^ Raise) = 1.0
      so P(¬Happy | Sunny ^ Raise) = .0

    P(Happy | Sunny ^ ¬Raise) =  .7
      so P(¬Happy | Sunny ^ ¬Raise) = .3

    P(Happy | ¬Sunny ^ Raise) =  .9
      so P(¬Happy | ¬Sunny ^ Raise) = .1
    
    P(Happy | ¬Sunny ^ ¬Raise) =  .1
      so P(¬Happy | ¬Sunny ^ ¬Raise) = .9
  Solution:
    P(Raise | Happy ^ Sunny) = alpha * <P(Happy | Sunny ^ Raise) * P(Sunny) * P(Raise), P(Happy | Sunny ^ ¬Raise) * P(Sunny) * P(¬Raise)>

    P(Raise | Happy ^ Sunny) = alpha * <1.0 * .7 * .01, .7 * .7 * .99>
    P(Raise | Happy ^ Sunny) = <.0142, .986>
'''

# EXERCISE 5.3 B:
#1) Compute P(Raise | happy)
print(enumeration_ask('Raise', dict(Happy=T), happiness).show_approx())
'''

Does is make sense?:
  Yes because a raise almost always leads to happiness. If we know that there
  happy is true, we expect their to be a higher chance that there was a raise.
  The probability of raise on it's own is .01, but it goes up to .0185 when we
  know happy is true.

'''
#2) P(Raise | happy ∧ ¬sunny)
print(enumeration_ask('Raise', dict(Happy=T, Sunny=F), happiness).show_approx())
'''

Does is make sense: 
  Yes, for happy to be true, it's either caused by sunny being true or raise being
  true. In this case, we know sunny is false, so for happy to be true, there is a
  higher chance that raise is true.

'''
'''
lab04

@author: Enoch Mwesigwa
@version March 1, 2020
'''

from probability import JointProbDist, enumerate_joint_ask

#### EXERCISE 4.2A ###

P = JointProbDist(['Toothache', 'Cavity', 'Catch', "Rain"])
T, F = True, False

#  P(rain) = .1            P(¬ rain) = .9
P[T, T, T, T] = 0.0108; P[T, T, T, F] = 0.0972 
P[T, T, F, T] = 0.0012; P[T, T, F, F] = 0.0108
P[F, T, T, T] = 0.0072; P[F, T, T, F] = 0.0648
P[F, T, F, T] = 0.0008; P[F, T, F, F] = 0.0072
P[T, F, T, T] = 0.0016; P[T, F, T, F] = 0.0144 
P[T, F, F, T] = 0.0064; P[T, F, F, F] = 0.0576
P[F, F, T, T] = 0.0144; P[F, F, T, F] = 0.1296 
P[F, F, F, T] = 0.0576; P[F, F, F, F] = 0.5184

''' 
    i. 
        There twice as many entries as before: 16

    ii. 
        Yes they do. A Probability distribution tables display every possible
        outcome with the probability of it occuring. By that definition, these
        tables must always sum up to one. Each cell represents the likelihood
        of that event occuring with respect to all the other possible outcomes.
        "All possible outcomes" must always add up to one

    iii. 
        The JointProbDist class just accepts variables. It doesn't specify that
        they have to be boolean values. So yes, anything that can be used as a
        a variable can be be used.

    iv.
        Yes, It was easier to set it up this way. I simply multiplied the P(rain)
        and P(¬rain) where appropriate (when rain is true or false)

'''


#### EXERCISE 4.2B ###

#    P( Toothache | Rain ) = (.0108 +.0012 + .0016 + .0064) / (.1) = .2 
#         --> true: .2; false: .8

# Compute P(Cavity|Catch=T)  (see the text, page 493).
PC = enumerate_joint_ask('Toothache', {'Rain': T}, P)
print(PC.show_approx())
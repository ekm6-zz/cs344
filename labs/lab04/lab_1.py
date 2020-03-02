'''
lab04

@author: Enoch Mwesigwa
@version March 1, 2020
'''

from probability import JointProbDist, enumerate_joint_ask

#### EXERCISE 4.1B ###

# P( Cavity | catch ) = (.108 +.072) / (.108 + .016 + .072 + .144) = .0529


# The Joint Probability Distribution Fig. 13.3 (from AIMA Python)
P = JointProbDist(['Toothache', 'Cavity', 'Catch'])
T, F = True, False
P[T, T, T] = 0.108; P[T, T, F] = 0.012
P[F, T, T] = 0.072; P[F, T, F] = 0.008
P[T, F, T] = 0.016; P[T, F, F] = 0.064
P[F, F, T] = 0.144; P[F, F, F] = 0.576

# Compute P(Cavity|Catch=T)  (see the text, page 493).
PC = enumerate_joint_ask('Cavity', {'Catch': T}, P)
print(PC.show_approx())

#### EXERCISE 4.1C ###

# P(coin1 | coin2=heads ) = (.5 * .5) / .5 = .5 ---> (heads = .5 and tails = .5)
# this is as expected flipping coin2 is independent of flipping coin1

P = JointProbDist(['coin1', 'coin2'])
H, T = "Heads", "Tails"

P[H,H]= .25; P[H,T]=.25
P[T,T]=.25; P[T,H]= .25

PC = enumerate_joint_ask('coin2', {'coin1': H}, P)
print(PC.show_approx())


weighs_same(duck, poor_lady).
witch(X) :- burns(X).
burns(X):- wood(X).
wood(X) :- floats(X). 
floats(X) :- weighs_same(duck, X).
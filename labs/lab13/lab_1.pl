%% Exercise %% 1
%% A
%%    i.
directlyIn(katarina, olaga)
directlyIn(olga, natasha)
directlyIn(natasha, irina)
%
in(X,Y) :- directlyIn(X,Y)
in(X,Y) :- directlyIn(X,Y), in(X,Y)

    %% ii.
tran(eins,one).
tran(zwei,two).
tran(drei,three).
tran(vier,four).
tran(fuenf,five).
tran(sechs,six).
tran(sieben,seven).
tran(acht,eight).
tran(neun,nine).

listtran([],[]).
listtran([A|Ta], [B|Tb]) :- tran(A,B), listtran(Ta,Tb).
%
/* 
B
    Prolog doesn not use propositional logic with mathmatical syntax. However,
    it does make use of modes poneus to show show infernce of a head based on
    its body.
    ex)
    someCond is true given that otherCond is true
    
    knowledge base:
        someCond(X) :- otherCond(X)
        otherCond(john)

    Query:    
    ?- someCond(john)

    result:
        yes

*/  

    

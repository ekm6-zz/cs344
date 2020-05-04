%% Exercise %% 1
%% A
%%    i.
        %% 1. Butch is a killer.
killer(butch)
        %% 2. Mia and Marsellus are married.
        married(mia, marsellus)
        %% 3. Zed is dead.
dead(zed)
        %% 4. Marsellus kills everyone who gives Mia a footmassage.
        kills(marsellus, X) :- givesFootMassage(X,mia)
        %% 5. Mia loves everyone who is a good dancer.
        loves(mia, X):- goodDancer(X)
        %% 6. Jules eats anything that is nutritious or tasty.
        eats(jules, X):- nutritious(X), tasty(x)
    %%  I did these by making adjectives and verbs complex terms. I made the subjects
    %%  of the sentences atoms which I passed into the complex terms. I made he words
    %%  "anything" and "everyone" variables.
%
    %% ii.
    %%  staments:
        %% 1. wizard(ron).
        %% 2. hasWand(harry).
        %% 3. quidditchPlayer(harry).
        %% 4. wizard(X):-  hasBroom(X),  hasWand(X).
        %% 5. hasBroom(X):-  quidditchPlayer(X).
    %%  questions
        %% 1. wizard(ron).
        %%    prolog looks at statement %% 1
        %% 2. witch(ron).
        %%    prolog has "no"knowledge of witch() or (witch/1) so returns "no". 
        %% 3. wizard(hermione).
        %%    prolog has "no"knowldege about hermoione, so returns "no".
        %%    prolog can not make deduction with missing information.
        %% 4. witch(hermione).
        %%    prolog has "no"knowldege about hermoine or witch() or (witch/1), so returns "no"
        %% 5. wizard(harry).
        %%    harry returns yes to both conditions of being a wizard. He is defined
        %%    as having a wand and prolog looks staemnt 5, which then makes it look
        %%    at staetment 3, which returns yes which leads to deduce that stament 5
        %%    is true, which means that this querry returns true. 
        %%    Therefore prolog returns "no"
        %% 6. wizard(Y).
        %%    This gets all the names that output "yes" to being a wizard. in this
        %% 7. witch(Y).
        %%    since prolog has "no"knowledge of witch() or (witch/1), it returns no.
%
/* 
B
    Prolog doesn not use propositional logic with mathmatical syntax. However,
    it does make use of modes poneus to show show infernce of a had based on
    its body.
    ex)
    someCond is true fiven that otherCond is true
    someCond(X) :- otherCond(X)

C
    These horn clauses are concise and practical to use for programming. However,
    they don not have the same historical precedent and familiarity of traditional
    propositional logic

D
    Yes, prolog allows the user to utilize the terminal to make queries
    (to the knowledge base) which functions as an ASK ask operations. Users can also program the
    knowldege base which fuctions as a TELL operation
*/  

    

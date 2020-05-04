%%  Exercise %% 2
%% A From LPN!
    %% i. questions 
        %% 1. unifies
        %% 2. does not unify
        %% 8. unifies; X= bread
        %% 9. unifies; Y= bread, X= sausage
        %% 14. does not unify
    %% ii.
            /*
            Unification rules:
            1. If term1 and term2 are constants, then term1 and term2 unify if and only
            if they are the same atom, or the same number.
            
            2. If term1 is a variable and term2 is any type of term, then term1 and term2
            unify, and term1 is instantiated to term2. And vice versa
            
            3. If term1 and term2 are complex terms, then they unify if and only if:
                -They have the same functor and arity
                -all their corresponding arguments unify,
                -the variable instantiations are compatible. 
            */

            /*
            Reasoning:
                Prolog uses unification in its querries as it is looking for
                possible solutions. It swaps in the atom that it is testing
                against the functors conditions. If one doesn"t match, it bacK0
                tracks until it can try differemt values.
            /*
wizard/1
house_elf/1 
house_elf(dobby).
witch(hermione).
witch('MGonagall').
witch(rita_skeeter).
magic(X):-  house_elf(X).
magic(X):-  wizard(X).
magic(X):-  witch(X).
/*     Questions:
        1-  magic(house_elf).
            Does not complete, house_elf is a complex term, that has arity 1.
        2-  wizard(harry).
                no, wizard() is not included in knowledge base, but if wizard/1
                was completed, it would complete.
        3-  magic(wizard).
                no, wizard is a complex term of arity 1, not a atom or variable
        4-  magic('McGonagall').
                does complete
        5-  magic(Hermione).
            yes, Hermione is a variable, so it'll look dor any atom that satisfies
            the magic() condition. in this case, dobby.  
*/

%% B Does inference in propositional logic use unification? Why or why not?
/*
    Not really. Propositional logic doesn"t have the same uses as prolog. Prolog
    is used differently than propositional logic. Propopositional logic is not
    used for queries< so it has no need for the back tracking search that is used
    by prolog, in which it makes use of unification.
*/

%% C Does Prolog inferencing use resolution? Why or why not?
/*
    Prolog makes heavy use of resolution in it"s reasoning. Resolution is 
    defined as inference operation where resolving two clauses creates a new one.
    Infact, it is crucial to it"s reasoning. This is likely becuase it is computaionaly,
    cheaper.

    The following:
        stuff(X) :- st(X), uff(X)
        realStuff(X) :- stuff(X), more(X), 
    Is better represented:
        realstuff(X) :- st(X), uff(X), more(x)
    and is what is done by prolog

    
*/
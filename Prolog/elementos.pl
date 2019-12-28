elementos(A,B,[],[]).
elementos(A,B,[X|L1],[X|L2]) :- A<=X, X<=B, elementos(A,B,L1,L2).
elementos(A,B,[X|L1],L2) :- A > X, elementos(A,B,L1,L2).
elementos(A,B,[X|L1],L2) :- X > B, elementos(A,B,L1,L2).

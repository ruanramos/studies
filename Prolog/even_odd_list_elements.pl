/*

first solution:

odd([]).
even([_]).

odd([X,Y|L]) :- odd(L).
even([X,Y|L]) :- even(L).

second solution:
odd([]).
odd([_,_|L]) :- odd(L).
even([_,L]) :- odd(L).

third solution:
odd([]).
odd([_|L]) :- even(L).
even([_|L]) :- odd(L).

*/

odd(L) :- length(L,N), X is N mod 2, X=0.


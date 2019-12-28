female(pam).
female(liz).
female(ann).
female(pat).
male(tom).
male(bob).
male(jim).
parent(pam,bob).
parent(tom,bob).
parent(tom,liz).
parent(bob,ann).
parent(bob,pat).
parent(pat,jim).
father(tom,bob).
father(tom,liz).
father(bob,ann).
father(bob,pat).
mother(pam,bob).
mother(pat,jim).

ancestral(X,Y) :- parent(X,Y).
ancestral(X,Y) :- parent(X,Z), ancestral(Z,Y).

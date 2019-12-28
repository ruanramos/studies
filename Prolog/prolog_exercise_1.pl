/* facts */
progenitor(jose,joao).
progenitor(jose,ana).
progenitor(maria,joao).
progenitor(maria,ana).
progenitor(ana,helena).
progenitor(ana,joana).
progenitor(joao,mario).
progenitor(helena,carlos).
progenitor(mario,carlos).

sex(ana,f).
sex(maria,f).
sex(helena,f).
sex(joana,f).
sex(mario,m).
sex(jose,m).
sex(carlos,m).
sex(joao,m).

m_brother(X,Y) :- progenitor(A,X), progenitor(A,Y), X\==Y, sex(X,m).
f_brother(X,Y) :- progenitor(A,X), progenitor(A,Y), X\==Y, sex(X,f).
m_grandparent(X,Y) :- progenitor(X,A), progenitor(A,Y), sex(X,m).
f_grandparent(X,Y) :- progenitor(X,A), progenitor(A,Y), sex(X,f).

mother(X,Y) :- progenitor(X,Y), sex(X,f).
father(X,Y) :- progenitor(X,Y), sex(X,m).
uncle(X,Y) :- m_brother(X,A), progenitor(A,Y).
aunt(X,Y) :- f_brother(X,A), progenitor(A,Y).


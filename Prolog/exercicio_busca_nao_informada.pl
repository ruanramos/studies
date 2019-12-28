objetivo((2,_)).

acao((J1,J2), encher1, (4,J2)):- J1<4.
acao((J1,J2), encher2, (J1,3)):- J2<3.
acao((J1,J2), esvaziar1, (0,J2)):- J1>0.
acao((J1,J2), esvaziar2, (J1,0)):- J2>0.

acao((J1,J2), passa12, (C,F)):- C is J1-3+J2, F is J2+3-J2, J1+J2>3.
acao((J1,J2), passar12, (0,C)):- C is J1+J2, C=<3.

acao((J1,J2), passar21, (C,F)):- C is J2-4+J1, F is 4-J1, J1+J2>4.
acao((J1,J2), passar21, (C,0)):- C is J1+J2, C=<4.


vizinho(N,FilhosN):- findall(V,acao(N,_,V),FilhosN).



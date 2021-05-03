% probleme 1

chiffre1(X) :- member(X,[0,1,2,3,4,5,6,7,8,9]).

generate1(X1,X2) :- chiffre(X1), chiffre(X2).

test1(X1,X2,X) :- dif(X1,X2), X is X1 + X2.
     
solve1(X1,X2,X) :-
    generate1(X1,X2),
    test1(X1,X2,X).


% probleme 2
couleur(rouge).
couleur(vert).
couleur(bleu).

nationalite(italien).
nationalite(norvegien).
nationalite(espagnol).

generate([1,C1,N1],[2,C2,N2],[3,C3,N3]) :- 
    couleur(C1),couleur(C2),couleur(C3),
    nationalite(N1),nationalite(N2),nationalite(N3).

testCouleur([_,C1,_],[_,C2,_],[_,C3,_]) :- 
    dif(C1,C2), 
    dif(C2,C3), 
    dif(C1,C3).

testNationalite([_,_,N1],[_,_,N2],[_,_,N3]) :- 
    dif(N1,N2), 
    dif(N2,N3), 
    dif(N1,N3).

indice1([[1,rouge,_],[2,_,espagnol],_]).
indice1([_,[2,rouge,_],[3,_,espagnol]]).

indice2(L) :- member([_,bleu,norvegien],L).

indice3([_,[2,_,italien],_]).

tests(M1,M2,M3) :-
    testCouleur(M1,M2,M3),
    testNationalite(M1,M2,M3),
    indice1([M1,M2,M3]),
    indice2([M1,M2,M3]),
    indice3([M1,M2,M3]).
    
solve([M1,M2,M3]) :-
    generate(M1,M2,M3),
	tests(M1,M2,M3).


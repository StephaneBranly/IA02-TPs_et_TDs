% Mastermind
%
% UTC - IA02
% Stéphane BRANLY
%

%nBienPlace(+Code1, +Code2, -BP) donnant le nombre de couleurs bien placees
nBienPlace([], [], 0). % condition de fin
nBienPlace([H|R1], [H|R2], BP) :- nBienPlace(R1,R2,BPupd), BP is  BPupd + 1. % cas ou l'element est bien place
nBienPlace([T1|R1], [T2|R2], BP) :- dif(T1,T2), nBienPlace(R1,R2,BP). % cas ou l'element est mal place

% nBienPlace([1,2,2],[1,4,2],X).


%longueur(+L, -N) indiquant la longueur d'une liste
longueur([],0). % condition de fin
longueur([_|R],N) :- longueur(R,Nbis), N is Nbis + 1. % incrementation compteur

% longueur([1,2,3,4,3],X).


%gagne(+Code1, +Code2) indiquant si le joueur a gagne (code1=code2)
gagne(Code1, Code2) :- nBienPlace(Code1,Code2,A), longueur(Code1,B), A=B.

% gagne([1,2,3,4],[1,2,3,4]).
% true 
% gagne([1,3,2,4],[1,2,3,4]).
% false


%element(+E, +L) indiquant si l'element E est dans L
element(_, []) :- fail. % condition de fin
element(E,[E|_]). % element present
element(E,[H|R]) :- E \= H, element(E,R). % element non present, analyse de la suite

% element(1,[4,57,9,11,9]).
% false
% element(1,[4,57,9,1,9]).
% true


%enleve(+E, +L1, -L2) construisant L2 a partir de L1 en retirant le premier element E
enleve(_, [], []). % condition de fin
enleve(T, [T|R], R). % cas ou l'on retire l'element
enleve(E, [T|R], L2) :- dif(E,T), enleve(E,R,L2bis), L2 = [T|L2bis]. % cas ou l'on continue

% enleve(1,[3,4,65,78],X).
% [3, 4, 65, 78]
% enleve(1,[3,4,65,78,1],X).
% [3, 4, 65, 78]
% enleve(1,[3,4,1,65,78,1],X).
% [3, 4, 65, 78, 1]


%enleveBP(+Code1, +Code2, -Code1Bis, -Code2Bis) retirant les elements bien places entre code1 et code2
enleveBP([], [], [], []). % condition de fin
enleveBP([T|R1], [T|R2], Code1Bis,Code2Bis) :- enleveBP(R1,R2,Code1Bis,Code2Bis). % cas ou l'element est bien place
enleveBP([T1|R1], [T2|R2], Code1Bis,Code2Bis) :- % cas ou l'element est mal place
    dif(T1,T2), 
    enleveBP(R1,R2,Code1Ter,Code2Ter), 
    Code1Bis = [T1|Code1Ter], 
    Code2Bis = [T2|Code2Ter].

% enleveBP([1,2,3,4,5,6], [1,2,5,4,3,4], Code1Bis, Code2Bis).


%nMalPlaces(+Code1, +Code2, -MP) donnant le nombre d'elements mal places
nMalPlacesAux([], _, 0). % condition de fin1
nMalPlacesAux(_, [], 0). % condition de fin2
nMalPlacesAux([T1|R1], Code2, N) :- % cas ou l'element est mal place (existe dans la liste Code2)
	element(T1, Code2),
	enleve(T1, Code2, Code2Bis),
	nMalPlacesAux(R1, Code2Bis, N2),
	N is N2 + 1.
nMalPlacesAux([T1|R1], Code2, N) :- % cas ou l'element n'est pas reference dans la liste Code2
	\+ element(T1, Code2),
	nMalPlacesAux(R1, Code2, N).

% PS : il faut garder en tete que : 
% - dans nMalPlacesAux, les elements biens places ne sont pas presents
% - que la liste Code1 est compose d'elements uniques (n'apparaissent qu'une seule fois)
% => on parcours la liste Code1, si un element de Code1 est present dans Code2, il est forcement mal place
    
nMalPlaces([], [], 0). % condition d'arret
nMalPlaces(Code1,Code2,MP) :-
    enleveBP(Code1,Code2,Code1Bis,Code2Bis),
    nMalPlacesAux(Code1Bis,Code2Bis,MP).
    
% nMalPlaces([1,2,3,4], [1,3,2,3], MP).


%codeur(+M, +N, -Code) generant un code de taille N base sur M couleurs
codeur(_, 0, []). % condition de fin
codeur(M, N, [Number | Suit]) :- X is M + 1, random(1, X, Number), Nb is N - 1, codeur(M,Nb,Suit).


% jouons(+M, +N, +Max) permettant de jouer au Mastermind avec un code de taille N compose d'un maximum de M couleurs, doit etre resolu en max essais.
jouons(M, N, Max) :-
    codeur(M, N, Code),
    essai(Code,Max).

perdu(Code) :- write("Vous avez perdu..."), nl, 
    write("Le code etait : "),
    write(Code),nl,
    fail.

gagne(Code) :-  write("Vous avez gagne !"), nl, 
    write(Code),nl.

verification(Code, _, 0) :- perdu(Code), fail.
verification(Code, Proposition, Essais) :- 
    dif(Code,Proposition), 
    NewNum is Essais - 1, 
	nMalPlaces(Code, Proposition, MP),
    enleveBP(Code,Proposition,BPrmList,_),
    longueur(BPrmList,L1),
    longueur(Code,L2),
    BP is L2 - L1,
	write("BP: "), write(BP), write(" / MP: "), write(MP), nl, nl,
    essai(Code, NewNum).
verification(Code, Code, _) :- gagne(Code).

essai(Code, 0) :- perdu(Code).
essai(Code,Essais) :-
    write("Il reste "), write(Essais), write(" coup(s)."), nl,
	write("Donner un code : "), nl, read(Proposition), nl,
    verification(Code, Proposition, Essais).
    

    

    

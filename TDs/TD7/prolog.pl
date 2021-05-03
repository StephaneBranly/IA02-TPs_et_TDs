swish :

pere(X,Y) :- homme(X), parent(X, Y).
mere(X, Y) :- femme(X), parent(X, Y).
epoux(X, Y) :- homme(X), couple(X, Y) ; homme(X), couple(Y, X).
epouse(X, Y) :- femme(X), couple(X, Y) ; femme(X), couple(Y, X).
couple(X, Y) :- couple(Y, X). % pas possible car on efface les règles, ça vient des primitives
fils(X, Y) :- homme(X), parent(Y, X).
fille(X, Y) :- femme(X), parent(Y, X).
enfant(X, Y) :- parent(Y, X).
%en règle général, on va de X vers Y
grandPere(X, Y) :- pere(X, Z), parent(Z, Y).
grandMere(X, Y) :- mere(X, Z), parent(Z, Y).
grandParent(X, Y) :- grandPere(X, Y) ; grandMere(X, Y).
petitFils(X, Y) :- homme(X), grandParent(Y, X).
petiteFille(X, Y) :- femme(X), grandParent(Y, X).

memePere(X, Y) :- enfant(X, Z), enfant(Y, Z), homme(Z), X/Y.
memeMere(X, Y) :- enfant(X, Z), enfant(Y, Z), femme(Z), X/Y.
memeParent(X, Y) :- parent(Z, X), parent(Z, Y).
memeParents(X, Y) :- memePere(X, Y), memeMere(X, Y).
frere(X, Y) :- homme(X), memeParents(X, Y).
soeur(X, Y) :- femme(X), memeParents(X, Y).
demiFrere(X, Y) :- homme(X), memeParent(X, Y), \+memeParents(X, Y).
demiSoeur(X, Y) :- femme(X), memeParent(X, Y), \+memeParents(X, Y).
oncle(X, Y) :- frere(X, Z), parent(Z, Y) ; demiFrere(X, Z), parent(Z, Y) ; epoux(X, Z), soeur(Z, T), parent(T, Y) ; epoux(X, Z), frere(Z, T), parent(T, Y).
tante(X, Y) :- soeur(X, Z), parent(Z, Y) ; demieSoeur(X, Z), parent(Z, Y) ; epouse(X, Z), soeur(Z, T), parent(T, Y) ; epouse(X, Z), frere(Z, T), parent(T, Y).
neveu(X, Y) :- homme(X), oncle(Y, X) ; homme(X), tante(Y, X).
niece(X, Y) :- femme(X), oncle(Y, X) ; femme(X), tante(Y, X).
cousin(X, Y) :- homme(X), oncle(X, Z), pere(Z, Y) ; homme(X), tante(X, Z), mere(Z, Y).
cousine(X, Y) :- femme(X), oncle(X, Z), pere(Z, Y) ; femme(X), tante(X, Z), mere(Z, Y).
gendre(X, Y) :- epoux(X, Z), enfant(Z, Y).
bru(X, Y) :- epouse(X, Z), enfant(Z, Y).

maratre(X, Y) :- epouse(X, Z), parent(Z, Y), \+mere(X, Y).
belleMere(X, Y) :- maratre(X, Y) ; femme(X), bru(Y, X) ; femme(X), gendre(Y, X).
paratre(X, Y) :- epoux(X, Z), parent(Z, Y), \+pere(X, Y).
beauPere(X, Y) :- paratre(X, Y) ;  pere(X, Z), couple(Z, Y) ; pere(X, Z), couple(Y, Z).

ascendant(X, Y) :- parent(X, Z), ascendant(Z, Y) ; parent(X, Y).
descendant(X, Y) :- ascendant(Y, X).
lignee(X, Y) :- ascendant(X, Y) ; descendant(X, Y).
parente(X, Y) :- descedant(X, Z), descendnat(Y, Z), X/Y.

femme(harmonie).
femme(agave).
femme(semele).
femme(eurydice).
femme(jocaste).
femme(antigone).
femme(ismene).

homme(cadmos).
homme(polydore).
homme(echion).
homme(zeus).
homme(dionysos).
homme(penthee).
homme(labdacos).
homme(laios).
homme(oedipe).
homme(hemon).
homme(eteocle).
homme(polynice).
homme(menecee)

couple(cadmos, harmonie).
couple(semele, zeus).
couple(agave, echion).
couple(laios, jocaste).
couple(creon, eurydice).
couple(oedipe, jocaste).

parent(cadmos, polydore).
parent(cadmos, echion).
parent(cadmos semele).
parent(harmonie, polydore).
parent(harmonie, echion).
parent(harmonie, semele).
parent(menecee, jocaste).
parent(menecee, creon).
parent(laios, oedipe).
parent(jocaste, oedipe).
parent(oedipe, eteocle).
parent(oedipe, polynice).
parent(oedipe, antigone).
parent(oedipe, ismene).
parent(jocaste, eteocle).
parent(jocaste, polynice).
parent(jocaste, antigone).
parent(jocaste, ismene).

?- gendre(X, harmonie)

?- mere(jocaste, oedipe)



%X/Y = dif(X, T)


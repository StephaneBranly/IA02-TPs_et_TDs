# **************************************************************************************************** #
#                                                                                                      #
#                                                                 :::    ::: :::::::::::  ::::::::     #
#    main.py                                                      :+:    :+:     :+:     :+:    :+:    #
#                                                                 +:+    +:+     +:+     +:+           #
#    By: branlyst <stephane.branly@etu.utc.fr>                    +:+    +:+     +:+     +:+           #
#                                                                 +#+    +:+     +#+     +#+           #
#    Created: 2021/03/22 11:02:26 by branlyst                     +#+    +:+     +#+     +#+           #
#    Updated: 2021/03/22 11:02:26 by branlyst                     +#+    +#+     +#+     +#+           #
#                                                                 #+#    #+#     #+#     #+#    #+#    #
#                                                                  ########      ###      ########     #
#                                                                                                      #
# **************************************************************************************************** #

######## IA02 ## TP1 ## BRANLY STEPHANE ########

#### QUESTION 1 ####

#decomp(n: int, nb_bits: int) -> List[bool] qui, étant donné un nombren, calcule la décomposition binaire en nb_bits de n. 
#L’ordre des bits (croissant ou décroissant) est sans importance.

def decomp(n: int, nb_bits: int):
    liste = []
    for i in range (nb_bits):
        liste.append(n % 2 != 0)
        n = n//2
    return liste[::-1]


print(str(decomp(5,4)))


#### QUESTION 2 ####

#interpretation(["A", "B", "C"],[True, True, False]){"A": True, "B": True, "C": False}
def interpretation(voc, vals):
    dic = dict()
    for i in range(len(voc)):
        dic[voc[i]] = vals[i]
    return dic

print(str(interpretation(["A", "B", "C"],[True, True, False])))


#### QUESTION 3 ####

def genInterpretations(voc):
    for i in range(2**len(voc)):
         dec = decomp(i,len(voc))
         yield(interpretation(voc,dec))

g = genInterpretations(["A", "B", "C"])
print(next(g))
for i in genInterpretations(["toto", "tutu"]):
    print(i)


#### QUESTION 4 ####

#valuate(formula: str, interpretation: Dict[str, bool]) -> bool
def valuate(formula, interpretation):
    return eval(formula,interpretation)


#### QUESTION 5 ####

#formule : (A or B) and not(C)+---+---+---+-------+| A | B | C | eval. |+---+---+---+-------+| F | F | F |   F   || T | F | F |   T   || F | T | F |   T   || T | T | F |   T   || F | F | T |   F   || T | F | T |   F   || F | T | T |   F   || T | T | T |   F   |+---+---+---+-------+
def table(formula, voc):
    print("formule : "+formula)
    separation = ""
    line = ""
    line2 = ""
    for i in range(len(voc)):
        separation = separation + "+---"
        line = line + "| "+voc[i]+" "
    separation = separation + "+-------+"
    line = line + "| eval. |"
    print(separation)
    print(line)
    print(separation)
    for i in genInterpretations(voc):
        line2 = line
        for v in voc:
            if i[v]:
                line2 = line2.replace(v,"T")
            else:
                line2 = line2.replace(v,"F")
        if(valuate(formula, i)):
            line2 = line2.replace("eval.","  T  ")
        else:
            line2 = line2.replace("eval.","  F  ")
        print(line2)
    print(separation)

table("(A or B) and not(C)", ["A", "B", "C"])

exp1 = "(A or B) and C"
exp2 = "C"
voc = ["A","B","C"]


#### QUESTION 6 ####

def isValid(f,voc):
    for i in genInterpretations(voc):
        if not valuate(f,i):
            return False
    return True

def isContr(f,voc):
    for i in genInterpretations(voc):
        if valuate(f,i):
            return False
    return True

def isConti(f,voc):
    return (not isContr(f, voc) and not isValid(f,voc))

print("Valid")
print(isValid(exp1,voc))

#### QUESTION 7 ####

def isCons(f1, f2, voc):
    genVoc = genInterpretations(voc)
    for i in genVoc:
         if(valuate(f1,i) and not valuate(f2,i)):
              return False
    return True

print(isCons(exp1,exp2,voc))

######## IA02 ## TP1 ## BRANLY STEPHANE ########

#### QUESTION 2 ####

#decomp(n: int, nb_bits: int) -> List[bool] qui, étant donné un nombren, calcule la décomposition binaire en nb_bits de n. 
#L’ordre des bits (croissant oudécroissant) est sans importance.

def decomp(n: int, nb_bits: int):
    liste = []
    copy = n
    for i in range (nb_bits):
        r = pow(2,nb_bits-i-1)
        if(copy>=r):
            copy = copy-r
            liste.append(True)
        else:
            liste.append(False)
    return liste


print(str(decomp(5,4)))

#### QUESTION 1 ####
#interpretation(["A", "B", "C"],[True, True, False]){"A": True, "B": True, "C": False}
def interpretation(voc, vals):
    dic = dict()
    for i in range(len(voc)):
        dic[voc[i]] = vals[i]
    return dic

print(str(interpretation(["A", "B", "C"],[True, True, False])))

#genInterpretations(voc: List[str]) -> Generator[Dict[str, bool], None, None]
# Using the generator pattern (an iterable)
class Generator(object):
    def __init__(self, l):
        self.l = l
        self.cur = 0
        self.size = len(l)

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()

    def next(self):
        if self.cur < self.size:
            self.cur = self.cur + 1
            return self.l[self.cur - 1]
        raise StopIteration()

def genInterpretations(voc):
    gen = []
    dec = []
    for i in range(pow(2,len(voc))):
        dec = decomp(i,len(voc))
        gen.append(interpretation(voc,dec))
    return Generator(gen)

g = genInterpretations(["A", "B", "C"])
print(next(g))
for i in genInterpretations(["toto", "tutu"]):
    print(i)



#valuate(formula: str, interpretation: Dict[str, bool]) -> bool
def valuate(formula:str, interpretation):
    copy = formula
    for voc, value in interpretation.items():
        copy = copy.replace(voc,str(value))
    return eval(copy)

print(valuate("(A or B) and not(C)", {"A": True, "B": False, "C": False}))


#formule : (A or B) and not(C)+---+---+---+-------+| A | B | C | eval. |+---+---+---+-------+| F | F | F |   F   || T | F | F |   T   || F | T | F |   T   || T | T | F |   T   || F | F | T |   F   || T | F | T |   F   || F | T | T |   F   || T | T | T |   F   |+---+---+---+-------+
def table(formula:str, voc):
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

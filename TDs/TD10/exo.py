# ************************************************************************************************************************* #
#   UTC Header                                                                                                              #
#                                                         ::::::::::::::::::::       :::    ::: :::::::::::  ::::::::       #
#      exo.py                                             ::::::::::::::::::::       :+:    :+:     :+:     :+:    :+:      #
#                                                         ::::::::::::::+++#####+++  +:+    +:+     +:+     +:+             #
#      By: branlyst <stephane.branly@etu.utc.fr>          ::+++##############+++     +:+    +:+     +:+     +:+             #
#      https://github.com/StephaneBranly              +++##############+++::::       +#+    +:+     +#+     +#+             #
#                                                       +++##+++::::::::::::::       +#+    +:+     +#+     +#+             #
#                                                         ::::::::::::::::::::       +#+    +#+     +#+     +#+             #
#                                                         ::::::::::::::::::::       #+#    #+#     #+#     #+#    #+#      #
#      Update: 2021/05/31 10:58:34 by branlyst            ::::::::::::::::::::        ########      ###      ######## .fr   #
#                                                                                                                           #
# ************************************************************************************************************************* #

import sys
from typing import List, Dict

Laby = Dict # { 'cell': [successors] } 

Laby1: Laby = {'A1': ['A2', 'B1'],
                'A2': ['A3', 'A1'],
                'A3': ['A4', 'A2'],
                'A4': ['B4', 'A3'],
                'B1': ['C1', 'A1'],
                'B2': [],
                'B3': [],
                'B4': ['C4', 'A4'],
                'C1': ['C2', 'D1', 'B1'],
                'C2': ['C3', 'D2', 'C1'],
                'C3': ['C4', 'C2'],
                'C4': ['D4', 'C3', 'B4'],
                'D1': ['D2', 'C1'],
                'D2': ['D1', 'C2'],
                'D3': [],
                'D4': ['C4'],
                'Depart': 'B1',
                'Arrivee': 'A4'
                }
                
def largeur(laby: Laby, depart: str, arrivee: str):
    chemin: List = list()
    visites: List = [depart]
    successeurs: List = [depart]
    next: str = ""
    while successeurs: 
        print("successeurs : ", successeurs)
        print("visites : ", visites, "\n")  
        next = successeurs.pop(0)
        visites.append(next)
        chemin.append(next)
        if(next == arrivee):
            return chemin
        for successeur in laby[next]:
            if(not successeur in visites):
                successeurs.append(successeur)
    return []

def profondeur(laby: Laby, depart: str, arrivee: str):
    chemin: List = list()
    visites: List = [depart]
    successeurs: List = [depart]
    next: str = ""
    while successeurs: 
        print("successeurs : ", successeurs)
        print("visites : ", visites, "\n")  
        next = successeurs.pop()
        visites.append(next)
        chemin.append(next)
        if(next == arrivee):
            return chemin
        for successeur in laby[next]:
            if(not successeur in visites):
                successeurs.append(successeur)
    return []

def largeur2(laby: Laby, depart: str, arrivee: str):
    pile = [depart]
    while arrivee not in pile:
        s=pile.pop(0)
        pile=pile + laby[s]
        print("pile", pile)
        
def profondeur2(laby: Laby, depart: str, arrivee: str):
    file = [depart]
    while arrivee not in file:
        s=file.pop()
        file=file + laby[s]
        print("file", file)


def main(argv):
    print(str(largeur(Laby1, Laby1['Depart'], Laby1["Arrivee"])))


if __name__ == "__main__":
    main(sys.argv[1:])
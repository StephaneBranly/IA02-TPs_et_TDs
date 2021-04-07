# ********************************************************************************************************************* #
# UTC Header                                                                                                            #
#                                                       ::::::::::::::::::::       :::    ::: :::::::::::  ::::::::     #
#    sudoku.py                                          ::::::::::::::::::::       :+:    :+:     :+:     :+:    :+:    #
#                                                       ::::::::::::::+++#####+++  +:+    +:+     +:+     +:+           #
#    By: branlyst <stephane.branly@etu.utc.fr>          ::+++##############+++     +:+    +:+     +:+     +:+           #
#    https://github.com/StephaneBranly              +++##############+++::::       +#+    +:+     +#+     +#+           #
#                                                     +++##+++::::::::::::::       +#+    +:+     +#+     +#+           #
#                                                       ::::::::::::::::::::       +#+    +#+     +#+     +#+           #
#                                                       ::::::::::::::::::::       #+#    #+#     #+#     #+#    #+#    #
#    Update: 2021/04/07 14:29:35 by branlyst            ::::::::::::::::::::        ########      ###      ######## .fr #
#                                                                                                                       #
# ********************************************************************************************************************* #

from typing import List, Tuple
import subprocess

# alias de types
Variable = int
Literal = int
Clause = List[Literal]
Model = List[Literal]
Clause_Base = List[Clause]
Grid = List[List[int]]

example: Grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]


example2: Grid = [
    [0, 0, 0, 0, 2, 7, 5, 8, 0],
    [1, 0, 0, 0, 0, 0, 0, 4, 6],
    [0, 0, 0, 0, 0, 9, 0, 0, 0],
    [0, 0, 3, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 5, 0, 2, 0],
    [0, 0, 0, 8, 1, 0, 0, 0, 0],
    [4, 0, 6, 3, 0, 1, 0, 0, 9],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [7, 2, 0, 0, 0, 0, 3, 1, 0],
]


empty_grid: Grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]

#### fonctions fournies


def write_dimacs_file(dimacs: str, filename: str):
    with open(filename, "w", newline="") as cnf:
        cnf.write(dimacs)


def exec_gophersat(
    filename: str, cmd: str = "gophersat", encoding: str = "utf8"
) -> Tuple[bool, List[int]]:
    result = subprocess.run(
        [cmd, filename], capture_output=True, check=True, encoding=encoding
    )
    string = str(result.stdout)
    lines = string.splitlines()

    if lines[1] != "s SATISFIABLE":
        return False, []

    model = lines[2][2:].split(" ")

    return True, [int(x) for x in model]


def displayGrid(grid: Grid):
    l=0
    c=0
    line=""
    for i in grid:
        c=0
        line=""
        if(l%3==0):
            print(" -------------------------")
        for j in i:
            if(c%3==0):
                line=line+" |"
            if(j==0):
                line=line+" ."
            else:
                line=line+" "+str(j)
            c=c+1
        print(line+" |")
        l=l+1
    print(" -------------------------")

#### fonction principale


def main():
    print("Hello world")
    displayGrid(example)
    pass


if __name__ == "__main__":
    main()

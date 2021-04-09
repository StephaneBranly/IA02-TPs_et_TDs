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
#    Update: 2021/04/09 10:12:49 by branlyst            ::::::::::::::::::::        ########      ###      ######## .fr #
#                                                                                                                       #
# ********************************************************************************************************************* #

from typing import List, Tuple
import subprocess
import sys, getopt, os

# alias de types
Variable = int
Literal = int
Clause = List[Literal]
Model = List[Literal]
Clause_Base = List[Clause]
Grid = List[List[int]]

def help():
    print("-h : help()")
    print("-g gridFile : Load a grid with the filename")
    print("-o outputFileName : Save the DISMACS file created")
    print("-s nameOS : Solve probleme using Gophersat, nameOS in [linux, windows, macos]")

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

#### given functions
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


#### added functions


def cell_to_variable(i: int, j: int, val: int) -> int:
    return i * 9 * 9 + j * 9 + val


def variable_to_cell(var: int) -> Tuple[int, int, int]:
    v = var - 1
    a = v / 81
    v = v % 81
    b = v / 9
    v = v % 9
    return (int(a), int(b), int(v + 1))


def at_least_one(vars: List[int]) -> List[int]:
    r = list()
    for i in vars:
        if i > 0:
            r.append(i)
    return r


def unique(vars: List[int]) -> List[List[int]]:
    r = list()
    r.append(vars)
    for i in range(len(vars)):
        for j in range(len(vars) - i - 1):
            r.append([(-1) * vars[i], (-1) * vars[i + j + 1]])
    return r


def create_line_constraints() -> List[List[int]]:
    r = list()
    for n in range(9):
        for line in range(9):
            l = list()
            for col in range(9):
                l.append(cell_to_variable(line, col, n + 1))
            r.append(l)
    return r


def create_column_constraints() -> List[List[int]]:
    r = list()
    for n in range(9):
        for col in range(9):
            l = list()
            for line in range(9):
                l.append(cell_to_variable(line, col, n + 1))
            r.append(l)
    return r


def create_box_constraints() -> List[List[int]]:
    r:List[List[int]] = []
    for n in range(9):
        for i in range(3):
            for j in range(3):
                l: List[int] = []
                for col in range(3):
                    for line in range(3):
                        l.append(cell_to_variable(i * 3 + col, j * 3 + line, n + 1))
                r.append(l)
    return r


def create_value_constraints(grid: List[List[int]]) -> List[List[int]]:
    r: List[List[int]] = []
    n: List[int] = []
    for col in range(9):
        for line in range(9):
            n = []
            for v in range(9):
                n.append(cell_to_variable(col, line, v + 1))
            r = r + unique(n)
            if grid[col][line] != 0:
                r.append([cell_to_variable(col, line, grid[col][line])])
    return r


def generate_problem(grid: List[List[int]]) -> List[List[int]]:
    r: List[List[int]] = list()
    r = r + create_line_constraints()
    r = r + create_column_constraints()
    r = r + create_box_constraints()
    r = r + create_value_constraints(grid)
    return r


def clauses_to_dimacs(clauses: List[List[int]], nb_vars: int) -> str:
    r = "c\nc made with love\nc\n"
    r = r + "p cnf " + str(nb_vars) + " " + str(len(clauses)) + "\n"
    for c in clauses:
        for t in c:
            r = r + str(t) + " "
        r = r + "0\n"
    return r


def model_to_grid(model: List[int], nb_vals: int = 9) -> List[List[int]]:
    g = [
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
    for i in model:
        if i > 0:
            c, l, v = variable_to_cell(i)
            g[c][l] = v
    return g


def displayGrid(grid: Grid):
    l = 0
    c = 0
    line = ""
    for i in grid:
        c = 0
        line = ""
        if l % 3 == 0:
            print(" -------------------------")
        for j in i:
            if c % 3 == 0:
                line = line + " |"
            if j == 0:
                line = line + " ."
            else:
                line = line + " " + str(j)
            c = c + 1
        print(line + " |")
        l = l + 1
    print(" -------------------------")

def loadSudoku(inputfile) -> Grid:
    try:
        linesGrid: List[int] = []
        result: Grid = []
        with open("./"+inputfile, "r") as filin:
            for line in filin:
                linesGrid = []
                line = line.rstrip('\r\n').split(' ')
                for c in line:
                    linesGrid.append(int(c))
                result.append(linesGrid)
        return result
    except:
        print("Error opening the graph file "+inputfile)
        return [[]]

#### fonction principale


def main(argv):
    inputFile: str = ""
    outputFile: str = ""
    osName: str = ""
    osPath: str = ""
    try:
        opts, args = getopt.getopt(argv,"hg:o:s:",["gridFile=","ouputFile=","OS="])
    except getopt.GetoptError:
        help()
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            help()
            sys.exit()
        elif opt in ("-g", "--gridFile"):
            inputFile = arg
        elif opt in ("-o", "--ouputFile"):
            outputFile = arg
        elif opt in ("-s","--OS"):
            osName = arg
    
    grid: Grid
    if(inputFile!=""):
        grid = loadSudoku(inputFile)
    else:
        grid=example2
        
    print("Original grid:")
    displayGrid(grid)
    
    clauses = generate_problem(grid)
    dimacs = clauses_to_dimacs(clauses, 729)

    if(outputFile==""):
        outputFile = "sudoku.cnf"
    write_dimacs_file(dimacs, outputFile)

    if(osName=='linux'):
        osPath = "../../gophersat/linux64/gophersat-1.1.6"
    elif(osName=='windows'):
        osPath = "../../gophersat/win64/gophersat-1.1.6.exe"
    elif(osName=='macos'):
        osPath = "../../gophersat/macos64/gophersat-1.1.6"
    if(osPath!=""):
        model = exec_gophersat(outputFile, cmd=osPath)
        grid = model_to_grid(model[1])
        print("Solution:")
        displayGrid(grid)


if __name__ == "__main__":
    main(sys.argv[1:])

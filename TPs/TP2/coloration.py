# **************************************************************************************************** #
#                                                                                                      #
#                                                                 :::    ::: :::::::::::  ::::::::     #
#    coloration.py                                                :+:    :+:     :+:     :+:    :+:    #
#                                                                 +:+    +:+     +:+     +:+           #
#    By: branlyst <stephane.branly@etu.utc.fr>                    +:+    +:+     +:+     +:+           #
#                                                                 +#+    +:+     +#+     +#+           #
#    Created: 2021/03/24 18:40:25 by branlyst                     +#+    +:+     +#+     +#+           #
#    Updated: 2021/03/24 18:40:25 by branlyst                     +#+    +#+     +#+     +#+           #
#                                                                 #+#    #+#     #+#     #+#    #+#    #
#                                                                  ########      ###      ########     #
#                                                                                                      #
# **************************************************************************************************** #

# (extension UTC Header dispo sur VSCode)

#!/usr/bin/python

from graph import Graph

colors = ["Red","Green","Blue","Cyan","Magenta","Yellow","Black","White","Purple","Pink"]

class Coloration():
    # Initialisation of the object 'Coloration'
    def __init__(self,graph,nbColors=3):
        self.graph = graph
        self.nbVertices = graph.getVerticesNumber()
        self.nbColors = nbColors

    def generateDIMACSfile(self,outputFile = None):
        generation = self.generateHeader() + '\n' + self.generateProblemHead()
        for i in self.graph.vertices:
            generation = generation + '\n' + self.generateClausesVertice(i)
        generation = generation + '\n'
        if(outputFile):
            try:
                f = open(outputFile, "w")
                f.write(generation)
                f.close()
            except:
                print("Error writing in file "+outputFile)
        else:
            print(generation)

    # Generate the header of the DIMACS file
    def generateHeader(self):
        return "c\nc  "+self.graph.getGraphFileName()+"\nc"

    def generateProblemHead(self):
        nbClauses = self.nbVertices * (fact(self.nbColors)/2 + 1)
        for v in self.graph.successors:
            nbClauses = nbClauses + (len(self.graph.successors[v]) * self.nbColors) / 2
        nbVars = self.nbVertices * self.nbColors
        return "p cnf "+str(nbVars)+" "+str(int(nbClauses))

    def generateClausesVertice(self,verticeName):
        index = self.graph.vertices[verticeName]

        # Condition on one color minimum
        colorMinClause = ""
        for i in range(self.nbColors):
            realColorIndex = i + (index - 1) * self.nbColors + 1
            colorMinClause = colorMinClause + " "+str(realColorIndex)
        colorMinClause = colorMinClause[1:] + " 0"

        # Condition on one color maximum
        colorMaxClauses = ""
        for i in range(self.nbColors):
            for j in range(self.nbColors - i - 1):
                iColorIndex = i + (index - 1) * self.nbColors + 1
                jColorIndex = i + j + 1 + (index - 1) * self.nbColors + 1
                colorMaxClauses = colorMaxClauses + "\n-" + str(iColorIndex) + " -" + str(jColorIndex)+" 0"

        # Conditions on successors
        successorsClauses = ""
        for succ in self.graph.successors[index]:
            # We don't want to have the same clauses twice
            if(int(succ) > index):
                for i in range(self.nbColors):
                    verColorI = (index -1) * self.nbColors + i + 1 
                    sucColorI = (int(succ)-1) * self.nbColors + i + 1
                    successorsClauses = successorsClauses + "\n-" + str(verColorI) + " -" +str(sucColorI) + " 0"                
        return colorMinClause + colorMaxClauses + successorsClauses

    # Print an intepretation of the solution found
    def interprete(self,solution):
        solutionLine = solution.split('\n')[2]
        print("INTERPRETATION :")
        solutionLine = solutionLine.split(' ')
        if self.nbColors <= len(colors):
            for v in range(self.graph.getVerticesNumber()):
                for c in range(self.nbColors):
                    i = v*self.nbColors + c
                    if int(solutionLine[i+1]) > 0:
                        print("Vertice "+str(v+1)+"  :   "+colors[c])
    
def fact(n):
    if n==0 :
        return 1
    return n * fact(n-1) 

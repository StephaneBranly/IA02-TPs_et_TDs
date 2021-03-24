# **************************************************************************************************** #
#                                                                                                      #
#                                                                 :::    ::: :::::::::::  ::::::::     #
#    graph.py                                                     :+:    :+:     :+:     :+:    :+:    #
#                                                                 +:+    +:+     +:+     +:+           #
#    By: branlyst <stephane.branly@etu.utc.fr>                    +:+    +:+     +:+     +:+           #
#                                                                 +#+    +:+     +#+     +#+           #
#    Created: 2021/03/24 18:48:59 by branlyst                     +#+    +:+     +#+     +#+           #
#    Updated: 2021/03/24 18:48:59 by branlyst                     +#+    +#+     +#+     +#+           #
#                                                                 #+#    #+#     #+#     #+#    #+#    #
#                                                                  ########      ###      ########     #
#                                                                                                      #
# **************************************************************************************************** #

# (extension UTC Header dispo sur VSCode)

#!/usr/bin/python

import sys

class Graph():
    # Initialisation of the object 'Graph'
    def __init__(self,inputfile="cubic_graph.txt"):
        self.inputfile = inputfile
        self.vertices = None
        self.successors = None
        self.loadGraph(inputfile)

    # Load a graph from an input file
    def loadGraph(self,inputfile="cubic_graph.txt"):
        try:
            newVertices = dict()
            newSuccessors = dict()
            with open("./"+inputfile, "r") as filin:
                i = 1
                for line in filin:
                    line = line.rstrip('\r\n').split(' ')
                    newVertices[line[0]] = i
                    newSuccessors[i] = line[1:]
                    i = i + 1
            self.vertices = newVertices
            self.successors = newSuccessors
        except:
            print("Error opening the graph file "+inputfile)

    # Print the content of the current loaded graph
    def printLoadedGraph(self):
        for l in self.vertices:
            print(str(self.vertices[l]) + " | "+str(self.successors[self.vertices[l]]))

    # Return the number of verticies
    def getVerticesNumber(self):
        return len(self.vertices)

    def getGraphFileName(self):
        return self.inputfile
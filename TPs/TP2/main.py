# **************************************************************************************************** #
#                                                                                                      #
#                                                                 :::    ::: :::::::::::  ::::::::     #
#    main.py                                                      :+:    :+:     :+:     :+:    :+:    #
#                                                                 +:+    +:+     +:+     +:+           #
#    By: branlyst <stephane.branly@etu.utc.fr>                    +:+    +:+     +:+     +:+           #
#                                                                 +#+    +:+     +#+     +#+           #
#    Created: 2021/03/24 18:38:14 by branlyst                     +#+    +:+     +#+     +#+           #
#    Updated: 2021/03/24 18:38:14 by branlyst                     +#+    +#+     +#+     +#+           #
#                                                                 #+#    #+#     #+#     #+#    #+#    #
#                                                                  ########      ###      ########     #
#                                                                                                      #
# **************************************************************************************************** #

# (extension UTC Header dispo sur VSCode)

#!/usr/bin/python

import sys, getopt, os

from graph import Graph
from coloration import Coloration

def help():
    print("Error... your are UTC sad")
    print("-h : help()")
    print("-g graphFileName : Load a graph with the filename")
    print("-c nbColors : Genere DISMACS file to colorize the graph with nbColors")
    print("-o outputFileName : Save the DISMACS file created")
    print("-r nameOS : Run Gophersat using the outputFile nameOS in [linux, windows, macOS]")

def main(argv):
    inputfile = None
    outputfile = None
    runOnOS = None
    graph = None
    colorisation = None
    nbColors = 3
    actions = dict()
    actions['loadGraph'] = False
    actions['colorGraph'] = False
    actions['runGo'] = False
    try:
        opts, args = getopt.getopt(argv,"hg:c:o:r:",["gfile=","nbColors=","ofile=","rOS="])
    except getopt.GetoptError:
        help()
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            help()
            sys.exit()
        elif opt in ("-g", "--gfile"):
            actions['loadGraph'] = True
            inputfile = arg
        elif opt in ("-c", "--nbColors"):
            actions['colorGraph'] = True
            nbColors = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        elif opt in ("-r", "--rOS"):
            actions['runGo'] = True
            runOnOS = arg
  
    
    if actions['loadGraph']:
        try:
            graph = Graph(inputfile)
        except:
            help()
    else:
        graph = Graph()


    if actions['colorGraph']:
        try:
            colorisation = Coloration(graph,nbColors)
            colorisation.generateDIMACSfile(outputfile)
        except:
            help()

    if actions['runGo']:
        if actions['colorGraph']:
            fileName = outputfile
        else:
            fileName = "cubic_graph.txt"

        if(runOnOS=='linux'):
            os.system("../../gophersat/linux64/gophersat-1.1.6 "+str(fileName))
        elif(runOnOS=='windows'):
            os.system("../../gophersat/win64/gophersat-1.1.6.exe "+str(fileName))
        else:
            os.system("../../gophersat/macos64/gophersat-1.1.6 "+str(fileName))

if __name__ == "__main__":
    main(sys.argv[1:])
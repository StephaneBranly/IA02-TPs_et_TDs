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
    print("-h : help()")
    print("-g graphFileName : Load a graph with the filename")
    print("-c nbColors : Genere DISMACS file to colorize the graph with nbColors")
    print("-o outputFileName : Save the DISMACS file created")
    print("-r nameOS : Run Gophersat using the outputFile nameOS in [linux, windows, macOS]")
    print("-i interpretation : Display text of an interpretation")

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
    actions['interprete'] = False

    try:
        opts, args = getopt.getopt(argv,"hg:c:o:r:i",["gfile=","nbColors=","ofile=","rOS="])
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
        elif opt in ("-i"):
            actions['interprete'] = True
  
    
    if actions['loadGraph']:
        try:
            graph = Graph(inputfile)
        except:
            help()
    else:
        graph = Graph()


    if actions['colorGraph']:
        try:
            colorisation = Coloration(graph,int(nbColors))
            colorisation.generateDIMACSfile(outputfile)
        except:
            help()

    if actions['runGo']:
        if actions['colorGraph']:
            fileName = outputfile
        else:
            fileName = "cubic_graph.txt"
        output = ''
        if(runOnOS=='linux'):
            output = os.popen("../../gophersat/linux64/gophersat-1.1.6 "+str(fileName)).read()
        elif(runOnOS=='windows'):
            output = os.popen("../../gophersat/win64/gophersat-1.1.6.exe "+str(fileName)).read()
        else:
            output = os.popen("../../gophersat/macos64/gophersat-1.1.6 "+str(fileName)).read()
        print(output)
        if(actions['interprete']):
            colorisation.interprete(output)

if __name__ == "__main__":
    main(sys.argv[1:])
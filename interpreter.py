#!/usr/bin/env python

import time
start_time = time.time()

import sys
from bidict import bidict


f = open(sys.argv[1], "r")
rawData = f.read()
f.close()



brackets = []
loopStarts = bidict({})

i=0

while (i < len(rawData)):
    ic = rawData[i]
    
    if (ic == "["):
        brackets.append({"b": "[", "i": i})

    elif (ic == "]"):

        if (brackets[-1]["b"] == "["):
            loopStarts[brackets[-1]["i"]] = i
            brackets.pop()
        else:  
            brackets.append({"b": "]", "i": i})

    i += 1

cells = [0, 0, 0, 0, 0, 0, 0, 0, 0]
dPointer = 0
cPointer = 0

while (cPointer < len(rawData)):
    c = rawData[cPointer]
    cell = cells[dPointer]

    if (c == ">"):
        dPointer += 1
    elif (c == "<"):
        dPointer -= 1
    elif (c == "+"):
        cells[dPointer] += 1
    elif (c == "-"):
        cells[dPointer] -= 1
    elif (c == "."):
        print(chr(cell))
    elif (c == ","):
        cells[dPointer] = input()
    elif (c == "["):
        if (cell == 0):
            cPointer = loopStarts[cPointer]
    elif (c == "]"):
        if (cell != 0):
            cPointer = loopStarts.inverse[cPointer]

    cPointer += 1

print("--- %s seconds ---" % (time.time() - start_time))

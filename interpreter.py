#!/usr/bin/env python

import sys

f = open(sys.argv[1], "r")
rawData = f.read()
f.close()


loopStarts = {}
loopEnds = {}

i = 0

loopStart = 0
depth = 0

while (i < len(rawData)):
    ic = rawData[i]

    print("d: " + str(depth) + " i: " + str(i) + " c: " + ic)

    if (ic == "["):
        depth += 1
        
        if (depth == 0):
            loopStart = i


    elif (ic == "]"):
        depth -= 1

        if (depth == 0):
            loopStarts[loopStart] = i
            i = loopStart
            

    
    i += 1
    
print(loopStarts)



cells = [0, 0, 0, 0, 0, 0, 0, 0, 0]
dPointer = 0
cPointer = 0

while (cPointer < len(rawData)):
    c = rawData[cPointer]

    print(c)
    if (c == ">"):
        dPointer += 1
    elif (c == "<"):
        dPointer -= 1
    elif (c == "+"):
        cells[dPointer] += 1
    elif (c == "-"):
        cells[dPointer] -= 1
    elif (c == "."):
        print(cells[dPointer])
    elif (c == ","):
        cells[dPointer] = input()
    elif (c == "["):
        print(c)
    elif (c == "]"):
        print(c)

    cPointer += 1

    

print(cells)




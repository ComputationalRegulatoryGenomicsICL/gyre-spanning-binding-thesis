#!/usr/bin/env python

"""
Based on a continues motif, generate a gapped motif with a defined gap size.
"""

import sys

inputFileName = sys.argv[1]
outputFileName = sys.argv[2]
gapSize = int(sys.argv[3])

with open(inputFileName, "r") as inputFile, \
     open(outputFileName, "w") as outputFile:
    lineList = []
    inMatrix = False
    motifWidth = 0
    rowNumber = 0
    # Read motif file and form output
    for line in inputFile:
        line = line.strip()
        if not inMatrix:
            if "letter-probability" in line:
                lineSplitted = line.split(" ")
                motifWidth = int(lineSplitted[5])
                inMatrix = True
                lineList.append(' '.join(lineSplitted[:5] + [str(motifWidth + gapSize)] + lineSplitted[6:]))
            else:
                lineList.append(line)
        else:
            rowNumber += 1
            lineList.append(line)
            if rowNumber == motifWidth / 2:
                lineList.extend(["0.25  0.25  0.25  0.25"] * gapSize)
    # Print the list of lines into the output file
    outputFile.write('\n'.join(lineList))

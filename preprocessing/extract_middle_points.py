#!/usr/bin/env python

"""
From a BED file, extract middle points of all reginons.
If the length of the region is even, it takes the position immediately preceding the middle of the region.
If the length of the region is odd, it takes the position in the middle.
"""

import sys

inFileName = sys.argv[1]
outFileName = sys.argv[2]

with open(inFileName, "r") as inFile, \
     open(outFileName, "w") as outFile:
    for line in inFile:
        if line.startswith("track"):
            outFile.write(line)
        else:
            lineList = line.strip().split("\t")
            seqId = lineList[0]
            seqStart = int(lineList[1]) 
            seqEnd = int(lineList[2])
            seqLen = seqEnd - seqStart
            if seqLen % 2 == 0:
                middleStart = seqStart + int((seqLen - 2) / 2)
            else:
                middleStart = seqStart + int((seqLen - 1) / 2)
            if lineList[3:]:
                outLine = '\t'.join([seqId, str(middleStart), str(middleStart + 1), '\t'.join(lineList[3:]) + "\n"])
            else:
                outLine = '\t'.join([seqId, str(middleStart), str(middleStart + 1) + "\n"])
            outFile.write(outLine)

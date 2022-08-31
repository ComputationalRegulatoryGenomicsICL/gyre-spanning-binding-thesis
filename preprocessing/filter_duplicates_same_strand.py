#!/usr/bin/env python3

import sys

inFileName = sys.argv[1]
outFileName = sys.argv[2]

with open(inFileName, "r") as inFile, \
     open(outFileName, "w") as outFile:
    idAndCoord = set()
    lines = dict()
    for line in inFile:
        if line.startswith("#"):
            outFile.write(line)
        else:
            lineList = line.strip().split("\t")
            seqId = lineList[1]
            seqStart = lineList[2]
            seqEnd = lineList[3]
            seqStrand = lineList[4]
            seqTriplet = ",".join([seqId, seqStart, seqEnd])
            if seqTriplet not in idAndCoord:
                idAndCoord.add(seqTriplet)
                lines[seqTriplet] = line
            else:
                if seqStrand == "+":
                    # Output current match
                    outFile.write(line)
                else:
                    # Output previous match
                    outFile.write(lines[seqTriplet])
                lines.pop(seqTriplet)
    for key in lines:
        outFile.write(lines[key])

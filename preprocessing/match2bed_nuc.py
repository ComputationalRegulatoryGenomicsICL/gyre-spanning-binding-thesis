#!/usr/bin/env python3

"""
Convert FIMO output for gapped motifs in nucleosomes to BED.
"""

import sys

inFileName = sys.argv[1]
outFileName = sys.argv[2]
gap_length = int(sys.argv[3])

with open(inFileName, "r") as inFile, \
     open(outFileName, "w") as outFile:
    for line in inFile:
        if line.startswith("#"):
            #outFile.write('track name="Gapped_T_motifs" description="Gapped T motifs matches in strong nucleosomes in human; gaps are 72, 73, 75 nt" itemRgb="On"\n')
            continue
        else:
            lineList = line.strip().split('\t')
            origName = lineList[1]
            insideStart = int(lineList[2])
            insideEnd = int(lineList[3])
            strand = lineList[4]
            score = lineList[5]
            chrNum = origName.split(":")[3]
            nucCoordRange = origName.split(":")[4]
            nucStart = int(nucCoordRange.split("-")[0])
            absStart = nucStart + insideStart - 1
            absEnd = nucStart + insideEnd
            matchName = ''.join([chrNum, ":", str(absStart), "-", str(absEnd), "_", str(gap_length)])
            if (strand == '+'):
                itemRgb = "255,0,0" # Red
            else:
                itemRgb = "0,0,255" # Blue
            blockCount = "2" # two halfs of the motif
            blockSizes = "8,8"
            firstStart = absStart
            gapSize = insideEnd - insideStart - 16 + 1
            secondStart = 8 + gapSize
            blockStarts = ','.join(["0", str(secondStart)])
            outFile.write('\t'.join([chrNum, str(absStart), str(absEnd), matchName, score, strand, str(absStart), str(absEnd), itemRgb, blockCount, blockSizes, blockStarts, "\n"]))


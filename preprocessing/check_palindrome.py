#!/usr/bin/env python

"""
If a motif in the input file (MEME format) is palindromic, then copy the input file to the output file.
Otherwise do nothing.
Motif M of length N is palindromic iff N is even and argmax(PFM[i]) ~ argmax(PFM[N - 1 - i]), where
- PFM is the position frequency matrix of the motif,
- 0 <= i <= N - 1,
- PFM[i] is the ith row of PFM,
- argmax(PFM[i]) is the most frequent nucleotide in the row,
- "~" means complementarity: A ~ T, T ~ A, C ~ G, G ~ C.
Alphabet should be ACGT, in this order.
The length of the motif should be even, because we need motifs for potential TF homodimers.
"""

import sys
import shutil

inputFileName = sys.argv[1]
outputFileName = sys.argv[2]

with open(inputFileName, "r") as inputFile:
    pfm = []
    inMatrix = False
    motifWidth = 0
    # Read PFM
    for line in inputFile:
        line = line.strip()
        if not inMatrix:
            if "letter-probability" in line:
                motifWidth = int(line.split(" ")[5])
                inMatrix = True
        else:
            if "URL" not in line and line:
                pfm.append(line.split('  ')[0:])
    # Check if the motif is palindromic
    palindrome = True
    if motifWidth % 2 == 0:
        for i in range(0, motifWidth / 2):
            topRow = pfm[i]
            bottomRow = pfm[motifWidth - 1 - i]
            topIndex = topRow.index(max(topRow))
            bottomIndex = bottomRow.index(max(bottomRow))
            if (topIndex == 0 and bottomIndex == 3 or
                # A ~ T
                topIndex == 3 and bottomIndex == 0 or
                # T ~ A
                topIndex == 1 and bottomIndex == 2 or
                # C ~ G
                topIndex == 2 and bottomIndex == 1):
                # G ~ C
                continue
            else:
                palindrome = False
    else:
        palindrome = False
    # Copy the input file to the output file if the motif if it is palindromic
    if palindrome:
        shutil.copyfile(inputFileName, outputFileName)

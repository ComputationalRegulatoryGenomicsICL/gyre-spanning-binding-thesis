#!/usr/bin/env python3

import sys

inFileName = sys.argv[1]
lenThreshold = int(sys.argv[2])

with open(inFileName, "r") as inFile:
    seq = ""
    for i, line in enumerate(inFile):
        if i % 4 == 0:
            if len(seq) == lenThreshold:
                print readId
                print seq
                print sep
                print qual
            readId = line.strip()
        elif (i - 1) % 4 == 0:
            seq = line.strip()
        elif (i - 2) % 4 == 0:
            sep = line.strip()
        elif (i - 3) % 4 == 0:
            qual = line.strip()
    if len(seq) == lenThreshold:
       print readId
       print seq
       print sep
       print qual

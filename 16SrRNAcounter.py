# -*- coding: utf-8 -*-
"""
Count the total length of 16S rRNA coding regions in a gff3 file.
"""
# credit to parseGFFAttributes and parseGFF3
# __author__  = "Uli Köhler"
# __license__ = "Apache License v2.0"
# __version__ = "1.1"

import argparse


parser = argparse.ArgumentParser(description="Count the number of genes")
parser.add_argument("-f", "--file", dest="fpath", help="Open specified file")

args = parser.parse_args()

genelength = 0
teststr = "16S ribosomal RNA"

with open(args.fpath) as infile:
    for line in infile:
        if line.startswith("#"):
            continue
        parts = line.strip().split("\t")
        buff = parts[8]
        if parts[2] == 'rRNA' and buff.find(teststr) != -1:
            genelength += int(parts[4]) - int(parts[3]) + 1

print("Total length of 16S rRNA coding regions = ", genelength)

# -*- coding: utf-8 -*-
"""
Count the number of rRNA in a gff3 file and its length.
"""
# credit to parseGFFAttributes and parseGFF3
# __author__  = "Uli Köhler"
# __license__ = "Apache License v2.0"
# __version__ = "1.1"

import argparse


parser = argparse.ArgumentParser(description="Count the number of genes")
parser.add_argument("-f", "--file", dest="fpath", help="Open specified file")

args = parser.parse_args()

filename = args.fpath
genelength = 0

with open(filename) as infile:
    for line in infile:
        if line.startswith("#"):
            continue
        parts = line.strip().split("\t")
        if parts[2] == 'rRNA':
            genelength += int(parts[4]) - int(parts[3]) + 1

print("Total length of rRNA = ", genelength)

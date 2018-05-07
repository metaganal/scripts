# -*- coding: utf-8 -*-
"""
Count the number of genes/CDS in a gff3 file and sums the length of the genes.
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
genecount = 0
geneCDS = 0

with open(filename) as infile:
    for line in infile:
        if line.startswith("#"):
            continue
        parts = line.strip().split("\t")
        if parts[1] == 'Genbank' and parts[2] == 'gene':
            genecount += 1
        if parts[1] == 'Genbank' and parts[2] == 'CDS':
            geneCDS += 1

print("Total number of genes = ", genecount)
print("Total number of CDS = ", geneCDS)

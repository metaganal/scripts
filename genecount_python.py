# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 07:37:22 2018

@author: user
"""
# credit to parseGFFAttributes and parseGFF3
# __author__  = "Uli Köhler"
# __license__ = "Apache License v2.0"
# __version__ = "1.1"

filename = input("Please input filename :")
record = ()
genecount = 0
genelength = 0

with open(filename) as infile:
    for line in infile:
        if line.startswith("#"):
            continue
        parts = line.strip().split("\t")
        if parts[2] == 'gene':
            genecount += 1
            genelength += int(parts[4]) - int(parts[3])

print("Total number of genes = ", genecount)
print("Total length of gene regions = ", genelength)

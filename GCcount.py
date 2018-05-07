# -*- coding: utf-8 -*-
"""
Count the GC ratio of Genbank genes from a gff3 and fna file.
"""
# credit to parseGFFAttributes and parseGFF3
# __author__  = "Uli Köhler"
# __license__ = "Apache License v2.0"
# __version__ = "1.1"

import argparse
from collections import Counter


parser = argparse.ArgumentParser(description="Count the number of genes")
parser.add_argument("-gf", "--gfile", dest="gfpath", help="Open specified gff3 file")
parser.add_argument("-ff", "--ffile", dest="ffpath", help="Open specified fna file")

args = parser.parse_args()

genecount = 0
i = 1
fullseq = ""

with open(args.ffpath) as infile:
    for line in infile:
        if line.startswith(">"):
            continue
        fullseq += line


with open(args.gfpath) as infile:
    for line in infile:
        if line.startswith("#"):
            continue
        parts = line.strip().split("\t")
        if parts[1] == 'Genbank' and parts[2] == 'gene':
            seqstart = int(parts[3]) - 1
            seqend = int(parts[4])
            tempseq = fullseq[seqstart:seqend]
            seqcount = Counter(tempseq)
            GCsum = seqcount['G'] + seqcount['C']
            lenseq = seqend - seqstart
            GCratio = GCsum / lenseq
            print("GC ratio of gene {} = {}".format(i, GCratio))
            i += 1

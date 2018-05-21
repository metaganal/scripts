"""
Count the number of genes in a gff3 file and sums the length of the genes.
"""

import argparse


parser = argparse.ArgumentParser(description="Count the number of genes")
parser.add_argument("-f", "--file", dest="fpath", help="Open specified file")

args = parser.parse_args()

filename = args.fpath
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
            genelength += int(parts[4]) - int(parts[3]) + 1

print("Total number of genes = {0}".format(genecount))
print("Total length of gene regions = {0}".format(genelength))

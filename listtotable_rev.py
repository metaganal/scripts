# -*- coding: utf-8 -*-
"""
Reads lists and then make an abundance table from it.
"""

import argparse
from pandas import DataFrame
import ntpath


def makelist(filename):
    with open(filename) as listfile:
        genuslist = []

        for line in listfile:
            genuslist.append(line[:-1])
        genuslist.sort()

    return genuslist


def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)


parser = argparse.ArgumentParser(description="Read lists and make a table.")
parser.add_argument("-f", "--file", dest="fpath", nargs='+', help="Filepath of lists")
parser.add_argument("-o", "--output", dest="ofile", help="Specify output file.")

args = parser.parse_args()
genustable = []
genuscount = {}

for i in args.fpath:
    genustable.append(makelist(i))

for j in range(len(genustable)):
    for i in range(len(genustable[j])):
        temp_str = str(genustable[j][i])
        if temp_str not in genuscount:
            genuscount.setdefault(temp_str, [])
            for k in range(len(genustable)):
                genuscount[temp_str].append(0)
            genuscount[temp_str][j] += 1
        else:
            genuscount[temp_str][j] += 1

filenames = [path_leaf(path) for path in args.fpath]

genusdata = DataFrame(data=genuscount, index=filenames)
genusdata = genusdata.transpose()

genusdata.to_csv(args.ofile, sep='\t')

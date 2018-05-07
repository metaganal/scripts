# -*- coding: utf-8 -*-
"""
Reads lists and then make an abundance table from it.
"""

import argparse
import sys


def makelist(filename):
    with open(filename) as listfile:
        genuslist = []

        for line in listfile:
            genuslist.append(line[:-1])
        genuslist.sort()

    return genuslist


parser = argparse.ArgumentParser(description="Read lists and make a table.")
parser.add_argument("-f", "--file", dest="fpath", nargs='+', help="Filepath of lists")


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

print("\tgenus1.list\tgenus2.list\tgenus3.list")
for k, v in genuscount.items():
    sys.stdout.write(k)
    for i in range(len(v)):
        sys.stdout.write("\t{}".format(v[i]))
    print()

# -*- coding: utf-8 -*-
"""
Reads lists and then make an abundance table from it.
"""

import argparse


parser = argparse.ArgumentParser(description="Read lists and make a table.")
parser.add_argument("-f", "--file", dest="fpath", nargs='+', help="Filepath of lists")
parser.add_argument("-o", "--output", dest="ofpath", help="Filepath of output file")

args = parser.parse_args()
genustable = []
genuscount = {}
j = 0

for i in args.fpath:
    with open(i) as listfile:
        for line in listfile:
            line = line[:-1]
            if line not in genuscount:
                genuscount.setdefault(line, [])
                for k in range(len(args.fpath)):
                    genuscount[line].append(0)
                genuscount[line][j] += 1
            else:
                genuscount[line][j] += 1
    j += 1

ofile = open(args.ofpath, "w+")

for k, v in genuscount.items():
    ofile.write(k)
    for i in range(len(v)):
        ofile.write("\t{}".format(v[i]))
    ofile.write("\n")

ofile.close()

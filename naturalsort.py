# -*- coding: utf-8 -*-
"""
Sort list content naturally, e.g. 1, 2, 10 instead of 1, 10, 2
"""

import argparse
import re


def naturalsort(listtosort):
    convert = lambda text: int(text) if text.isdigit() else text
    natsort_alg = lambda algo: [convert(c) for c in re.split('([0-9]+)', algo)]
    listtosort.sort(key=natsort_alg)
# credit to:
# https://blog.codinghorror.com/sorting-for-humans-natural-sort-order/


parser = argparse.ArgumentParser(description="Sort the list naturally.")
parser.add_argument("-f", "--file", dest="fpath", help="Open specified file.")
parser.add_argument("-o", "--output", dest="ofpath", help="Specify path of output file.")


args = parser.parse_args()

filename = args.fpath
enzymelist = []

with open(filename) as enzymes:
    for line in enzymes:
        enzymelist.append(line)

naturalsort(enzymelist)

filename = args.ofpath

ofile = open(filename, "w+")

for i in range(len(enzymelist)):
    ofile.write(enzymelist[i])

ofile.close()

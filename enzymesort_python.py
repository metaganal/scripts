# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 21:20:38 2018

@author: user
"""

import re
import sys


def naturalsort(listtosort):
    convert = lambda text: int(text) if text.isdigit() else text
    natsort_alg = lambda algo: [convert(c) for c in re.split('([0-9]+)', algo)]
    listtosort.sort(key=natsort_alg)
# credit to:
# https://blog.codinghorror.com/sorting-for-humans-natural-sort-order/


filename = input("Please input filename :")
enzymelist = []

with open(filename) as enzymes:
    for line in enzymes:
        enzymelist.append(line)

naturalsort(enzymelist)

for i in range(len(enzymelist)):
    sys.stdout.write(enzymelist[i])

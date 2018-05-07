# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 21:31:51 2018

@author: user
"""

import sys


def makelist(filename):
    with open(filename) as listfile:
        genuslist = []

        for line in listfile:
            genuslist.append(line[:-1])
        genuslist.sort()

    return genuslist


genustable = []
genuscount = {}

while True:
    filename = input("Please input filename :")
    genustable.append(makelist(filename))
    print(len(genustable))
    choice = input("Any more files to read (Y/N)?")
    if choice.lower() != 'y':
        break

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

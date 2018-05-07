# -*- coding: utf-8 -*-
"""
Cut the gene in files with either EcoRI, HindIII, BamHI, NotI or all of them
"""

import argparse


def cut(seq, enzyme, cut_pos):
    frags = []
    start = 0
    end = seq.find(enzyme)

    while True:
        if end == -1:
            frags.append(seq[start:])
            break
        frags.append(seq[start:end + cut_pos])
        start = end + cut_pos
        end = seq.find(enzyme, start)

    return frags


parser = argparse.ArgumentParser(description="Cut the gene in file")
parser.add_argument("-f", "--file", dest="fpath", help="Open specified file")
parser.add_argument("-c", "--cut", dest="mode", help="""
Please specify restriction enzyme to cut the sequence :
1.EcoRI
2.HindIII
3.BamHI
4.NotI
5.All of the above
""", type=int)


args = parser.parse_args()

filename = args.fpath

header = ''
seq = []
frags = []
seqlength = 0
ecor1 = 'GAATTC'
hind3 = 'AAGCTT'
bamh1 = 'GGATCC'
not1 = 'GCGGCCGC'

with open(filename) as fastafile:
    for line in fastafile:
        if line.startswith('>'):
            header = line
            continue
        seq.append(line[:-1])

fullseq = ''.join(seq)

i = args.mode

if i == 1:
    frags = cut(fullseq, ecor1, 1)
    for x in range(len(frags)):
        print("Length of fragment ", x+1, " is ", len(frags[x]))
        seqlength += len(frags[x])
    print('Total gene length = ', seqlength)
elif i == 2:
    frags = cut(fullseq, hind3, 1)
    for x in range(len(frags)):
        print("Length of fragment ", x+1, " is ", len(frags[x]))
        seqlength += len(frags[x])
    print('Total gene length = ', seqlength)
elif i == 3:
    frags = cut(fullseq, bamh1, 1)
    for x in range(len(frags)):
        print("Length of fragment ", x+1, " is ", len(frags[x]))
        seqlength += len(frags[x])
    print('Total gene length = ', seqlength)
elif i == 4:
    frags = cut(fullseq, not1, 1)
    for x in range(len(frags)):
        print("Length of fragment ", x+1, " is ", len(frags[x]))
        seqlength += len(frags[x])
    print('Total gene length = ', seqlength)
elif i == 5:
    frags = cut(fullseq, ecor1, 1)
    n = len(frags)
    for x in range(len(frags)):
        frags += cut(frags[x], hind3, 1)
    frags = frags[n:]
    n = len(frags)
    for x in range(len(frags)):
        frags += cut(frags[x], bamh1, 1)
    frags = frags[n:]
    n = len(frags)
    for x in range(len(frags)):
        frags += cut(frags[x], not1, 2)
    frags = frags[n:]
    for x in range(len(frags)):
        print("Length of fragment ", x+1, " is ", len(frags[x]))
        seqlength += len(frags[x])
    print('Total gene length = ', seqlength)
else:
    print("Please enter an integer between 1-5.")

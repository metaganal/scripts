"""
Print the stats of inputted sequences
Stats : Sum, Min, Max, Mean
"""

import argparse
import sys


def sum(seq):
    n = 0
    for i in range(len(seq)):
        n += seq[i]
    return n


def mean(seq):
    n = sum(seq)
    m = n / len(seq)
    return m


def min(seq):
    min_val = seq[0]
    for i in range(len(seq)):
        if min_val > seq[i]:
            min_val = seq[i]
    return min_val


def max(seq):
    max_val = seq[0]
    for i in range(len(seq)):
        if max_val < seq[i]:
            max_val = seq[i]
    return max_val


parser = argparse.ArgumentParser()
parser.add_argument("seq", help="Sequence to sort")
parser.add_argument("-dl", "--delimiter", dest="delim", default=",", help="Delimiter of sequence")

args = parser.parse_args()

line = args.seq

listseq = list(map(int, line.split(args.delim)))

sys.stdout.write("{},".format(sum(listseq)))
sys.stdout.write("{},".format(min(listseq)))
sys.stdout.write("{},".format(max(listseq)))
sys.stdout.write("{}".format(mean(listseq)))

"""
Count the amino acid frequency of each amino acid in a sequence.
"""


import argparse
from collections import Counter

parser = argparse.ArgumentParser()
parser.add_argument("seq", help="The amino acid sequence to read")

args = parser.parse_args()

aminofreq = Counter(args.seq)
seqlen = len(args.seq)

for i in aminofreq:
    print("Frequency of {} = {}".format(i, aminofreq[i] / seqlen))

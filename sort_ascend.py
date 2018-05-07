"""
Sort list by ascending order
"""

import argparse
import sys


parser = argparse.ArgumentParser()
parser.add_argument("seq", help="Sequence to sort")
parser.add_argument("-dl", "--delimiter", dest="delim", default=",", help="Delimiter of sequence")

args = parser.parse_args()

line = args.seq

listseq = list(map(int, line.split(args.delim)))

sortseq = sorted(listseq)

for i in sortseq:
    sys.stdout.write("{},".format(i))

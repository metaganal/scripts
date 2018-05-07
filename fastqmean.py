"""
Parse a fastq file and return a fasta file containing sequences with
Q-score averaging 25 or more.
"""


import argparse


parser = argparse.ArgumentParser()
parser.add_argument("ifpath", help="Path of the input file (.fastq)")
parser.add_argument("ofpath", help="Path of the output file (.fasta)")

args = parser.parse_args()

outfile = open(args.ofpath, "w+")

with open(args.ifpath) as infile:
    for line in infile:
        if line.startswith('+'):
            check = infile.readline()
            qscore = 0
            base = ord('!')
            for i in check:
                qscore += ord(i) - base
            checker = qscore/len(check)
            outfile.write("{}\n".format(checker))
            continue

outfile.close()

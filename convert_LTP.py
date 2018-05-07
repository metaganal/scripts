"""
Convert LTP files with the rules below:
1. Replace the tabs in header with spaces
2. Replace the U in sequences with T
3. Remove spaces or tabs from sequences
"""


import argparse


parser = argparse.ArgumentParser()
parser.add_argument("ifpath", help="Path of input file")
parser.add_argument("ofpath", help="Path of output file")

args = parser.parse_args()

infile = open(args.ifpath)
outfile = open(args.ofpath, "w+")
seq = ""

for line in infile:
    if line.startswith(">"):
        line = line.replace("\t", " ")
        if len(seq) > 0:
            outfile.write(seq + "\n")
            seq = ""
        outfile.write(line)
    else:
        line = line.replace("U", "T").replace(" ", "").replace("\t", "")
        seq += line.strip("\n")

outfile.write(seq)

outfile.close()

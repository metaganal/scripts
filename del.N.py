#!/Users/felix/.pyenv/shims/python3
"""
Parse a fastq file and remove entries with N in the sequence
The name of output file will be <inputfilename>.N
"""


import argparse


parser = argparse.ArgumentParser()
parser.add_argument("ifpath", nargs='*', help="Path of input file (.fastq)")

args = parser.parse_args()

for i in range(len(args.ifpath)):
    ofpath = args.ifpath[i] + ".N"
    outfile = open(ofpath, "w+")

    block = []
    towrite = ""

    with open(args.ifpath[i]) as infile:
        for line in infile:
            block.append(line)

            if len(block) == 4:
                seq = block[1]
                if 'N' in seq:
                    block = []
                else:
                    towrite += "".join(block)
                    block = []

    outfile.write(towrite)
    outfile.close()

"""
Parse a fastq file and return a fastq file containing sequences with
Q-score averaging 25 or more.
"""


import argparse
import sys


parser = argparse.ArgumentParser()
parser.add_argument("ifpath", nargs='*', help="Path of the input files")

args = parser.parse_args()

for i in range(len(args.ifpath)):
    ofpath = args.ifpath[i] + ".qv25"
    outfile = open(ofpath, "w+")
    count = 0
    towrite = ""

    with open(args.ifpath[i]) as infile:
        block = []

        for line in infile:
            count += 1
            block.append(line)

            if count % 4 == 0:
                scoresum = 0
                for n in line[:-1]:
                    scoresum += ord(n) - 33
                meanq = scoresum / len(line[:-1])

                if meanq < 25:
                    block = []
                else:
                    towrite += "".join(block)
                    block = []

    outfile.write(towrite)
    sys.stdout.write("Finished writing to {}\n".format(ofpath))

    outfile.close()

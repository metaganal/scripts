"""
Convert fastq file to fasta file
"""


import argparse


parser = argparse.ArgumentParser()
parser.add_argument("ifpath", nargs='*', help="Path of the input files")

args = parser.parse_args()

for i in range(len(args.ifpath)):
    ofpath = args.ifpath[i] + ".fasta"
    outfile = open(ofpath, "w+")
    count = 0
    towrite = ""

    with open(args.ifpath[i]) as infile:
        for line in infile:
            count += 1

            if count % 4 == 1:
                towrite += ">" + line[1:]
            if count % 4 == 2:
                towrite += line

    outfile.write(towrite)

    outfile.close()

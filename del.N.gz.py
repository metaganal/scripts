#!/Users/felix/.pyenv/shims/python3
"""
Parse a fastq file and remove entries with N in the sequence
The name of output file will be <inputfilename>.N
"""


import argparse
import gzip


def myopen(inpath):
    if inpath.endswith('.gz'):
        return gzip.open(inpath, "rt")
    else:
        return open(inpath)


parser = argparse.ArgumentParser()
parser.add_argument("ifpath", nargs='*', help="Path of input file (.fastq)")

args = parser.parse_args()

for i in range(len(args.ifpath)):
    ofpath = args.ifpath[i] + ".N"
    block = []
    towrite = ""

    with myopen(args.ifpath[i]) as infile:
        print("Opening {}".format(args.ifpath[i]))

        for line in infile:
            block.append(line)

            if len(block) == 4:
                seq = block[1]
                if 'N' in seq:
                    block = []
                else:
                    towrite += "".join(block)
                    block = []

        print("Finished reading {}".format(args.ifpath[i]))

    if args.ifpath[i].endswith('.gz'):
        outfile = gzip.open(ofpath, "wb+")
        towrite = towrite.encode()
    else:
        outfile = open(ofpath, "w+")
    print("Writing content to file")
    outfile.write(towrite)
    outfile.close()

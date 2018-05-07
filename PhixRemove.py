#!/Users/felix/.pyenv/shims/python3
"""
Parse a fastq file and remove entries that aligned with PhiX
(Based on the SAM provided)
The name of output file will be *.fastq.N.rem
"""


import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-f",  "--seqfile", dest="ifpath", nargs='*', help="Path of input file (.fastq)")
parser.add_argument("-s", "--samfiles", dest="samfpath", nargs='*', help="Path of SAM files to use")
args = parser.parse_args()

if len(args.ifpath) != len(args.samfpath):
    print("Error: The number of fastq files and sam files don't match")

for i in range(len(args.ifpath)):
    ofpath = args.ifpath[i] + ".rem"
    outfile = open(ofpath, "w+")

    block = []
    IDlist = []
    towrite = ""

    with open(args.samfpath[i]) as samfile:
        for line in samfile:
            parts = line.split('\t')
            IDlist.append(parts[0])
    IDlist.reverse()

    with open(args.ifpath[i]) as infile:
        for line in infile:
            block.append(line)

            if len(block) == 4:
                if len(IDlist) > 0 and IDlist[-1] in block[0]:
                    block = []
                    del IDlist[-1]
                else:
                    towrite += "".join(block)
                    block = []

    outfile.write(towrite)
    outfile.close()

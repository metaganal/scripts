"""
List fasta entries to <SampleID><ReadID>
Each column is tab-separated
"""


import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-f", "--input", nargs="*", dest="ifpath", help="Path of input file(s)")

args = parser.parse_args()

for i in range(len(args.ifpath)):
    towrite = ""

    ofpath = args.ifpath[i] + ".list"
    ofile = open(ofpath, "w+")

    with open(args.ifpath[i]) as fasta:
        for line in fasta:
            if '>' in line:
                sample = line[1:10]
                read = line[1:]
                towrite += "{0}\t{1}".format(sample, read)

    ofile.write(towrite)
    ofile.close()

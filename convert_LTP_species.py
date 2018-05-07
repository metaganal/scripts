"""
Convert fasta_tmp header into a list of species and class
"""


import argparse


parser = argparse.ArgumentParser()
parser.add_argument("ifpath", help="Path of input file")
parser.add_argument("ofpath", help="Path of output file")

args = parser.parse_args()

infile = open(args.ifpath)
outfile = open(args.ofpath, "w+")

for line in infile:
    if line.startswith(">"):
        parts = line.strip(">\n").replace(" ", "_").split("\t")
        outfile.write("_".join(parts))
        outfile.write("\t{i[5]}\n".format(i=parts))

infile.close()
outfile.close()

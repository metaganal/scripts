"""
Calculate the relative abundance of each OTU per sample
"""


import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-in", "--input", dest="ifpath", help="The input file path")

args = parser.parse_args()

ofpath = args.ifpath + ".normalized"

OTU = []
abundance = []
towrite = ""

with open(args.ifpath) as infile:
    for line in infile:
        temp = line.strip('\n').split('\t')
        if temp[0] == "":
            towrite += line
        else:
            OTU.append(temp[0])
            abundance.append(list(map(float, temp[1:])))

total_abundance = list(map(sum, zip(*abundance)))

for i in range(len(OTU)):
    for j in range(len(abundance[0])):
        abundance[i][j] = abundance[i][j] / total_abundance[j]
    towrite += "{}\t{}\n".format(OTU[i], "\t".join(map(str, abundance[i])))

with open(ofpath, "w+") as outfile:
    outfile.write(towrite)

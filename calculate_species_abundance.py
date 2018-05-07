"""
Calculate species abundance based on OTU reads, blast output and species list
"""


import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-s", "--spec", dest="spec", help="The list of species name")
parser.add_argument("-b", "--blast", dest="blast", help="The blast output to read")
parser.add_argument("-m", "-matrix", dest="matrix", help="The matrix to read")

args = parser.parse_args()

ofpath = args.matrix + ".silva.id0.97.cov0.8.parsed"
spec_dict = {}
blast_dict = {}
abund_dict = {}
final_dict = {}
towrite = ""

with open(args.spec) as infile:
    for line in infile:
        temp = line.strip('\n').split('\t')
        spec_dict[temp[0]] = temp[1]

with open(args.matrix) as infile:
    for line in infile:
        temp = line.strip('\n').split('\t')
        if not temp[0] == "":
            abund_dict[temp[0]] = sum(map(int, temp[1:]))

with open(args.blast) as infile:
    for line in infile:
        temp = line.strip('\n').split('\t')
        temp2 = temp[0].split(';')
        if temp2[0] not in blast_dict:
            blast_dict[temp2[0]] = []
        blast_dict[temp2[0]].append(temp[1])

for k, v in abund_dict.items():
    if k not in blast_dict:
        species = "Unclassifed"
        abundance = v
        if species not in final_dict:
            final_dict[species] = 0
        final_dict[species] += abundance
    else:
        for i in blast_dict[k]:
            species = spec_dict[i]
            abundance = v / len(blast_dict[k])
            if species not in final_dict:
                final_dict[species] = 0
            final_dict[species] += abundance

for k, v in final_dict.items():
    towrite += "{}\t{}\n".format(k, v)

with open(ofpath, "w+") as outfile:
    outfile.write(towrite)

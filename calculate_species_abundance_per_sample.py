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
        if temp[0] == "":
            towrite += line
        else:
            abund_dict[temp[0]] = list(map(int, temp[1:]))


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
        for i in range(len(v)):
            if species not in final_dict:
                final_dict[species] = []
                for n in range(len(v)):
                    final_dict[species].append(0)
            abundance = v[i]
            final_dict[species][i] += abundance
    else:
        for i in blast_dict[k]:
            species = spec_dict[i]
            for n in range(len(v)):
                if species not in final_dict:
                    final_dict[species] = []
                    for m in range(len(v)):
                        final_dict[species].append(0)
                abundance = v[n] / len(blast_dict[k])
                final_dict[species][n] += abundance

for k, v in final_dict.items():
    towrite += "{}\t{}\n".format(k, "\t".join(map(str, v)))

with open(ofpath, "w+") as outfile:
    outfile.write(towrite)

"""
Filter blast output to each OTUs top hit
based on score and identity.
If both score and identity are equal the OTU has multiple hits.
"""


import argparse


parser = argparse.ArgumentParser()
parser.add_argument("blast", help="The blast output to filter")

args = parser.parse_args()

ofpath = args.blast + ".parsed"
towrite = ""
blastdict = {}

with open(args.blast) as infile:
    for line in infile:
        temp = line.strip('\n').split('\t')
        OTU = temp[0]
        if OTU not in blastdict.keys():
            blastdict[OTU] = []
            blastdict[OTU].append(line)
        else:
            comp = blastdict[OTU][0].strip('\n').split('\t')
            if temp[11] > comp[11]:
                blastdict[OTU][0] = line
            elif temp[11] == comp[11] and temp[2] > comp[2]:
                blastdict[OTU][0] = line
            elif temp[11] == comp[11] and temp[2] == comp[2]:
                blastdict[OTU].append(line)

for k, v in blastdict.items():
    for i in v:
        towrite += i

with open(ofpath, "w+") as outfile:
    outfile.write(towrite)

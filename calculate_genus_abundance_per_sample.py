"""
Calculate genus abundance based on OTU reads and RDP output
"""


import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-r", "--RDP", dest="RDP", help="The RDP output to read")
parser.add_argument("-m", "-matrix", dest="matrix", help="The matrix to read")

args = parser.parse_args()

ofpath = args.matrix + ".rdp.0.5"
RDP_dict = {}
abund_dict = {}
final_dict = {}
towrite = ""

with open(args.matrix) as infile:
    for line in infile:
        temp = line.strip('\n').split('\t')
        if temp[0] == "":
            towrite += line
        else:
            abund_dict[temp[0]] = list(map(int, temp[1:]))

with open(args.RDP) as infile:
    for line in infile:
        temp = line.strip('\n').split('\t')
        temp2 = temp[0].split(';')
        if temp2[0] not in RDP_dict:
            RDP_dict[temp2[0]] = []
        if float(temp[-1]) < 0.5:
            RDP_dict[temp2[0]].append("Unclassifed")
        else:
            RDP_dict[temp2[0]].append(temp[-3])

for k, v in abund_dict.items():
    for i in RDP_dict[k]:
        genus = i
        for n in range(len(v)):
            if genus not in final_dict:
                final_dict[genus] = []
                for m in range(len(v)):
                    final_dict[genus].append(0)
            abundance = v[n] / len(RDP_dict[k])
            final_dict[genus][n] += abundance

for k, v in final_dict.items():
    towrite += "{}\t{}\n".format(k, "\t".join(map(str, v)))

with open(ofpath, "w+") as outfile:
    outfile.write(towrite)

"""
Parse .list and .fasta.derep.uc file
Make a .list.derep file based on read files
"""


import argparse


parser = argparse.ArgumentParser()
parser.add_argument("rlist", help="The .list file to read")
parser.add_argument("derep", help="The .fasta.derep.uc file to read")

args = parser.parse_args()

ofpath = args.rlist + ".derep"
towrite = ""
refer_dict = {}
with open(args.derep) as refer:
    for line in refer:
        temp = line.strip('\n').split('\t')
        if temp[0] == 'S':
            refer_dict[temp[8]] = temp[8]
        if temp[0] == 'H':
            refer_dict[temp[8]] = temp[9]

with open(args.rlist) as listfile:
    for line in listfile:
        temp = line.strip('\n').split('\t')
        towrite += "{}\t{}\t{}\n".format(temp[0], temp[1], refer_dict[temp[1]])

with open(ofpath, "w+") as outfile:
    outfile.write(towrite)

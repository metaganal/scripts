"""
Turn a list file into a table showing
how many entry became OTUs in a sample
Columns are sample IDs
Rows are Entry IDs that became OTU
"""


import argparse
import sys


parser = argparse.ArgumentParser()
parser.add_argument("rlist", help="The list to read from")

args = parser.parse_args()

ofpath = args.rlist + ".matrix"
entry_dict = {}
columns = []

with open(args.rlist) as infile:
    for line in infile:
        temp = line.strip('\n').split('\t')
        if not temp[0] in columns:
            columns.append(temp[0])
        if not temp[3] in entry_dict:
            entry_dict[temp[3]] = {}
        if not temp[0] in entry_dict[temp[3]]:
            entry_dict[temp[3]][temp[0]] = 0
        entry_dict[temp[3]][temp[0]] += 1

towrite = "\t" + "\t".join(columns) + "\n"

for k in entry_dict.keys():
    val = []
    for i in columns:
        try:
            val.append(entry_dict[k][i])
        except KeyError:
            entry_dict[k][i] = 0
            val.append(entry_dict[k][i])
    val = list(map(str, val))
    tempstr = "\t".join(val)
    sys.stdout.write(tempstr + "\n")
    towrite += "{}\t{}\n".format(k, tempstr)

with open(ofpath, "w+") as outfile:
    outfile.write(towrite)

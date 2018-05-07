"""
Parse .list.derep and .uc file
Make a list based on read files

The columns are:
<SampleID>
<EntryID>
<RepresentativeEntryID>
<EntryID of the same OTU>
"""


import argparse


parser = argparse.ArgumentParser()
parser.add_argument("derep", help="The .derep file to read")
parser.add_argument("uclust", help="The .uc file to read")

args = parser.parse_args()

ofpath = args.derep + ".uclust.id0.97.cov0.8"
towrite = ""
refer_dict = {}

with open(args.uclust) as refer:
    for line in refer:
        temp = line.strip('\n').split('\t')
        if temp[0] == 'S':
            temp2 = temp[8].split(';')
            refer_dict[temp2[0]] = temp2[0]
        if temp[0] == 'H':
            temp2 = temp[8].split(';')
            temp3 = temp[9].split(';')
            refer_dict[temp2[0]] = temp3[0]

with open(args.derep) as listfile:
    for line in listfile:
        temp = line.strip('\n').split('\t')
        tempstr = "{}\t{}\n".format(line.strip('\n'), refer_dict[temp[2]])
        towrite += tempstr

with open(ofpath, "w+") as outfile:
    outfile.write(towrite)

"""
Determine whether an entry is chimera or not
based on .ref and .denovo files

The columns are:
<SampleID>
<EntryID>
<RepresentativeEntryID>
<EntryID of the same OTU>
<Chimera or not>
"""


import argparse


parser = argparse.ArgumentParser()
parser.add_argument("rlist", help="The list file to read")
parser.add_argument("ref", help="The .ref file to read")
parser.add_argument("denovo", help="The .denovo file to read")

args = parser.parse_args()

ofpath = args.rlist + ".uchime"
towrite = ""
refer_dict = {}
denovo_dict = {}

with open(args.ref) as refer:
    for line in refer:
        temp = line.strip('\n').split('\t')
        temp2 = temp[0].split(';')

        if temp[2] == 'Y':
            refer_dict[temp2[0]] = True
        else:
            refer_dict[temp2[0]] = False

with open(args.denovo) as refer2:
    for line in refer2:
        temp = line.strip('\n').split('\t')
        temp2 = temp[0].split(';')

        if temp[2] == 'perfect_chimera':
            denovo_dict[temp2[0]] = True
        else:
            denovo_dict[temp2[0]] = False

with open(args.rlist) as listfile:
    for line in listfile:
        temp = line.strip('\n').split('\t')
        if refer_dict[temp[3]] and denovo_dict[temp[3]]:
            tempstr = "{}\tCHIMERA\n".format(line.strip('\n'))
        else:
            tempstr = "{}\tnonCHIMERA\n".format(line.strip('\n'))
        towrite += tempstr

with open(ofpath, "w+") as outfile:
    outfile.write(towrite)

"""
Remove chimera entries from list
"""


import argparse


parser = argparse.ArgumentParser()
parser.add_argument("uchime", help="The list file to read")

args = parser.parse_args()

ofpath = args.uchime + "out"
towrite = ""

with open(args.uchime) as infile:
    for line in infile:
        temp = line.strip('\n').split('\t')
        if temp[-1] == 'nonCHIMERA':
            towrite += line

with open(ofpath, "w+") as outfile:
    outfile.write(towrite)

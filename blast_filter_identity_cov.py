"""
Filter blast output to those with
identity>=97% and coverage>=98%
"""


import argparse


parser = argparse.ArgumentParser()
parser.add_argument("blast", help="The blast output to filter")
parser.add_argument("fasta", help="The fasta file used as blast query")

args = parser.parse_args()

ofpath = args.blast + ".id0.97.cov0.8"
towrite = ""
fastadict = {}

with open(args.fasta) as infile:
    for line in infile:
        if line.startswith('>'):
            head = line.strip(">\n")
            fastadict[head] = ""
        fastadict[head] += line.strip('\n')

with open(args.blast) as infile:
    for line in infile:
        temp = line.strip('\n').split('\t')
        qlen = int(temp[7]) - int(temp[6]) + 1
        coverage = 100.0 * qlen / len(fastadict[temp[0]])
        if float(temp[2]) >= 97.0 and coverage >= 80.0:
            towrite += line

with open(ofpath, "w+") as outfile:
    outfile.write(towrite)

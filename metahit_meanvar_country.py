"""
Calculate the mean and variance for every genus in a metahit file divided by country
"""


import argparse
import statistics as st


def create_countrydict(a):
    newdict = {}
    ccode = "None"

    for i in range(len(a)):
        if a[i].find(ccode) == -1:
            ccode = a[i][:2]
            newdict[ccode] = [i + 1, i + 1]
        else:
            newdict[ccode][1] = (i + 1)

    return newdict


parser = argparse.ArgumentParser()
parser.add_argument("fpath", help="File path of the input file")

args = parser.parse_args()

with open(args.fpath) as infile:
    for line in infile:
        if line.startswith("\t"):
            parts = line.strip().split("\t")
            countrydict = create_countrydict(parts)
            continue
        parts = line.strip().split("\t")
        for k, v in countrydict.items():
            gendata = list(map(float, parts[v[0]:v[1] + 1]))
            genmean = st.mean(gendata)
            genvar = st.variance(gendata)
            print("The mean of genus {} in samples from {} is {}".format(parts[0], k, genmean))
            print("The variance of genus {} in samples from {} is {}".format(parts[0], k, genvar))

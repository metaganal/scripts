"""
Calculate the mean and variance for every genus in a metahit file
"""


import argparse
import statistics as st


parser = argparse.ArgumentParser()
parser.add_argument("fpath", help="File path of the input file")

args = parser.parse_args()

with open(args.fpath) as infile:
    for line in infile:
        if line.startswith("\t"):
            continue
        parts = line.strip().split("\t")
        gendata = list(map(float, parts[1:]))
        genmean = st.mean(gendata)
        genvar = st.variance(gendata)
        print("The mean and variance of genus {} is {} and {}".format(parts[0], genmean, genvar))

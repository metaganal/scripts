"""
Transpose a matrix in a file
"""

import argparse


parser = argparse.ArgumentParser()
parser.add_argument("mfile", help="File path of the matrix file")


args = parser.parse_args()

infile = open(args.mfile, mode="r+")

matrix = [map(int, line.split(' ')) for line in infile]

matrix = list(map(list, zip(*matrix)))

for i in range(len(matrix)):
    infile.write("{} {} {}\n".format(matrix[i][0], matrix[i][1], matrix[i][2]))

infile.close()

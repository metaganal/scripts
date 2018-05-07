#!/Users/felix/.pyenv/shims/python3
"""
Parse 2 fastq file and remove entries that aren't a pair
The name of output file will be *.fastq.N.rem.pair
"""


import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-1", dest="pair1", nargs='*', help="Path of file with read 1")
parser.add_argument("-2", dest="pair2", nargs='*', help="Path of file with read 2")
args = parser.parse_args()

if len(args.pair1) != len(args.pair2):
    print("Error: The number of *_1.fastq files and *_2.fastq files don't match")

for i in range(len(args.pair1)):
    ofpath1 = args.pair1[i] + ".pair"
    outfile1 = open(ofpath1, "w+")
    ofpath2 = args.pair2[i] + ".pair"
    outfile2 = open(ofpath2, "w+")
    head = []
    dict_read1 = {}
    dict_read2 = {}
    write1 = ""
    write2 = ""
    linecounter = 0

    with open(args.pair1[i], "r") as read1, open(args.pair2[i], "r") as read2:
        for line in read1:
            linecounter += 1
            if linecounter % 4 == 1:
                head = line.split(" ")
                dict_read1[head[1]] = [line]
            else:
                dict_read1[head[1]].append(line)
            if linecounter % 4 == 0:
                linecounter = 0
        for line in read2:
            linecounter += 1
            if linecounter % 4 == 1:
                head = line.split(" ")
                dict_read2[head[1]] = [line]
            else:
                dict_read2[head[1]].append(line)
            if linecounter % 4 == 0:
                linecounter = 0

    for key in dict_read1.keys() & dict_read2.keys():
            write1 += "".join(dict_read1[key])
            write2 += "".join(dict_read2[key])

    outfile1.write(write1)
    outfile2.write(write2)

    outfile1.close()
    outfile2.close()

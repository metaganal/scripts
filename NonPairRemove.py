#!/Users/felix/.pyenv/shims/python3
"""
Parse 2 fastq file and remove entries that aren't a pair
The name of output file will be *.fastq.N.rem.pair
"""


import argparse
import sys


parser = argparse.ArgumentParser()
parser.add_argument("-1", dest="pair1", nargs='*', help="Path of file with read 1")
parser.add_argument("-2", dest="pair2", nargs='*', help="Path of file with read 2")
args = parser.parse_args()

if len(args.pair1) != len(args.pair2):
    print("Error: The number of *_1.fastq files and *_2.fastq files")

for i in range(len(args.pair1)):
    ofpath1 = args.pair1[i] + ".pair"
    outfile1 = open(ofpath1, "w+")
    ofpath2 = args.pair2[i] + ".pair"
    outfile2 = open(ofpath2, "w+")
    head1 = []
    head2 = []
    index1 = []
    index2 = []

    with open(args.pair1[i], "r") as read1, open(args.pair2[i], "r") as read2:
        while True:
            line1 = read1.readline()
            line2 = read2.readline()

            if not line1 or not line2:
                break

            if line1.startswith('@', 0, 1):
                temp = line1.split(' ')
                if len(temp) != 1:
                    index1.append(read1.tell())
                    head1.append(temp)
            if line2.startswith('@', 0, 1):
                temp = line2.split(' ')
                if len(temp) != 1:
                    index2.append(read2.tell())
                    head2.append(temp)

        if len(head1) > len(head2):
            for i in range(len(head1)):
                for j in range(len(head2)):
                    if head1[i][1] == head2[j][1]:
                        read1.seek(index1[i], 0)
                        read2.seek(index2[j], 0)
                        sys.stdout.write(" ".join(head1[i]))
                        sys.stdout.write(" ".join(head2[j]))
                        outfile1.write(" ".join(head1[i]))
                        outfile2.write(" ".join(head2[j]))
                        for n in range(3):
                            line1 = read1.readline()
                            line2 = read2.readline()
                            outfile1.write(line1)
                            outfile2.write(line2)
        else:
            for i in range(len(head2)):
                for j in range(len(head1)):
                    if head2[i][1] == head1[j][1]:
                        read1.seek(index1[j], 0)
                        read2.seek(index2[i], 0)
                        outfile1.write(" ".join(head1[j]))
                        outfile2.write(" ".join(head2[i]))
                        for n in range(3):
                            line1 = read1.readline()
                            line2 = read2.readline()
                            sys.stdout.write(" ".join(head1[j]))
                            sys.stdout.write(" ".join(head2[i]))
                            outfile1.write(line1)
                            outfile2.write(line2)

    index1 = []
    index2 = []
    head1 = []
    head2 = []

    outfile1.close()
    outfile2.close()

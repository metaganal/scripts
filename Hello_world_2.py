"""
Print "Hello World" n times
"""

import argparse


parser = argparse.ArgumentParser("Print 'Hello World' n times")
parser.add_argument("integers", metavar="N", type=int, help="How many times 'Hello World' should be printed")


args = parser.parse_args()

ofile = open(r'/Users/felix/Hello_world_2.txt', "w+")

for i in range(args.integers):
    ofile.write("Hello World" + "\n")

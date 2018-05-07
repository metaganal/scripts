"""
Calculate the GCF from 2 integers
"""


import argparse


parser = argparse.ArgumentParser()
parser.add_argument("a", type=int, help="The first number")
parser.add_argument("b", type=int, help="The second number")

args = parser.parse_args()

x, y = args.a, args.b

if y > x:
    x, y = y, x

while y != 0:
    x, y = y, x % y

print("The GCF is {}".format(x))

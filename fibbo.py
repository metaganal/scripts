"""
Output the n+2 Fibbonaci number based on input (n)
"""


import argparse


parser = argparse.ArgumentParser()
parser.add_argument("integers", metavar="N", type=int, help="n")

args = parser.parse_args()

n = args.integers + 3

for i in range(n):
    if i == 0 or i == 1:
        a = 1
        b = 1
    else:
        a, b = b, a + b

print(b)

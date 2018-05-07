"""
Print a sequence of number up to n.
Replace numbers divisible by 3 with "Fizz", numbers divisible by 5 with "Buzz"
, and numbers divisible by both with "FizzBuzz"
"""

import argparse
import sys


parser = argparse.ArgumentParser()
parser.add_argument("integers", type=int, help="Last number for the sequence")

args = parser.parse_args()

n = args.integers + 1

for i in range(1, n):
    if i % 3 == 0 and i % 5 == 0:
        sys.stdout.write("FizzBuzz")
    elif i % 3 == 0:
        sys.stdout.write("Fizz")
    elif i % 5 == 0:
        sys.stdout.write("Buzz")
    else:
        sys.stdout.write("{}".format(i))
    sys.stdout.write(",")

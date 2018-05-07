"""
Print "Hello World" n times
"""

import argparse
import sys


parser = argparse.ArgumentParser("Print 'Hello World' n times")
parser.add_argument("integers", metavar="N", type=int, help="How many times 'Hello World' should be printed")


args = parser.parse_args()

for i in range(args.integers):
    sys.stdout.write("Hello World")

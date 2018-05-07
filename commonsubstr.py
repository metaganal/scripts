"""
Calculate the size of the longest common substring
"""


import argparse
import difflib


parser = argparse.ArgumentParser()
parser.add_argument("seq1", help="The first string")
parser.add_argument("seq2", help="The second string")

args = parser.parse_args()

s = difflib.SequenceMatcher(None, args.seq1, args.seq2)
match = s.find_longest_match(0, len(args.seq1), 0, len(args.seq2))

print(match.size)

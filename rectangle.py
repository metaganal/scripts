"""
Calculate the area and perimeter of a rectangle
"""

import argparse


parser = argparse.ArgumentParser()
parser.add_argument("side1", type=int, help="First side of the rectangle")
parser.add_argument("side2", type=int, help="Second side of the rectangle")


args = parser.parse_args()

area = args.side1 * args.side2
perimeter = 2 * (args.side1 + args.side2)

print('{}, {}'.format(area, perimeter))

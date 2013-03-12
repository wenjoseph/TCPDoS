#!/usr/bin/env python

import string
import random
import os
from argparse import ArgumentParser

parser = ArgumentParser(description="Generate HTTP Test Files")
parser.add_argument('--dir', '-d',
                    dest="dir",
                    action="store",
                    help="Directory to store outputs",
                    default="results",
                    required=True)

args = parser.parse_args()
DIR = args.dir
PACKAGE_SIZE = 1500

# Generate a random string
# SIZE is number of characters to generate
# CHARS is the range of characters to select from
def rand_string(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

def main():

  # Create output directory
  if not os.path.exists(DIR):
    os.makedirs(DIR)

  # Specify the sizes of files to generate (number of packages)
  sizes = range(1, 10, 1) + range(10, 100, 10) + range(100, 1000, 100)

  # Randomly generate ASCII characters for the specified sizes
  for size in sizes:
    filename = "%s/%s_Packages" % (DIR, size)
    outfile = open(filename, "w")
    outfile.write(rand_string(size * PACKAGE_SIZE))
    outfile.close()

if __name__ == '__main__':
  main()


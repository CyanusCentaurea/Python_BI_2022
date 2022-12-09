#!/usr/bin/env python3

import os
import sys
import shutil
import argparse
from argparse import RawDescriptionHelpFormatter

parser = argparse.ArgumentParser(description="""Simplified analogue of the mv utility <https://www.gnu.org/software/coreutils/mv>.\nMove (rename) files""", formatter_class=RawDescriptionHelpFormatter)
parser.add_argument('src', nargs='+', help='source')
parser.add_argument('dst', help='destination')
args = parser.parse_args()


def mv(src, dst):
    for file in src:
        os.popen(f'mv {file} {dst}')

def main():
    mv(args.src, args.dst)


if __name__ == '__main__':
    main()

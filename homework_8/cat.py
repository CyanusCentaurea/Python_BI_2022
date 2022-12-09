#!/usr/bin/env python3

import os
import sys
import argparse
from argparse import RawDescriptionHelpFormatter

parser = argparse.ArgumentParser(description="""Simplified analogue of the cat utility <https://www.gnu.org/software/coreutils/cat>.\nConcatenate files and print on the standard output.\nWith no FILE, read standard input.""", formatter_class=RawDescriptionHelpFormatter)
parser.add_argument('files', nargs='*',  help='Input files')
if parser.parse_args().files:
        args = parser.parse_args()
        input_type = 'files'
else:
    input_type = 'stdin'


def cat(*files):
    for file in files:
        with open(file) as file:
            for line in file:
                print(line.strip())


def main():
    if input_type == 'files':
        for file in args.files:
            if not os.path.exists(file):
                print(f'Cannot read {file}: no such file or directory')
                sys.exit(1)
            elif os.path.isdir(file):
                print(f'{file}: is a directory')
                sys.exit(1)
        cat(*args.files)
    else:
        for line in sys.stdin:
            print(line.strip())


if __name__ == '__main__':
    main()

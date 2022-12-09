#!/usr/bin/env python3

import os
import sys
import argparse
from argparse import RawDescriptionHelpFormatter

parser = argparse.ArgumentParser(description="""Simplified analogue of the sort utility <https://www.gnu.org/software/coreutils/sort>.\nWrite sorted concatenation of all FILE(s) to standard output.\nWith no FILE, read standard input.""", formatter_class=RawDescriptionHelpFormatter)
parser.add_argument('files', nargs='*',  help='Input files')
if parser.parse_args().files:
        args = parser.parse_args()
        input_type = 'files'
else:
    input_type = 'stdin'


def sort_files(*files):
    res = []
    for file in files:
        with open(file) as file:
            for line in file:
                if line.strip() == "":
                    break
                else:
                    res.append(line.strip())
    res.sort()
    return res


def main():
    if input_type == 'files':
        for file in args.files:
            if not os.path.exists(file):
                print(f'Cannot read {file}: no such file or directory')
                sys.exit(1)
        res = sort_files(*args.files)
    else:
        res = [line.strip() for line in sys.stdin.readlines()]
        res.sort()
    print(*res, sep="\n")


if __name__ == '__main__':
    main()


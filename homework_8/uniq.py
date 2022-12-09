#!/usr/bin/env python3

import os
import sys
import argparse
from argparse import RawDescriptionHelpFormatter

parser = argparse.ArgumentParser(description="""Simplified and modified analogue of the uniq utility <https://www.gnu.org/software/coreutils/uniq>.\nReport or omit repeated lines""", formatter_class=RawDescriptionHelpFormatter)
parser.add_argument('files', nargs='*',  help='Input files')
if parser.parse_args().files:
        args = parser.parse_args()
        input_type = 'files'
else:
    input_type = 'stdin'


def uniq(*files):
    res = {}
    for file in files:
        with open(file) as file:
            line = file.readline().strip()
            while line:
                res[line] = None
                line = file.readline().strip()
    return res


def main():
    if input_type == 'files':
        for file in args.files:
            if not os.path.exists(file):
                print(f'Cannot read {file}: no such file or directory')
                sys.exit(1)
            elif os.path.isdir(file):
                print(f'read error: {file} is a directory')
                sys.exit(1)
        res = uniq(*args.files)
    else:
        res = {line.strip(): None for line in sys.stdin.readlines()}
    for elem in res:
        print(elem)


if __name__ == '__main__':
    main()

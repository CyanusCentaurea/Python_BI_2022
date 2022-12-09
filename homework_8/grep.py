#!/usr/bin/env python3

import re
import os
import sys
import argparse
from argparse import RawDescriptionHelpFormatter

parser = argparse.ArgumentParser(description="""Simplified analogue of the grep utility <https://www.gnu.org/software/coreutils/grep>.\nPrint lines that match patterns.\nWith no FILE, read standard input.""", formatter_class=RawDescriptionHelpFormatter)
parser.add_argument('pattern',  help='Pattern for search')
parser.add_argument('files', nargs='*',  help='Input files')
if parser.parse_args().files:
        args = parser.parse_args()
        input_type = 'files'
else:
    input_type = 'stdin'
pattern = parser.parse_args().pattern


def grep(*files):
    errors = []
    for file in files:
        try:
            with open(file) as f:
                line = f.readline().strip()
                while line:
                    if re.findall(pattern, line):
                        if len(files) > 1:
                            print(f'{file}:{line}')
                        else:
                            print(line)
                    line = f.readline().strip()
        except (IsADirectoryError, FileNotFoundError) as error:
            print(error)


def main():
    if input_type == 'files':
        grep(*args.files)
    else:
        for line in sys.stdin:
            if re.findall(pattern, line):
                print(line.strip())


if __name__ == '__main__':
    main()            

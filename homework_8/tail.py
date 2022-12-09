#!/usr/bin/env python3

import os
import sys
import argparse
from argparse import RawDescriptionHelpFormatter

parser = argparse.ArgumentParser(description="""Simplified analogue of the tail utility <https://www.gnu.org/software/coreutils/tail>.\nOutput the last part of files""", formatter_class=RawDescriptionHelpFormatter)
parser.add_argument('files', nargs='*',  help='Input files')
parser.add_argument('-n', '--lines', help='output the last NUM lines, instead of the last 10', default=10)
if parser.parse_args().files:
        args = parser.parse_args()
        input_type = 'files'
else:
    input_type = 'stdin'


def tail(*files):
    for file in files:
        if os.path.exists(file) and os.path.isfile(file):
            print(f'==> {file} <==')
        sys.stdout.write(os.popen(f'tail -n {parser.parse_args().lines} {file}').read())


def main():
    if input_type == 'files':
        tail(*args.files)
    else:
        sys.stdout.write(os.popen(f'tail -n {parser.parse_args().lines}').read())

if __name__ == '__main__':
    main()


#!/usr/bin/env python3

import sys
import os
import argparse
from argparse import RawDescriptionHelpFormatter

parser = argparse.ArgumentParser(description="""Simplified analogue of the mkdir utility <https://www.gnu.org/software/coreutils/mkdir>.\nMake directories""", formatter_class=RawDescriptionHelpFormatter)
parser.add_argument('files', nargs='*',  help='Input directories')
parser.add_argument('-p', '--parents', action='store_true', help='no error if existing, make parent directories as needed')
args = parser.parse_args()

def mkdir(file):
    if args.parents:
        os.popen(f'mkdir -p {file}')
    else:
        os.popen(f'mkdir {file}')


def main():
    if not args.files:
        print("mkdir: missing operand")
        print("Try 'mkdir --help' for more information")
        sys.exit(1)
    for file in args.files:
        mkdir(file)

if __name__ == '__main__':
    main()

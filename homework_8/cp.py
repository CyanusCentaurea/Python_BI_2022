#!/usr/bin/env python3

import os
import sys
import shutil
import argparse
from argparse import RawDescriptionHelpFormatter

parser = argparse.ArgumentParser(description="""Simplified analogue of the cp utility <https://www.gnu.org/software/coreutils/cp>.\nCopy files or directories""", formatter_class=RawDescriptionHelpFormatter)
parser.add_argument('src', nargs='+', help='source')
parser.add_argument('dst', help='destination')
parser.add_argument('-r', '--recursive', action='store_true', help='copy directories recursively')


def cp(src, dst):
    for file in src:
        if not parser.parse_args().recursive and os.path.isdir(file):
            print(f'-r not specified; omitting directory {file}')
            sys.exit(1)
        elif parser.parse_args().recursive and os.path.isdir(file):
            os.popen(f'cp -r {file} {dst}')
            # слишком поздно нашла os.popen, зато сразу видно, что делала точно сама и одна )))
        else:
            shutil.copy(file, dst)


def main():
    cp(parser.parse_args().src, parser.parse_args().dst)


if __name__ == '__main__':
    main()

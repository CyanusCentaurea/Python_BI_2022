#!/usr/bin/env python3

import os
import shutil
import argparse
from argparse import RawDescriptionHelpFormatter

parser = argparse.ArgumentParser(description="""Simplified analogue of the rm utility <https://www.gnu.org/software/coreutils/rm>.\nRemove files or directories""", formatter_class=RawDescriptionHelpFormatter)
parser.add_argument('files', nargs='*',  help='Input files or directories')
parser.add_argument('-r', '--recursive', action='store_true', help='remove directories and their contents recursively')

def rm(*args):
    errors = []
    if parser.parse_args().recursive:
        for arg in args:
            try:
                shutil.rmtree(arg)
            except FileNotFoundError as e:
                errors.append(e)
                pass
    else:
        for arg in args:
            try:
                os.remove(arg)
            except FileNotFoundError as error:
                errors.append(error)
                pass
    for error in errors:
        print(f'{error}, cannot remove it')


def main():
    args = parser.parse_args()
    rm(*args.files)


if __name__ == '__main__':
    main()


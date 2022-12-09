#!/usr/bin/env python3

import os
import argparse
from argparse import RawDescriptionHelpFormatter

parser = argparse.ArgumentParser(description="""Simplified analogue of the ls utility <https://www.gnu.org/software/coreutils/ls>.\nList information about the FILEs (the current directory bydefault).""", formatter_class=RawDescriptionHelpFormatter)
parser.add_argument('paths', nargs='*',  help='Input directories', default=[os.getcwd()])
parser.add_argument('-a', '--all', action='store_true', help='do not ignore entries starting with .')

def ls(*args):
    errors = []
    for arg in args:
        if os.path.exists(arg):
            if len(parser.parse_args().paths) > 1:
                print(f'{arg}:')
            if parser.parse_args().all:
                print(*sorted(os.listdir(arg)))
            else:
                print(*sorted(list(filter(lambda x: not x.startswith('.'), os.listdir(arg)))))
        else:
            errors.append(f'No such file or directory: {arg}')
    for error in errors:
        print(error)


def main():
    args = parser.parse_args()
    ls(*args.paths)


if __name__ == '__main__':
    main()


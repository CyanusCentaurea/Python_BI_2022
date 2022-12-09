#!/usr/bin/env python3

import os
import sys
import argparse
from argparse import RawDescriptionHelpFormatter

parser = argparse.ArgumentParser(description="""Simplified analogue of the wc utility <https://www.gnu.org/software/coreutils/wc>.\nPrint newline, word, and byte counts for each FILE, and a total line if more than one FILE is specified.\nWith no FILE, reads standard input. A word is a non-zero-length sequence of characters delimited by white space.\nThe options below may be used to select which counts are printed, always in the following order: newline, word, byte.""", formatter_class=RawDescriptionHelpFormatter)
parser.add_argument('files', nargs='*',  help='Input files')
parser.add_argument('-c', '--bytes', action='store_true', help='print the byte counts')
parser.add_argument('-l', '--lines', action='store_true', help='print the newline counts')
parser.add_argument('-w', '--words', action='store_true', help='print the word counts')

if parser.parse_args().files:
    input_type = 'files'
else:
    input_type = 'stdin'

counts = []
if  parser.parse_args().lines or parser.parse_args().bytes + parser.parse_args().lines + parser.parse_args().words == 0:
    counts.append('lines')
if  parser.parse_args().words or parser.parse_args().bytes + parser.parse_args().lines + parser.parse_args().words == 0:
    counts.append('words')
if parser.parse_args().bytes or parser.parse_args().bytes + parser.parse_args().lines + parser.parse_args().words == 0:
    counts.append('bytes')


def wc(*args):
    res = {}
    errors = []
    for arg in args:
        if input_type == 'files':
            if os.path.exists(arg):
                res[arg] = {count: 0 for count in counts}
                with open(arg, 'rb') as file:
                    for line in file:
                        if 'bytes' in counts:
                            res[arg]['bytes'] += len(line)
                        if  'lines' in counts:
                            res[arg]['lines'] += 1 if line.endswith(b"\n") else 0
                        if  'words' in counts:
                            res[arg]['words'] += len(line.split())
            else:
                errors.append(f'No such file or directory: {arg}')
        else:
            res[arg] = {count: 0 for count in counts}
            for line in args:
                if 'bytes' in counts:
                    res[arg]['bytes'] += len(line.encode('utf-8'))
                if 'lines' in counts:
                    res[arg]['lines'] += 1 if line.endswith("\n") else 0
                if 'words' in counts:
                    res[arg] ['words'] += len(line.split())
    if input_type == 'files':
        for arg in res:
            for count in res[arg]:
                print(res[arg][count], end=' ')
            print(arg)
    else:
         print(*list(res[arg][count] for count in counts))
    for error in errors:
        print(error)
    return res


def main():
    if input_type == 'files':
        args = parser.parse_args()
        res = wc(*args.files)
        if len(args.files) > 1:
            total_counts = []
            if  'lines' in counts:
                total_counts.append(sum(res[file]['lines'] for file in res))
            if  'words' in counts:
                total_counts.append(sum(res[file]['words'] for file in res))
            if 'bytes' in counts:
                total_counts.append(sum(res[file]['bytes'] for file in res))
            print(*total_counts, 'total')
    else:
        args = (sys.stdin.readlines())
        res = wc(*args)


if __name__ == '__main__':
    main()


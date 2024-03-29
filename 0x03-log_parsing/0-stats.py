#!/usr/bin/python3
"""
Module: Reads stdin line by line and computes metrics
"""
import sys


def print_status(dic, size):
    """ Prints information """
    print("File size: {:d}".format(size))
    for i in sorted(dic.keys()):
        if dic[i] != 0:
            print("{}: {:d}".format(i, dic[i]))


count = 0
size = 0
status_codes = {'200': 0,
                '301': 0,
                '400': 0,
                '401': 0,
                '403': 0,
                '404': 0,
                '405': 0,
                '500': 0}

try:
    for line in sys.stdin:
        if count != 0 and count % 10 == 0:
            print_status(status_codes, size)

        stlist = line.split()
        count += 1

        try:
            size += int(stlist[-1])
        except Exception:
            pass

        try:
            if stlist[-2] in status_codes:
                status_codes[stlist[-2]] += 1
        except Exception:
            pass
    print_status(status_codes, size)


except KeyboardInterrupt:
    print_status(status_codes, size)
    raise

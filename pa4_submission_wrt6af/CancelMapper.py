#!/usr/bin/env python3

from csv import reader
import sys

def check_float(potential_float):
    try:
        float(potential_float)
        return True
    except ValueError:
        return False

# input comes from STDIN (standard input)
for line in reader(sys.stdin):
    # split the line into words
    cancelled = line[13]
    if cancelled == '1.00':
        print("{0}".format(line[14]))
    # increase counters

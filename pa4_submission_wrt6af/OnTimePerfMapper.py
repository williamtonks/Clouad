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
    airline = line[1]
    delay = line[12]
    valid = check_float(delay)
    if valid == False:
        delay = '0.00'
    print("{0}\t{1}".format(airline, delay))
    # increase counters

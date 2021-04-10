#!/usr/bin/env python3

from operator import itemgetter
import sys

current_reason = None
reason = None
route_number_of_cancels = 0.0

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    reason = line.strip()

    # parse the input we got from mapper.py
    # by key (here: word) before it is passed to the reducer
    if current_reason == reason:
        route_number_of_cancels += 1
    else:
        if current_reason:
            # write result to STDOUT
            print("{0}\t{1}".format(current_reason, route_number_of_cancels))
        current_reason = reason
        route_number_of_cancels = 1

# do not forget to output the last word if needed!
if current_reason == reason:
    print("{0}\t{1}".format(current_reason, route_number_of_cancels))

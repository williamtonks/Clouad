#!/usr/bin/env python3

from operator import itemgetter
import sys

current_route = None
route = None
route_total_delay = 0.0
route_number_of_flights = 0.0

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    route, delay = line.split('\t', 1)

    # convert count (currently a string) to int
    try:
        delay = float(delay)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_route == route:
        route_total_delay += delay
        route_number_of_flights += 1
    else:
        if current_route:
            # write result to STDOUT
            average = route_total_delay / route_number_of_flights
            print("{0}\t{1}".format(current_route, average))
        current_route = route
        route_total_delay = delay
        route_number_of_flights = 1

# do not forget to output the last word if needed!
if current_route == route:
    average = route_total_delay / route_number_of_flights
    print("{0}\t{1}".format(current_route, average))

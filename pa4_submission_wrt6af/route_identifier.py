#!/usr/bin/env python3

from operator import itemgetter
import sys

current_airline = None
airline = None
the_routes = {}
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    airline_route, average_delay = line.split('\t', 1)
    airline, route = airline_route.split(':', 1)

    # convert count (currently a string) to int
    try:
        average_delay = float(average_delay)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue
    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_airline == airline:
        the_routes.update({route: average_delay})
    else:
        if current_airline:
            x = sorted(the_routes.items(), key=itemgetter(1))
            print(current_airline)
            for i in range(1,16):
                print(x[-i])
        current_airline = airline
        the_routes.clear()
        the_routes.update({route: average_delay})

# do not forget to output the last word if needed!
if current_airline == airline:
    x = sorted(the_routes.items(), key=itemgetter(1))
    print(current_airline)
    for i in range(1,16):
        print(x[-i])
    #print("{0}\t{1}".format(current_route, average))

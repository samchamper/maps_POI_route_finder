# Some functions that take a list of points of interest and construct
# a route whereby you can visit the most possible points of interest
# given a certain maximum travel distance.

import math

def route(lat, long, max_dist, poi_list):
    # Convert from meters to radians:
    rad_dist = max_dist * math.cos(lat) / 111320

    graph = makegraph(poi_list)

    return 0

def makegraph(poi_list):
    return 0
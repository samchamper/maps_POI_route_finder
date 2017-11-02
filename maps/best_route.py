# Some functions that take a list of points of interest and construct
# a route whereby you can visit the most possible points of interest
# given a certain maximum travel distance.

import math

routelist = []


def route(lat, long, max_dist, poi_list):
    global routelist
    # Convert from meters to radians:
    rad_dist = max_dist * math.cos(lat) / 111320
    # Initialize routelist with a single element which is the route
    # consisting of only the starting location.
    routelist = [(lat, long)]
    all_routes((lat, long), rad_dist, poi_list, [])

    # Trim away all routes that don't traverse the most pois possible
    longest = keep_longest_routes(routelist)

    # Among the remaining routes with the max number of pois, select
    # the route with the shortest length.
    best = choose_shortest_route(longest, rad_dist)

    # Return the list of points in the best route.
    return best


def all_routes(cur_loc, dist_remaining, poi_list, visited):
    """
    Recursive search (DFS) to find routes from cur_loc to everywhere else
    in poi list which are of the greatest length possible.
    :param cur_loc: tupple with (lat, long).
    :param dist_remaining: distance we can travel.
    :param poi_list: list of tuples of form (lat, long).
    :param visited: The places we've visited thus far on this current route.
    """
    # Add our current location to our list of visited places for this route.
    global routelist
    visited.append(cur_loc)
    if len(visited) >= len(routelist[len(routelist) - 1]):
        # If this route has at least as many points as the previous route
        # in the routelist, add this route. No point in keeping shorter routes.
        routelist.append(visited)
    for poi in poi_list:
        if poi not in visited:
            distance = math.hypot(cur_loc[0] - poi[0], cur_loc[1] - poi[1])
            if distance <= dist_remaining:
                # If we can travel far enough to reach the node,
                # try to find routes from that node
                all_routes(poi, dist_remaining - distance, poi_list, visited[:])


def keep_longest_routes(ls):
    # The last item in the route list is necessarily tied with the longest.
    longest = []
    maxlen = len(ls[-1])
    for i in ls:
        if len(i) == maxlen:
            longest.append(i)
    return longest


def choose_shortest_route(ls, rad_dist):
    min_dist = rad_dist
    shortest_path = []
    for path in ls:
        path_length = 0
        for j in range(1, len(path)):
            # Sum the distances between the points in the route.
            path_length += math.hypot(path[j][0] - path[j-1][0], path[j][1] - path[j-1][1])
        if path_length < min_dist:
            # Remember the shortest path
            min_dist = path_length
            shortest_path = path
    # The first entry of all routes in the routes dict is our start
    # location, which is not actually a poi, so trim it off.
    return shortest_path[1:]

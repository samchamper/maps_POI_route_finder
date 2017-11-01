# Some functions to preprocess csv file into a
# python data structure and to crop the list based
# on user selections.

import math


def make_list(filename):
    """
    Make the initial python list by reading the csv file.
    :param filename: path to csv file
    :return: a python list of lats, longs, and destination type
    """
    # with open(filename) as f:
    pois = []
    file = open(filename, 'r')
    for line in file:
        ls = line.split(",")
        entry = ((float(ls[1]), float(ls[2])), int(ls[3]))
        pois.append(entry)
    return pois


def filter(full_poi_list, type_of_poi):
    """
    Filter the full list based on the type of poi we are
    interested in
    :return: a filtered list with just latitudes and logitudes.
    """
    pois = []
    if type_of_poi == "all":
        for i in full_poi_list:
            entry = i[0]
            pois.append(entry)
    if type_of_poi == "gym":
        for i in full_poi_list:
            if i[1] == 2:
                entry = i[0]
                pois.append(entry)
    return pois


def crop(pois, lat, long, max_dist):
    """
    Crop a list to points that are within a
    maximum distance of a center point.
    :param pois: list of lats and longs
    :param lat: center lat
    :param long: center long
    :param max_dist: max distance
    :return: a filtered list
    """
    # Convert from meters to radians:
    rad_dist = max_dist * math.cos(lat) / 111320
    crop_list = []
    for i in pois:
        if math.hypot(lat-i[0], long - i[1]) <= rad_dist:
            crop_list.append(i)
    return crop_list

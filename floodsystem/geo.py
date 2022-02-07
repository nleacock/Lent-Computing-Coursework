# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from distutils.command import build
from .utils import sorted_by_key  # noqa
from .station import MonitoringStation
from .stationdata import build_station_list
from haversine import haversine, Unit
def stations_by_distance(stations, p):
    stations_distance_list = []
    for i in stations:
        distance = haversine(i.coord, p)
        t = (i.name, i.town, distance)
        stations_distance_list.append(t)
    sortedlist = sorted_by_key(stations_distance_list, 2)
    return sortedlist

def stations_within_radius(stations, centre, r):
    """""This function returns a list of all stations within radius r
    of a geographical coordinate x"""
    #create empty list of stations
    within_radius_list = []
    #calculate distance of station from x
    for i in stations:
        dist = haversine(i.coord, centre)
        #if distance to x is less than r, add station name to the list
        if dist <= r:
            within_radius_list.append(i.name)
    
    return within_radius_list
        
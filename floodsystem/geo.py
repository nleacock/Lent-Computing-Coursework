# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

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
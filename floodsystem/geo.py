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
        
rivers = set()
def rivers_with_stations(stations):
    #runs through every river and adds them to a list
    for i in stations:
        rivers.add(i.river)
    return rivers

def stations_by_river(stations):
    dictionary = {}
    #for each river in the list of rivers
    for i in rivers:
        stationsonriver = []
        #test every station for the selected river
        for j in stations:
            #check if selected station is on the river of the selected river - add station to the list if yes
            if j.river == i:
                #adds station to the list of stations that lie on selected river
                stationsonriver.append(j.name)
            else:
                #nothing happens and returns to the loop for the next stations
                arbitrary = 0
        #adds the river and its corresponding stations to the dictionary
        stationsonriver.sort()
        dictionary[i] = stationsonriver
    return dictionary

def rivers_by_station_number(stations, N):
    """""""function that determines the N number of rivers with greatest monitoring stations, returning a list of river-station tuples, sorted by number of stations"""""""
    """""""if more rivers with same no of stations than Nth entry, include these other rivers"""""""
    #use 1d function to create dictionary with rivers as keys and corresponding stations
    dictionary2 = stations_by_river(stations)
    print(dictionary2)
    #go through each river and make a list of the number of stations per river, in descending order
    req_rivers = []
    stations_per_river = []
    for river in dictionary2:
        stations_per_river.append(len(dictionary2[river]))
    sorted_stations_per_river = sorted(stations_per_river)
    sorted_stations_per_river.reverse()
    #set the minimum no of stations to be included, based on N inputted
    min_station_number = sorted_stations_per_river[N-1]
    #go back to original dictionary and find the corresponding rivers and create list
    for river in dictionary2:
        if len(dictionary2[river]) >= min_station_number:
            req_rivers.append(river, len(dictionary2[river]))
    final_list = sorted_by_key(req_rivers,1)
    final_list.reverse()
    
    return final_list
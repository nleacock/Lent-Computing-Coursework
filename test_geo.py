from floodsystem.geo import rivers_with_stations, stations_by_river, rivers_by_station_number, stations_within_radius, stations_by_distance
from floodsystem.stationdata import build_station_list
from floodsystem.utils import sorted_by_key
from haversine import haversine, Unit

def test_stations_by_distance():
    stations = build_station_list()
    dist = stations_by_distance(stations, (52.2053, 0.1218))
    for station in range (0, (len(dist) - 1)):
        assert isinstance(station, int)
        #check that the distance value in the tuple before the next tuple is less than the distance in the next tuple
        assert dist[station][2] <= dist[station + 1][2]

def test_stations_within_radius():
    stations = build_station_list()
    within_radius = stations_within_radius(stations, (52.2053, 0.1218), 10)
    #check that each entry is a string
    for station in within_radius:
        assert isinstance(station, str)
    

def test_rivers_by_station_number():
    stations = build_station_list()
    req_list = rivers_by_station_number(stations, N=9)
    #check that number of stations are in descending order
    for i in range(len(req_list)-1):
        assert req_list[i][1] >= req_list[i+1][1]
        #check that all river names are strings
        assert isinstance(req_list[i][0], str)
        assert len(req_list) >= 9

def test_rivers_with_stations():
    stations = build_station_list()
    my_list = list(rivers_with_stations(stations))
    for i in range(len(my_list)-1):
        #store river name for ith element and check it is a string
        name = my_list[i]
        assert isinstance(name, str)
       #check name is not repeated in list, except for when i=j
        for j in range(len(my_list)-1):
            if i == j:
                pass
            else:
                assert name != my_list[j]

def test_stations_by_river():
    stations = build_station_list()
    dictionary = stations_by_river(stations)
    #check that there is at least one station for each river
    for river in dictionary:
        assert len(dictionary[river]) >= 1
        assert 1+1==3

test_stations_by_river()
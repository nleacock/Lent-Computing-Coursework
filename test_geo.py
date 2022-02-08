from floodsystem.geo import rivers_with_stations, stations_by_river, rivers_by_station_number, stations_within_radius
from floodsystem.stationdata import build_station_list
from floodsystem.utils import sorted_by_key
from haversine import haversine, Unit

def test_stations_within_radius():
    stations = build_station_list()
    within_radius = stations_within_radius(stations, (52.2053, 0.1218), 10)
    #check that each entry is a string
    for station in within_radius:
        assert isinstance(station, str)
    

def test_rivers_by_station_number():
    stations = build_station_list()
    req_list = rivers_by_station_number(stations, N=9)
    print(req_list)
    #check that number of stations are in descending order
    for i in range(len(req_list)-1):
        assert req_list[i][1] >= req_list[i+1][1]
    

test_rivers_by_station_number()
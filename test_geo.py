from floodsystem.geo import rivers_with_stations, stations_by_river, rivers_by_station_number, stations_within_radius
from floodsystem.stationdata import build_station_list
from floodsystem.utils import sorted_by_key

def test_stations_within_radius():
    stations = build_station_list()
    within_radius = stations_within_radius(stations)
    #check that each entry is a string
    for station in within_radius:
        assert isinstance(station, str)




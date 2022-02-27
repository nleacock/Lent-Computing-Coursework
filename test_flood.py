from floodsystem.flood import stations_highest_rel_level, stations_level_over_threshold
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import update_water_levels, build_station_list


def test_stations_level_over_threshold():
    stations = build_station_list()
    update_water_levels(stations)
    desired_stations = stations_level_over_threshold(stations, 0.5)
    #check resulting list of tuples of station and water level
    for i in range(0, len(desired_stations)-1):
        #check type
        assert isinstance(desired_stations[i], tuple)
        assert isinstance(desired_stations[i][0], MonitoringStation)
        assert isinstance(desired_stations[i][1], float)
        #check that water levels are above tol
        assert desired_stations[i][1] >= 0.5
        #ensure order of descending rel water level
        assert desired_stations[i][1] >= desired_stations[i+1][1]





def test_stations_highest_rel_level():
    stations = build_station_list()
    update_water_levels(stations)
    desired_stations = stations_highest_rel_level(stations, N=10)
    #check resulting list of tuples of station and water level
    for i in range(0, len(desired_stations)-1):
        #check type
        assert isinstance(desired_stations[i], tuple)
        assert isinstance(desired_stations[i][0], MonitoringStation)
        assert isinstance(desired_stations[i][1], float)
        #check that length of list is the same as N=10
        assert len(desired_stations) == 10
        #ensure order of descending rel water level
        assert desired_stations[i][1] >= desired_stations[i+1][1]


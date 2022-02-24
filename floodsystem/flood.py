from floodsystem.station import MonitoringStation
from floodsystem.utils import sorted_by_key

def stations_level_over_threshold(stations, tol):
    list_of_tuples = []
    for station in stations:
        if station.relative_water_level() == None:
            pass
        elif station.relative_water_level() > tol:
            tuple = (station, station.relative_water_level())
            list_of_tuples.append(tuple)
        else:
            pass
    sorted_list = sorted_by_key(list_of_tuples, 1, reverse=True)
    return sorted_list


def stations_highest_rel_level(stations, N):
    """""""take the code from 2B and chop off the first N terms, i.e. generate a list of the N stations with the highest relative levels"""""""
    total_list = stations_level_over_threshold(stations, -786)
    new_list = []
    for i in range(0,N):
        new_list.append(total_list[i])

    return new_list
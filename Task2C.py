

from floodsystem.utils import sorted_by_key
from floodsystem.stationdata import build_station_list


def stations_highest_rel_level(stations, N):
    """""""take the code from 2B and chop off the first N terms, i.e. generate a list of the N stations with the highest relative levels"""""""
    #create list of tuples of stations with their relative levels
    new_list = []
    for station in stations:
        new_list.append((station, station.relative_water_level))
    #sort list of tuples in decreasing relative water level order
    sorted_list = sorted_by_key(new_list, 1, reverse=True)
    #keep only the first N entries in the list
    for i in range(N, len(sorted_list)+1):
        sorted_list.pop(i)

    return sorted_list

def run():
    stations = build_station_list()
    at_risk = stations_highest_rel_level(stations, 10)
    print(at_risk)

if __name__ == "__main__":
    run()
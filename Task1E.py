from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list

def run():
    """""""run function from geo for 1e, with N = 9"""""""
    stations = build_station_list()
    relevant_list = rivers_by_station_number(stations, 9)

    print(relevant_list)


run()    
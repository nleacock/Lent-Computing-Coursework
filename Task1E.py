from floodsystem.geo import rivers_with_stations, stations_by_river, rivers_by_station_number
from floodsystem.stationdata import build_station_list
from floodsystem.utils import sorted_by_key


def run():
    
    stations = build_station_list()
    relevant_list = rivers_by_station_number(stations, 9)
    print(relevant_list)

if __name__ == "__main__":
    run()



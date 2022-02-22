from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold
from floodsystem.utils import sorted_by_key
def run():
    stations = build_station_list()
    update_water_levels(stations)
    stationsover = stations_level_over_threshold(stations, 0.8)
    for element in stationsover:
        print(element[0], element[1])


if __name__ == "__main__":
    run()
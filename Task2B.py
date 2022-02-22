from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_level_over_threshold
def run():
    stations = build_station_list()
    stationsover = stations_level_over_threshold(stations, 0.8)
    print(stationsover)

if __name__ == "__main__":
    run()
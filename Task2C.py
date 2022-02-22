from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
def run():
    stations = build_station_list()
    update_water_levels(stations)
    at_risk = stations_highest_rel_level(stations, 10)
    print(at_risk)

if __name__ == "__main__":
    run()
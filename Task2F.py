from floodsystem.geo import build_station_list
from floodsystem.stationdata import update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import polyfit
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.flood import stations_highest_rel_level

def run():
    stations = build_station_list()
    update_water_levels(stations)
    #obtain list of 5 stations for which the relative level is highest
    desired_stations = stations_highest_rel_level(stations, 5)
    for station in desired_stations:
        






if __name__ == "__main__":
    run()
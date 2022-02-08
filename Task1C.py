from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list

def run():
    """""""use function for task 1c, find for 10km within ccc, print station names in alphabetical order"""""""
    stations = build_station_list()
    ccc = (52.2053, 0.1218)
    stations_within_10km_of_ccc = stations_within_radius(stations, ccc, 10)
    stations_within_10km_of_ccc.sort()
    
    print(stations_within_10km_of_ccc)

if __name__ == "__main__":
    run()
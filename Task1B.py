from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list


def run():
    stations = build_station_list()
    ccc = (52.2053, 0.1218)
    stationdistances = stations_by_distance(stations, ccc)
    print("--10 Closest stations to Cambridge City Centre--")
    print(stationdistances[:10])
    print("--10 Furthest stations to Cambridge City Centre--")
    print(stationdistances[-10:])

if __name__ == "__main__":
    run()
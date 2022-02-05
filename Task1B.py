from distutils.command.build import build
from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation
#stations_by_distance(build_station_list(), )
def IB():
    stations = build_station_list()
    ccc = (52.2053, 0.1218)
    stationdistances = stations_by_distance(stations, ccc)
    print("--10 Closest stations to Cambridge City Centre--")
    print(stationdistances[:10])
    print("--10 Furthest stations to Cambridge City Centre--")
    print(stationdistances[-10:])

IB()
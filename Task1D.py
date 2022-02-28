from floodsystem.geo import rivers_with_stations, stations_by_river
from floodsystem.stationdata import build_station_list

def run():
    stations = build_station_list()
    riverswithstations = rivers_with_stations(stations)
    rivers = list(riverswithstations)
    rivers.sort()
    print("Number of stations:")
    print(len(rivers))
    print("First 10 stations in alphabetical order:")
    print(rivers[:10])

    dictionary = stations_by_river(stations)
    print(" ========== \n Names of stations on the River Aire: \n ==========")
    print(dictionary['River Aire'])
    print(" ========== \n Names of stations on the River Cam: \n ==========")
    print(dictionary['River Cam'])
    print(" ========== \n Names of stations on the River Thames: \n ==========")
    print(dictionary['River Thames'])
if __name__ == "__main__":
    run()


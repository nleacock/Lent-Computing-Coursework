from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations

def run():
    stations = build_station_list()
    inconsistentstations = inconsistent_typical_range_stations(stations)
    stationnames = [i.name for i in inconsistentstations]
    stationnames.sort()
    print(stationnames)

if __name__ == "__main__":
    run()
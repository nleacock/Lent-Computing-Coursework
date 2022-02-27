from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list

def run():
    
    stations = build_station_list()
    relevant_list = rivers_by_station_number(stations, 9)
    print(relevant_list)

if __name__ == "__main__":
    run()



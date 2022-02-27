from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold
from floodsystem.utils import sorted_by_key
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.station import MonitoringStation
from datetime import datetime, timedelta
def run():
    stations = build_station_list()
    update_water_levels(stations)
    desired_stations = stations_level_over_threshold(stations, 0)

    dt = 10
    counter = 0
    for station in desired_stations:
        #return water level history, and skips if these lists are empty, like Letcombe Bassett
        dates, levels = fetch_measure_levels(station[0].measure_id, dt=timedelta(days=dt))
        if dates == [] or levels == []:
            pass
        else:
            plot_water_levels(station[0], dates, levels)
            counter += 1
            if counter > 4:
                break
        
        
if __name__ == "__main__":
    run()
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
    dt = 10

    for i in range (0, 5):
        dates, levels = fetch_measure_levels(stations[i].measure_id, dt=timedelta(days=dt))
        plot_water_levels(stations, dates, levels, i)
        
if __name__ == "__main__":
    run()
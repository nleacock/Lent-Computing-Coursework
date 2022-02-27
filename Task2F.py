import datetime
from floodsystem.geo import build_station_list
from floodsystem.stationdata import update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.flood import stations_level_over_threshold
        
def run():
    stations = build_station_list()
    update_water_levels(stations)
    #obtain list of all stations in descending relative water level order
    desired_stations = stations_level_over_threshold(stations, 0)
    counter = 0
    for station in desired_stations:
        #get relevant data for water level history
        dates, levels = fetch_measure_levels(station[0].measure_id, dt=datetime.timedelta(days=2))
        #tests that there is no error where data has empty lists, and ignores these, coz there was an issue with one station already!
        if dates == [] or levels == []:
            pass
        else:
            counter += 1
            plot_water_level_with_fit(station, dates, levels, 4)
            #ensures only plots for the five most at risk stations
            if counter > 4:
                break

if __name__ == "__main__":
    run()
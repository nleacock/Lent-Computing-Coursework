import datetime
from floodsystem.geo import build_station_list
from floodsystem.stationdata import update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import polyfit
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.flood import stations_highest_rel_level

#                                    def run():
 #                                       stations = build_station_list()
  #                                      update_water_levels(stations)
   #                                     #obtain list of 5 stations for which the relative level is highest
    #                                    desired_stations = stations_highest_rel_level(stations, 5)
     #                                   #find dates and levels for every one of these stations and plot
      #                                  for station in desired_stations:
       #                                     dates, levels = fetch_measure_levels(station, 2)
        #                                    plot_water_level_with_fit(station, dates, levels, 4)
        
def run():
    stations = build_station_list()
    update_water_levels(stations)
    #obtain list of 5 stations for which the relative level is highest
    desired_stations = stations_highest_rel_level(stations, 5)
    for station in desired_stations:
        #attempt to find station measure id using the station name provided by desired stations
        name = station[0]
        for element in stations:
            if element.name == name:
                measure_id = element.measure_id
        dates, levels = fetch_measure_levels(measure_id, dt=datetime.timedelta(days=2))
        poly, d0 = polyfit(dates, levels, 4)
        print(poly)
        print(d0)
    







if __name__ == "__main__":
    run()
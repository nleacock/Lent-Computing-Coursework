import datetime
from floodsystem.geo import build_station_list
from floodsystem.stationdata import update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import polyfit
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.flood import stations_highest_rel_level, stations_level_over_threshold

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
            #poly, d0 = polyfit(dates, levels, 4)
            plot_water_level_with_fit(station, dates, levels, 4)
            #ensures only plots for the five most at risk stations
            if counter > 4:
                break


            #use station measure_id to find water level history and hence the polynomial information to plot
            #print(station[0].measure_id)
            #print(station[0].name)
            #print(dates, levels)
            #poly, d0 = polyfit(dates, levels, 4)
            #print(poly, d0)






if __name__ == "__main__":
    run()
import datetime
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import polyfit
from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels


def run():
    stations = build_station_list()
    update_water_levels(stations)
    #have 4 categories of flood risk, where the higher warnings are due to high derivatives and/or is well above the typical range
    
    #get latest water levels of stations and their typical ranges using the function made for task 2B, stations_level_over_threshold()
    #for loop which iterates an amount of times equal to the length of the list of the stations above the tolerance
    #get the polynomial for the station water levels using the function in 2F
    #find the derivative of this polynomial
    #if typical range > (some value, maybe 1.5?) and positive derivative, issue severe flood risk, add to severe flood risk list
    #elif typical range > (1?) and positive derivative, issue high flood risk, add to high flood risk list
    #elif typical range > (0.75?) and positive derivative, issue moderate flood risk, add to moderate flood risk list
    #elif derivative is very high issue severe, less high then high
    #else issue low risk, add to low risk list

    #iterate through the severe and high flood risk stations and add their TOWNS to a SET (set because we dont want duplicate towns)
    #print the contents of the set (towns that are most at risk of flooding)
    stationsover = stations_level_over_threshold(stations, 0.75)
    for station in stationsover:
        #using 2F's function (dates, stationsover[1], 3)
        #use some numerical differentiation at some x value, not sure which (i barely understand 2F T_T)
        dates, levels = fetch_measure_levels(station[0].measure_id, dt=datetime.timedelta(days=2))
        poly, d0 = polyfit(dates, levels, 3)
        if station[1] > 1.5 and """derivative greater than some value""":
            severe = set()
            for i in stations:
                if station[0] == i.name:
                    severe.add(i.town)
        elif station[1] > 1.0 and """derivative greater than some value""":
            high = set()
            for i in stations:
                if station[0] == i.name:
                    high.add(i.town)
        elif station[1] > 0.75 or """derivative is positive""":
            moderate = set()
            for i in stations:
                if station[0] == i.name:
                    moderate.add(i.town)
        else:
            low = set()
            for i in stations:
                if station[0] == i.name:
                    low.add(i.town)

    print("--TOWNS WITH SEVERE FLOOD RISK--")
    print(severe)
    print("--TOWNS WITH HIGH FLOOD RISK--")
    print(high)
if __name__ == "__main__":
    run()
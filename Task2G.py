import datetime
import numpy as np
import matplotlib as plt
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import polyfit
from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels


def run():
    stations = build_station_list()
    update_water_levels(stations)
    stationsover = stations_level_over_threshold(stations, 0.75)
    severe = set()
    high = set()
    moderate = set()
    low = set()
    for station in stationsover:
        dates, levels = fetch_measure_levels(station[0].measure_id, dt=datetime.timedelta(days=1))
        if dates == [] or levels == []:
            pass
        else:
            poly, d0 = polyfit(dates, levels, 4)
            derivative = np.polyder(poly, 4)
            value = derivative(plt.dates.date2num(dates[-1]) - d0)
            if station[1] > 1.5 and value > 0:
                for i in stations:
                    if station[0].name == i.name and i.town != None:
                            severe.add(i.town)
            elif station[1] > 1.0 and value > 0:
                for i in stations:
                    if station[0].name == i.name and i.town != None:
                            high.add(i.town)
            elif station[1] > 0.75 or value > 0:
                for i in stations:
                    if station[0].name == i.name and i.town != None:
                            moderate.add(i.town)
            else:
                for i in stations:
                    if station[0].name == i.name and i.town != None:
                            low.add(i.town)

    print("--TOWNS WITH SEVERE FLOOD RISK--")
    print(severe)
    print("--TOWNS WITH HIGH FLOOD RISK--")
    print(high)
if __name__ == "__main__":
    run()
from floodsystem.analysis import polyfit
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
import datetime
import numpy




def test_polyfit():
    stations = build_station_list()
    update_water_levels(stations)
    #find the polynomial and shift for the first few stations, and assert their types
    #for station in stations:
     #   dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=2))
        # try and remove empty list problem with Letcombe Bassett
        #if dates == [] or levels == []:
        #    pass
       # else:
          #  poly, d0 = polyfit(dates, levels, 4)
          #  assert isinstance(poly, numpy.poly1d)
          #  assert isinstance(d0, float)
          #  #check that d0 is bigger than 0 for all values
          #  assert d0 >= 0
          #pass
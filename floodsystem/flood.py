from floodsystem.station import MonitoringStation

def stations_level_over_threshold(stations, tol):
    list_of_tuples = []
    for station in stations:
        if station.relative_water_level() == None:
            pass
        elif station.relative_water_level() > tol:
            tuple = (station.name, station.relative_water_level())
            list_of_tuples.append(tuple)
    return list_of_tuples

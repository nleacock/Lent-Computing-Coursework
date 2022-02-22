

from floodsystem.utils import sorted_by_key

def stations_highest_rel_level(stations, N):
    """""""take the code from 2B and chop off the first N terms, i.e. generate a list of the N stations with the highest relative levels"""""""
    #create list of tuples of stations with their relative levels
    new_list = []
    for station in stations:
        new_list.append((station, station.relative_water_level))
    #sort list of tuples in decreasing relative water level order
    sorted_list = sorted_by_key(new_list, 1, reverse=True)
    #keep only the first N entries in the list
    for i in range(N, len(sorted_list)+1):
        sorted_list.pop(i)

    return sorted_list
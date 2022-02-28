import matplotlib.dates as plt
import numpy as np

def polyfit(dates, levels, p):
    """""""convert the history of water level into a polynomial and a shift of the time axis"""""""
    
    if dates == [] or levels == []:
        pass
    
    else:
        #convert the date values to time in days, x
        x = plt.date2num(dates)
        #subtract the first time from the rest of the list, then store this as the time shift, d0
        d0 = x[0]
        new_x = x - x[0]
        # Find coefficients of best-fit polynomial of degree p
        p_coeff = np.polyfit(new_x, levels, p)

        # Convert coefficient into a polynomial that can be evaluated
        poly = np.poly1d(p_coeff)
        
    return poly, d0
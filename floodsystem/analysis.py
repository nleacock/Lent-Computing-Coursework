import matplotlib as plt
import numpy as np

def polyfit(dates, levels, p):
    """""""convert the history of water level into a polynomial and a shift of the time axis"""""""
    #convert the date values to time in days, x
    x = plt.dates.date2num(dates)
    #subtract the first time from the rest of the list, then store this as the time shift, d0
    d0 = x[0]
    x = x - x[0]
    # Find coefficients of best-fit polynomial of degree p
    p_coeff = np.polyfit(x, levels, p)

    # Convert coefficient into a polynomial that can be evaluated
    poly = np.poly1d(p_coeff)

    return poly, d0



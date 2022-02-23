import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta
from floodsystem.analysis import polyfit
from floodsystem.datafetcher import fetch_measure_levels
def plot_water_levels(stations, dates, levels):
    plt.plot(dates, levels)
    plt.xlabel("time")
    plt.ylabel("relative water level (m)")
    plt.title("station: {}".format(stations[0].name))


def plot_water_level_with_fit(station, dates, levels, p):
    """""""plots water level data and best fit polynomial"""""""

    # Plot original data points
    plt.plot(dates, levels, '.')

    # Use polyfit to define the polynomial required and the shift
    poly, d0 = polyfit(dates, levels, p)

    #plot the polynomial for 30 points, calculating at the shifted values and then plotting at the actual values
    x = plt.dates.date2num(dates)
    x1 = np.linspace(x[0], x[-1], 30)
    plt.plot(x1, poly(x1 - d0))
    plt.title(station.name)

    # Display plot
    plt.show()
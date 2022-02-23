import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta
from floodsystem.analysis import polyfit
from floodsystem.datafetcher import fetch_measure_levels

def plot_water_levels(stations, dates, levels, i):
    plt.plot(dates, levels, label="Water level")
    plt.axhline(1.0, color="red", label="Typical high")
    plt.axhline(0.0, color="green", label="Typical low")
    plt.xlabel("Date")
    plt.ylabel("Relative water level (m)")
    plt.title("Station: {}".format(stations[i].name))
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.legend()

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

    # Display plot
    plt.show()
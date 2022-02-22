import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta
def plot_water_levels(stations, dates, levels):
    plt.plot(dates, levels)
    plt.xlabel("time")
    plt.ylabel("relative water level (m)")
    plt.title("station: {}".format(stations[0].name))
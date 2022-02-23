import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta
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
    plt.show()
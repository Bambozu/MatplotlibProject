import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from psutil import cpu_percent
import pandas as pd
import numpy as np

time.sleep(2)

def CPU_LOAD():
    """
    Door middel van de library van PSUTIL halen we de CPU Load in percentage.
    """
    cpu_load= psutil.cpu_percent(1)
    return cpu_load


def SYSTEM_LOAD():
"""
Het binnen halen van de average load of de OS
"""
    system_load= psutil.getloadavg(1)
    return system_load


#hier begint livedata
cpu_percent()

frame_len = 200
y = []
def animate(i):
    y.append(cpu_percent())

    if len(y) <= frame_len:
        plt.cla()
        plt.plot(y, 'r', label = 'Real-Time CPU usage')

    plt.tight_layout()

ani = FuncAnimation(plt.gcf(), animate, interval = 1000)

# hier begint de static plot

# importing data using pandas
data = pd.read_csv("systemUsage.csv")
a = np.array(list(data["ram"]))

# plotting data directly from dataframe
data.plot("timestamp","ram", color="red",figsize=(15,5) )

# use this for extracting range from data (not really necessary)
# a = np.array(list(data["ram"][0:60]))

b = np.array(range(len(a)))

# making plot wider horizontally
plt.figure(figsize=(15,5))

# plotting points
plt.plot(b,a)

# filling everything below curve (to make it an "area chart")
plt.fill_between(b,a,color="blue",alpha=0.1)

# dynamically setting the limit on the y axis so a curve can be observed (maybe change scalar for different data) again not really necessary
plt.ylim((np.min(a)-np.min(a)*0.001), (np.max(a)+np.max(a)*0.001))

plt.title("Monitoring")
plt.xlabel("time in seconds")
plt.ylabel("cpu usage")
plt.grid(True)
plt.show()
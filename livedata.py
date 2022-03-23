import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from psutil import cpu_percent

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
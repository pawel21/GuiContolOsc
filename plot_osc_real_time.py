import matplotlib
matplotlib.use('qt5Agg')
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import time
import threading
import random
import sys

import rigol_ds1104b

plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = 'Palatino'
plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.unicode'] = True
plt.rcParams.update({'font.size': 28})

osc = rigol_ds1104b.RigolDS1104B("/dev/usbtmc0")


def real_time_plot():
    fig = plt.figure()
    ax1 = fig.add_subplot(1, 1, 1)

    def animate(*args):
        try:
            x, y = osc.get_data()
            ax1.clear()
            ax1.plot(x, y, 'r-')
            ax1.set_xlabel("time [s]")
            ax1.set_ylabel("voltage [V]")
            ax1.set_xlabel("time [s]", color="red")
            ax1.set_ylabel("voltage [V]", color="red")
            ax1.set_axis_bgcolor('black')
            plt.grid(True, color="red")
        except Exception as err:
            print(err)

    ani = animation.FuncAnimation(fig, animate, interval=10)
    plt.show()
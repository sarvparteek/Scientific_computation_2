'''
module: _plot.py
author: Luis Paris
description:
- defines graph() method to plot y = f(x) functions on the XY plane
- implemented as a simple wrapper over the matplotlib.pyplot class
'''

import matplotlib.pyplot as plt
import numpy as np

def graph(f, xl=0.01, xu=10.0, xlabel='x axis', ylabel='y axis', title='title', fig='plot.png', show=True):
    xp = (xu - xl) / 1000.0
    xpts = np.arange(xl, xu, xp)
    ypts = []
    for x in xpts:
        y = f(x)
        ypts.append(y)
    plt.plot(xpts, ypts)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(True)
    plt.savefig(fig)
    if show: plt.show()

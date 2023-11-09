import numpy as np
from matplotlib import pyplot as plt


class Graph:
    def __init__(self, fig, title: str = 'f(x)'):
        self.fig = fig
        self.ax = self.fig.add_subplot()
        self.ax.set(title=title,
                    xlabel='x',
                    ylabel='y',
                    facecolor='ghostwhite')
        self.ax.grid()
        self.color_bar = None

    def contour(self, x: list, y: list, z: list[list], *args, **kwargs):
        X, Y = np.meshgrid(x, y)
        Z = np.array(z)

        plt.xticks(x)
        plt.yticks(y)
        C = self.ax.contourf(X, Y, Z, *args, **kwargs)
        self.color_bar = self.fig.colorbar(C)

    def clear(self):
        if self.color_bar:
            self.color_bar.remove()

        attrs = {
            'title': self.ax.get_title(),
            'xlabel': self.ax.get_xlabel(),
            'ylabel': self.ax.get_ylabel(),
            'facecolor': self.ax.get_facecolor()
        }
        self.ax.clear()
        self.ax.set(**attrs)

import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


class Graph:
    def __init__(self, fig, title: str = 'f(x)'):
        self.fig = fig
        self.ax3d: Axes3D = self.fig.add_subplot(122, projection='3d')
        self.ax3d.set(title=title,
                      xlabel='x',
                      ylabel='y',
                      zlabel='p',
                      facecolor='ghostwhite')

        self.ax = self.fig.add_subplot(121)
        self.ax.set(title=title,
                    xlabel='x',
                    ylabel='y',
                    facecolor='ghostwhite')
        self.ax.grid()
        self.color_bar = None

    def draw3d(self, x: list, y: list, z: list, **kwargs):
        x, y = np.meshgrid(x, y)
        z = np.array(z)
        self.ax3d.plot_surface(x, y, z, **kwargs)

    def contour(self, x: list, y: list, z: list[list], *args, **kwargs):
        X, Y = np.meshgrid(x, y)
        Z = np.array(z)

        plt.xticks(x)
        plt.yticks(y)
        C = self.ax.contour(X, Y, Z, *args, **kwargs)
        plt.clabel(C, fontsize=8)
        self.color_bar = self.fig.colorbar(C)

    def clear(self):
        attrs3d = {
            'title': self.ax3d.get_title(),
            'xlabel': self.ax3d.get_xlabel(),
            'ylabel': self.ax3d.get_ylabel(),
            'zlabel': self.ax3d.get_zlabel(),
            'facecolor': self.ax3d.get_facecolor()
        }
        self.ax3d.clear()
        self.ax3d.set(**attrs3d)
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

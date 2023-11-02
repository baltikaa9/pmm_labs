import numpy as np
from mpl_toolkits.mplot3d import Axes3D


class Graph:
    def __init__(self, fig, title: str = 'f(x)'):
        self.ax: Axes3D = fig.add_subplot(projection='3d')
        self.ax.set(title=title,
                    xlabel='x',
                    ylabel='t',
                    zlabel='T',
                    facecolor='ghostwhite')

    def draw(self, x: list, y: list, z: list, **kwargs):
        x, y = np.meshgrid(x, y)
        z = np.array(z)
        self.ax.plot_surface(x, y, z, **kwargs)

    def clear(self):
        attrs = {
            'title': self.ax.get_title(),
            'xlabel': self.ax.get_xlabel(),
            'ylabel': self.ax.get_ylabel(),
            'zlabel': self.ax.get_zlabel(),
            'facecolor': self.ax.get_facecolor()
        }
        self.ax.clear()
        self.ax.set(**attrs)

    def draw_scatter(self, x, y, z, **kwargs):
        self.ax.scatter(x, y, z, **kwargs)

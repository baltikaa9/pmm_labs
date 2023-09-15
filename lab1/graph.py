import numpy as np


class Graph:
    def __init__(self, fig, title: str = 'f(x)'):
        self.ax = fig.add_subplot(111, projection='3d')
        self.ax.set(title=title,
                    xlabel='x',
                    ylabel='t',
                    zlabel='T',
                    facecolor='ghostwhite')

    def draw(self, x: list, y: list, z: list, **kwargs):
        x, y = np.meshgrid(x, y)
        z = np.array(z)
        self.ax.plot_surface(x, y, z, **kwargs)

    def draw_scatter(self, x, y, z, **kwargs):
        self.ax.scatter(x, y, z, **kwargs)
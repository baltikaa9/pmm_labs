import numpy as np
from mpl_toolkits.mplot3d import Axes3D


class Graph:
    def __init__(self, fig, title: str = 'f(x)'):
        self.ax3d: Axes3D = fig.add_subplot(projection='3d')
        self.ax3d.set(title=title,
                      xlabel='x',
                      ylabel='t',
                      zlabel='u',
                      facecolor='ghostwhite')

        self.ax2d = fig.add_subplot()
        self.ax2d.set(title=title,
                      xlabel='x',
                      ylabel='u',
                      facecolor='ghostwhite')

    def draw3d(self, x: list, y: list, z: list, **kwargs):
        x, y = np.meshgrid(x, y)
        z = np.array(z)
        self.ax3d.plot_surface(x, y, z, **kwargs)

    def draw2d(self, x: list, y: list, **kwargs):
        self.ax2d.set_xlim(-0.1, 1.1)
        self.ax2d.set_ylim(-0.25, 0.4)
        line, = self.ax2d.plot(x, y, **kwargs)
        return line

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

        attrs2d = {
            'title': self.ax2d.get_title(),
            'xlabel': self.ax2d.get_xlabel(),
            'ylabel': self.ax2d.get_ylabel(),
            'facecolor': self.ax2d.get_facecolor()
        }
        self.ax2d.clear()
        self.ax2d.set(**attrs2d)

    def draw_scatter(self, x, y, z, **kwargs):
        self.ax3d.scatter(x, y, z, **kwargs)

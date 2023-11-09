import numpy as np


class Graph:
    def __init__(self, fig, title: str = 'f(x)'):
        self.fig = fig
        self.ax = self.fig.add_subplot()
        self.ax.set(title=title,
                    xlabel='x',
                    ylabel='y',
                    facecolor='ghostwhite')
        self.color_bar = None

    def draw(self, x: list, y: list, z: list, **kwargs):
        X, Y = np.meshgrid(x, y)
        Z = np.array(z)

        self.color_bar = self.fig.colorbar(self.ax.contourf(X, Y, Z, vmin=0, **kwargs))

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

    def draw_scatter(self, x, y, z, **kwargs):
        self.ax.scatter(x, y, z, **kwargs)

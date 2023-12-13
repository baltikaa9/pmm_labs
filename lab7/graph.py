class Graph:
    def __init__(self, fig, title: str = 'f(x)'):
        self.fig = fig
        self.ax = self.fig.add_subplot()
        self.ax.set(title=title,
                    xlabel='x',
                    ylabel='T',
                    facecolor='ghostwhite')
        self.color_bar = None

    def draw(self, x: list, y: list, **kwargs):
        # self.color_bar = self.fig.colorbar(self.ax.imshow(z[::-1], extent=(x[0], x[-1], y[0], y[-1]), aspect='auto', **kwargs))
        # self.ax.plot(x, z[0], label='t = 0')
        # self.ax.plot(x, z[len(z) // 4], label='t = t_max * 25%')
        # self.ax.plot(x, z[len(z) // 4 * 3], label='t = t_max * 75%')
        # self.ax.plot(x, z[-1], label='t = t_max')
        # print(z)
        # self.ax.legend()
        # self.ax2d.set_xlim(-0.1, 1.1)
        # self.ax2d.set_ylim(-0.25, 0.4)
        # self.ax2d.set_ylim(-1, 1)
        line, = self.ax.plot(x, y, **kwargs)
        return line

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

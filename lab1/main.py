from dataclasses import dataclass

import numpy as np
from matplotlib import pyplot as plt

from lab1.plot import Graph

"""
0 ≤ x ≤ 1 , h ≤ 0.02 , t ≤ 4 
"""

Coords = Temperature = list[float]


@dataclass
class Parameters:
    a: int
    b: int
    h: float
    t_max: float
    T_a: float
    T_b: float

    def __post_init__(self):
        self.N = int((self.b - self.a) / self.h)
        self.x = [0.0 for _ in range(self.N + 2)]
        for i in range(self.N + 2):
            self.x[i] = round(self.a + (i - 0.5) * self.h, 2)
        self.T0 = [round(1 - x, 2) for x in self.x]
        # self.T0 = [0.0 for x in self.x]
        self.T0[0] = self.T_a
        self.T0[-1] = self.T_b
        self.tau = self.h * self.h / (2 * self.D(-1))

    def D(self, i: int) -> int:
        return 1 if self.x[i] < 0.5 else 2
        # return 1


def thermal_conductivity(params: Parameters):
    T = [params.T0]
    t = 0
    T0 = params.T0
    T1 = [0.0 for _ in range(params.N + 2)]
    while round(t, 4) < params.t_max:
        for i in range(1, params.N + 1):
            k = (params.tau * params.D(i)) / (params.h * params.h)
            T1[i] = k * T0[i + 1] + (1 - 2 * k) * T0[i] + k * T0[i - 1]

        T1[0] = params.T_a
        T1[params.N + 1] = params.T_b
        print(t // params.tau + 1, T1[1:-1])
        T.append(T1.copy())
        T0 = T1.copy()
        t += params.tau
    return T


if __name__ == '__main__':
    params = Parameters(a=0, b=1, h=0.02, t_max=0.3, T_a=0, T_b=0)
    # params = Parameters(a=0, b=1, h=0.02, t_max=0.3, T_a=-2, T_b=1)

    fig = plt.figure(facecolor='gainsboro')

    graph = Graph(fig, title='Явная схема')
    T = thermal_conductivity(params)
    graph.draw(params.x, list(np.arange(0, params.t_max + params.tau, params.tau)), T, color='#b7ddfe')
    plt.show()

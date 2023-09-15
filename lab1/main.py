import numpy as np
from matplotlib import pyplot as plt

from lab1.parameters import Parameters
from lab1.graph import Graph

"""
0 ≤ x ≤ 1 , h ≤ 0.02 , t ≤ 4 
"""


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
    params = Parameters(a=0, b=1, h=0.02, t_max=0.3, T0_expr='1-x', T_a=0, T_b=0)
    # params = Parameters(a=0, b=1, h=0.02, t_max=0.3, T_a=-2, T_b=1)

    fig = plt.figure(facecolor='gainsboro')

    graph = Graph(fig, title='Явная схема')
    T = thermal_conductivity(params)
    graph.draw(params.x, list(np.arange(0, params.t_max + params.tau, params.tau)), T, color='#b7ddfe')
    plt.show()

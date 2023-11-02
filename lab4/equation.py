"""
0 ≤ x ≤ 1 , h ≤ 0.02 , t ≤ 4
"""
from math import exp

from matplotlib import pyplot as plt

from graph import Graph
from parameters import Parameters


def impurities_transfer(params: Parameters) -> list[list[float]]:
    p = params.p
    p1 = p.copy()
    t = 0
    while t <= params.t_max:
        for i in range(1, len(params.x) - 1):
            for j in range(1, len(params.y) - 1):
                p1[i][j] = p[i][j] - (1 / (params.dx * params.dy)) * \
                   (params.dM1(p, i, j) - params.dM2(p, i, j) + params.dM3(p, i, j) - params.dM4(p, i, j)) + \
                   (params.dt / (params.dx * params.dx)) * (params.D * params.C * ((p[i + 1][j] - p[i][j]) - (p[i][j] - p[i - 1][j]))) + \
                   (params.dt / (params.dy * params.dy)) * (params.D * params.C * ((p[i][j + 1] - p[i][j]) - (p[i][j] - p[i][j - 1]))) + \
                   params.dt * params.Q(i, j)

        for i in range(len(params.x)):
            for j in range(len(params.y)):
                if i == 0 or j == 0 or i == len(params.x) - 1 or j == len(params.y) - 1:
                    p1[i][j] = 0

        p = p1.copy()
        t += params.dt
    return p


if __name__ == '__main__':
    # print(Parameters().x)
    # print(Parameters().p)
    params = Parameters()
    p = impurities_transfer(params)
    # for r in p:
    #     print(r)



    fig = plt.figure(facecolor='ghostwhite')
    graph = Graph(fig, title='')
    graph.contour(params.x, params.y, p)
    plt.show()

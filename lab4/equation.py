"""
0 ≤ x ≤ 1 , h ≤ 0.02 , t ≤ 4
"""
from math import exp
from pprint import pprint

from parameters import Parameters


def impurities_transfer(params: Parameters):
    p = params.p
    p1 = p.copy()
    t = 0
    Q = 1
    while t <= params.t_max:
        for i in range(1, params.N + 1, params.dx):
            for j in range(1, params.M + 1, params.dy):
                p1[i][j] = p[i][j] - (1 / (params.dx * params.dy)) * \
                   (params.dM1(p, i, j) - params.dM2(p, i, j) + params.dM3(p, i, j) - params.dM4(p, i, j)) + \
                   (params.dt / (params.dx * params.dx)) * (params.D * params.C * ((p[i + 1][j] - p[i][j]) - (p[i][j] - p[i - 1][j]))) + \
                   (params.dt / (params.dy * params.dy)) * (params.D * params.C * ((p[i][j + 1] - p[i][j]) - (p[i][j] - p[i][j - 1]))) + \
                   params.dt * Q

        for i in range(params.N + 2):
            for j in range(params.M + 2):
                if i == 0 or j == 0 or i == params.N + 1 or j == params.M + 1:
                    p1[i][j] = 0.0
        p = p1.copy()
        # print(p)
        t += params.dt
    return p


if __name__ == '__main__':
    pprint(impurities_transfer(Parameters())[400])

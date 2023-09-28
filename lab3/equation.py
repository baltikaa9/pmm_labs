"""
0 ≤ x ≤ 1 , h ≤ 0.02 , t ≤ 4
"""
from math import exp

from parameters import Parameters


def wave_equation(params: Parameters):
    u = [params.u0, params.u1]
    t = 2 * params.tau
    u0 = params.u0
    u1 = params.u1
    u2 = [0.0 for _ in range(params.N + 2)]
    while round(t, 4) <= params.t_max:
        for i in range(1, params.N + 1):
            k = (params.tau * params.tau * params.c(i) * params.c(i)) / (params.h * params.h)
            u2[i] = k * u1[i+1] + (1 - k) * 2 * u1[i] + k * u1[i-1] - u0[i]

        u2[0] = 0
        u2[params.N + 1] = t * exp(-t)
        # print(t // params.tau + 1, T1[1:-1])
        u.append(u2.copy())
        u0 = u1.copy()
        u1 = u2.copy()
        t += params.tau
    return u

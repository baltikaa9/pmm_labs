"""
0 ≤ x ≤ 1 , h ≤ 0.02 , t ≤ 4
"""
from parameters import Parameters


def thermal_conductivity_explicit_non_linear(params: Parameters):
    T = [params.T0]
    t = params.tau
    T0 = params.T0
    T1 = [0.0 for _ in range(params.N + 2)]
    while round(t, 4) <= params.t_max:
        for i in range(1, params.N + 1):
            DR = (params.D(i, T0[i+1]) + params.D(i, T0[i])) / 2
            DL = (params.D(i, T0[i-1]) + params.D(i, T0[i])) / 2
            k = params.tau / (params.h * params.h)
            T1[i] = k * DR * T0[i + 1] + (1 - k * (DR + DL)) * T0[i] + k * DL * T0[i - 1]

        T1[0] = T1[1] - params.h * params.left_bound
        T1[params.N + 1] = T1[params.N] + params.h * params.right_bound
        # print(t // params.tau + 1, T1[1:-1])
        T.append(T1.copy())
        T0 = T1.copy()
        t += params.tau
    return T

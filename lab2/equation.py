"""
0 ≤ x ≤ 1 , h ≤ 0.02 , t ≤ 4
"""
from parameters import Parameters


def thermal_conductivity_implicit(params: Parameters):
    T = [params.T0]
    t = params.tau
    T0 = params.T0
    N = params.N
    T1 = [0.0 for _ in range(N + 2)]

    while round(t, 4) <= params.t_max:
        # прогоночные коэф-ты
        A = [0.0 for _ in range(N + 2)]
        B = [0.0 for _ in range(N + 2)]

        A[0] = 1
        B[0] = -params.h * params.left_bound
        for i in range(1, N + 2):
            k = params.tau * params.D(i)
            A[i] = k / (params.h * params.h + k * (2 - A[i-1]))
            B[i] = (params.h * params.h * T0[i-1] + k * B[i-1]) / (params.h * params.h + k * (2 - A[i-1]))

        T1[N+1] = (params.h * params.right_bound + B[N+1]) / (1 - A[N+1])
        for i in range(N, -1, -1):
            T1[i] = A[i+1] * T1[i+1] + B[i+1]

        # T1[0] = T1[1] - params.h * params.left_bound
        # T1[params.N + 1] = T1[params.N] + params.h * params.right_bound
        T.append(T1.copy())
        T0 = T1.copy()
        t += params.tau
    return T

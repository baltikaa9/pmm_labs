from parameters import Parameters


def poisson_equation(params: Parameters):
    U0 = params.U
    U1 = U0.copy()
    tau = params.tau
    h = params.h

    for _ in range(params.n_iter):
        for m in range(1, params.ny + 1):
            for n in range(1, params.nx + 1):
                U1[m][n] = U0[m][n] + (tau / h ** 2) * (U0[m + 1][n] - 2 * U0[m][n] + U0[m - 1][n]) + \
                    (tau / h ** 2) * (U0[m][n + 1] - 2 * U0[m][n] + U0[m][n - 1]) - \
                    tau * ((m * h) ** 2 - (n * h) ** 2 - m * h + n * h)     # tau * rho

        U0 = U1.copy()
    return U0

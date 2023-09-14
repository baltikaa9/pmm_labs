from typing import Callable

"""
0 ≤ x ≤ 1 , h ≤ 0.02 , t ≤ 4 
"""

Coords = Temperature = list[float]


class Parameters:
    def __init__(self, a: int, b: int, h: float, t_max: float, t_a: float, t_b: float):
        self.a = a
        self.b = b
        self.h = h
        self.t_max = t_max
        self.T_a = t_a
        self.T_b = t_b

        self.N = int((self.b - self.a) / self.h)
        self.x = [0.0 for _ in range(self.N + 2)]
        for i in range(self.N + 2):
            self.x[i] = round(self.a + (i - 0.5) * self.h, 2)
        self.T0 = [round(1 - x, 2) for x in self.x]
        self.tau = self.h * self.h / (2 * self.D(-1))

    def D(self, i: int) -> int:
        return 1 if self.x[i] < 0.5 else 2


def thermal_conductivity(params: Parameters):
    t = 0
    T1 = [0.0 for _ in range(params.N + 2)]
    while t < params.t_max:
        for i in range(1, params.N + 1):
            k = (params.tau * params.D(i)) / (params.h * params.h)
            T1[i] = k * params.T0[i + 1] + (1 - 2 * k) * params.T0[i] + k * params.T0[i - 1]

        T1[0] = params.T_a - T1[1]
        T1[params.N + 1] = params.T_b - T1[params.N]
        print(T1[1:-1])
        params.T0 = T1.copy()
        t += params.tau


if __name__ == '__main__':
    params = Parameters(0, 1, 0.02, 4, 0, 0)
    thermal_conductivity(params)
    ...

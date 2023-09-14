from typing import Callable

"""
0 ≤ x ≤ 1 , h ≤ 0.02 , t ≤ 4 
"""

Coords = Temperature = list[float]

a = 0
b = 1
h = 0.02
N = int((b - a) / h)
gu_a = 0
gu_b = 0

x = [0.0 for _ in range(N + 2)]
for i in range(N + 2):
    x[i] = round(a + (i - 0.5) * h, 2)

T0 = [round(1 - _x, 2) for _x in x]


def D(x: float) -> int:
    return 1 if x < 0.5 else 2


t = 0
tau = h * h / (2 * D(x[-1]))
t_max = 4


def thermal_conductivity(x: Coords, T0: Temperature, d: Callable[[float], int] = (lambda _: 1)):
    t = 0
    T1 = [0.0 for _ in range(N + 2)]
    while t < t_max:
        for i in range(1, N + 1):
            k = (tau * d(x[i])) / (h * h)
            T1[i] = k * T0[i + 1] + (1 - 2 * k) * T0[i] + k * T0[i - 1]

        T1[0] = gu_a - T1[1]
        T1[N + 1] = gu_b - T1[N]
        print(T1[1:-1])
        T0 = T1.copy()
        t += tau


if __name__ == '__main__':
    thermal_conductivity(x, T0, D)
    ...

from dataclasses import dataclass
from math import exp, sin, cos, pi

import numpy as np

Coords = Wave = list[float]


@dataclass
class Parameters:
    # размерность сетки
    N: int = 100
    M: int = 100
    t_max: int = 10
    # шаги
    dx: int = 1
    dy: int = 1
    dt: float = 0.01
    C: float = 3    # скорость ветра
    D: float = 10   # коэфф-т диффузии
    # скорости ветра по x, y
    u = C * cos(pi / 4)
    v = C * sin(pi / 4)

    def __post_init__(self):
        self.x: Coords = [0.0 for _ in range(0, self.N + 2)]
        self.y: Coords = [0.0 for _ in range(0, self.M + 2)]
        for i in range(self.N + 2):
            self.x[i] = i * self.dx

        for i in range(self.N + 2):
            self.y[i] = i * self.dy

        # НУ
        self.p = [[0 for _ in self.y] for _ in self.x]

        # ГУ
        for i in range(self.N + 2):
            for j in range(self.M + 2):
                if i == 0 or j == 0 or i == self.N + 1 or j == self.M + 1:
                    self.p[i][j] = 0

    def dM1(self, p: list[list[float]], i: int, j: int) -> float:
        res = self.dy * self.dt
        if self.u > 0:
            return res * p[i][j] * self.u
        else:
            return res * p[i+1][j] * self.u

    def dM2(self, p: list[list[float]], i: int, j: int) -> float:
        res = self.dy * self.dt
        if self.u < 0:
            return res * p[i][j] * self.u
        else:
            return res * p[i-1][j] * self.u

    def dM3(self, p: list[list[float]], i: int, j: int) -> float:
        res = self.dx * self.dt
        if self.v > 0:
            return res * p[i][j] * self.v
        else:
            return res * p[i][j + 1] * self.v

    def dM4(self, p: list[list[float]], i: int, j: int) -> float:
        res = self.dx * self.dt
        if self.v < 0:
            return res * p[i][j] * self.v
        else:
            return res * p[i][j - 1] * self.v

    def Q(self, i: int, j: int):
        if i == self.N // 2 and j == self.M // 2:
            return 100
        return 0

    # def D1(self, i: int, j: int) -> float:
    #     return self.D *

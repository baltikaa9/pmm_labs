from dataclasses import dataclass
from math import exp, sin, cos, pi

import numpy as np

Coords = Wave = list[float]


@dataclass
class Parameters:
    # размерность сетки
    N: int = 840
    M: int = 840
    t_max: float = 10
    # шаги
    dx: int = 120 // 2
    dy: int = 120 // 2
    dt: float = 0.01
    C: float = 10    # скорость ветра
    D: float = 10   # коэфф-т диффузии
    # скорости ветра по x, y
    C_angle: str = 'pi/4'
    # источник в центре
    q: float = 1

    def __post_init__(self):
        self.x: Coords = [0.0 for _ in range(self.N // self.dx + 2)]
        self.y: Coords = [0.0 for _ in range(self.M // self.dy + 2)]

        for i in range(self.N // self.dx + 2):
            self.x[i] = i * self.dx

        for i in range(self.M // self.dy + 2):
            self.y[i] = i * self.dy

        # НУ
        self.p = [[0 for _ in self.y] for _ in self.x]

        # ГУ
        for i in range(len(self.x)):
            for j in range(len(self.y)):
                if i == 0 or j == 0 or i == len(self.x) - 1 or j == len(self.y) - 1:
                    self.p[i][j] = 0

        self.u = self.C * cos(eval(self.C_angle))
        self.v = self.C * sin(eval(self.C_angle))

        print(f'{self.C_angle}, {self.u=}, {self.v=}')

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
        if i == len(self.x) // 2 and j == len(self.y) // 2:
            return self.q
        return 0

    # def D1(self, i: int, j: int) -> float:
    #     return self.D *

from dataclasses import dataclass
from math import pi, log

import numpy as np

Coords = Temperature = list[float]


@dataclass
class Parameters:
    a_x: int = 0
    b_x: int = 1
    a_y: int = 0
    b_y: int = 1
    h: float = 0.05
    e: float = 0.001

    def __post_init__(self):
        self.x = np.arange(self.a_x - self.h, self.b_x + 2 * self.h, self.h).round(3)
        self.y = np.arange(self.a_y - self.h, self.b_y + 2 * self.h, self.h).round(3)
        self.nx = len(self.x) - 2  # -2 фиктивные ячейки
        self.ny = len(self.y) - 2

        self.tau = self.h * self.h / (4 * pi)
        self.n_iter = int((2 * log(1 / self.e)) / (pi * pi * self.h * self.h))

        # НУ
        self.U = np.zeros((len(self.y), len(self.x)))

        # ГУ
        for i in range(1, self.nx + 1):
            self.U[0][i] = i * self.h - (i * self.h) ** 2  # Снизу
            self.U[self.ny + 1][i] = i * self.h - (i * self.h) ** 2  # Сверху

        for i in range(1, self.ny + 1):
            self.U[i][0] = i * self.h - (i * self.h) ** 2  # Слева
            self.U[i][self.nx + 1] = (i * self.h - (i * self.h) ** 2) * np.exp(i * self.h)  # Справа


if __name__ == '__main__':
    p = Parameters()

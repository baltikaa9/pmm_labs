from dataclasses import dataclass
from math import exp, sin

import numpy as np

Coords = Wave = list[float]


@dataclass
class Parameters:
    a: int = 0
    b: int = 1
    h: float = 0.02
    t_max: float = 30
    init_cond_1: int = 0
    init_cond_2: int = 0
    left_bound: float = 0
    right_bound: float = 0

    def __post_init__(self):
        self.N: int = int((self.b - self.a) / self.h)
        self.x: Coords = [0.0 for _ in range(self.N + 2)]
        for i in range(self.N + 2):
            self.x[i] = round(self.a + (i - 0.5) * self.h, 2)

        self.tau: float = self.h / 3
        # self.tau: float = 0.001

        # НУ
        self.u0: Wave = [self.init_cond_1 for _ in self.x]
        self.u1: Wave = [self.init_cond_1 + self.tau * 0 for x in self.x]

        # ГУ
        self.u0[0] = self.left_bound
        self.u0[-1] = self.right_bound
        self.u1[0] = self.left_bound
        self.u1[-1] = self.tau * exp(-self.tau)
        # self.u1[-1] = 0

    def c(self, i: int) -> int:
        return 1

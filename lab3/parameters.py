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
    init_cond_1: str = '0'
    init_cond_2: str = '0'
    left_bound: str = '0'
    right_bound: str = 't * exp(-t)'

    def __post_init__(self):
        self.N: int = int((self.b - self.a) / self.h)
        self.x: Coords = [0.0 for _ in range(self.N + 2)]
        for i in range(self.N + 2):
            self.x[i] = round(self.a + (i - 0.5) * self.h, 2)

        self.tau: float = self.h / 1.5
        # self.tau: float = 0.001

        # НУ
        self.u0: Wave = [eval(self.init_cond_1) for x in self.x]
        self.u1: Wave = [eval(self.init_cond_1) + self.tau * eval(self.init_cond_2) for x in self.x]

        # ГУ
        t = 0
        self.u0[0] = eval(self.left_bound)
        self.u0[-1] = eval(self.right_bound)
        t += self.tau
        self.u1[0] = eval(self.left_bound)
        self.u1[-1] = eval(self.right_bound)
        # self.u1[-1] = 0

    def c(self, i: int) -> int:
        return 1

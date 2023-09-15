from dataclasses import dataclass

Coords = Temperature = list[float]


@dataclass
class Parameters:
    a: int = 0
    b: int = 1
    h: float = 0.02
    t_max: float = 0.3
    T0_expr: str = '1-x'
    T_a: float = 0
    T_b: float = 0

    def __post_init__(self):
        self.N: int = int((self.b - self.a) / self.h)
        self.x: Coords = [0.0 for _ in range(self.N + 2)]
        for i in range(self.N + 2):
            self.x[i] = round(self.a + (i - 0.5) * self.h, 2)
        # НУ
        self.T0: Temperature = [round(eval(self.T0_expr), 2) for x in self.x]
        # self.T0 = [0.0 for x in self.x]

        # ГУ
        self.T0[0] = self.T_a
        self.T0[-1] = self.T_b

        self.tau: float = self.h * self.h / (2 * self.D(-1))

    def D(self, i: int) -> int:
        return 1 if self.x[i] < 0.5 else 2
        # return 1

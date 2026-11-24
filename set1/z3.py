import numpy as np


def my_nsolve(f, c, n: int, s):
    a = [s * i for i in range(n) if abs(f(s * i) - c) < 10e-6 and s * i > 1e-3]
    return min(a)


def compound_interest(t, y, n):
    return (1 + t * y / n) ** (n * t)


y = 0.05
i = 0.1
b = [1, 2, 4, 12]
inflation = compound_interest(1, i, 1)

for n in b:
    com = lambda y: compound_interest(1, y, n)
    print(
        f"Frequency: {n:<2} Interest needed: {my_nsolve(com, inflation, int(1e5), 1e-5):.4f}"
    )

print(f"{my_nsolve(lambda y: np.exp(y),inflation,int(1e5),1e-5):.4f}")

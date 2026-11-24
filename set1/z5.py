import numpy as np

s = 10000
y = 0.05
n = 4
t = 2


def my_nsolve(f, c, n=int(1e5), a=30, b=10e-5):
    x = 0
    for i in range(n):
        x += a / n
        if abs(f(x) - c) < b:
            return x


def const_deposit_simple(x, y, t, n):
    total_depo = 0
    interest_acc = 0
    for i in range(n * t):
        total_depo += x
        interest_acc += y / n * total_depo
    return total_depo + interest_acc


def const_deposit_compound(x, y, t, n):
    total = 0
    for i in range(n * t):
        total += x
        # interest_acc += y / n * total_depo
        total += y / n * total
    return total


cds = lambda x: const_deposit_simple(x, y, t, n)
print(f"Simple interest: {my_nsolve(cds, s, n=int(10e8), a=10e6, b=1e-1):.2f}")

cdc = lambda x: const_deposit_compound(x, y, t, n)
print(
    f"Compound interest (quaterly): {my_nsolve(cdc, s, n=int(10e8), a=10e6, b=1e-1):.2f}"
)

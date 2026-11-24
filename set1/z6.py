from methods import *
import numpy as np


def my_comopund_varying(l: list):
    total = 100
    for i in l:
        total *= 1 + i / (12 * 100)
    return total - 100


def my_simple_varying(l: list, d: list):
    init = 100
    interest = 0
    for i, j in zip(l, d):
        interest += i / (12 * 100) / (1 + j / (100 * 12)) * init
    return interest


l = ["A", "B", "C"]
a = [i for i in range(1, 13)]
c = [i for i in range(12, 0, -1)]
b = [6.5 for i in range(12)]
print(
    f"For bank A, calculated effective interest rate is: {my_comopund_varying(a):.4f} %\n"
)
print(
    f"For bank B, calculated effective interest rate is: {my_comopund_varying(b):.4f} %\n"
)
print(
    f"For bank C, calculated effective interest rate is: {my_comopund_varying(c):.4f} %\n"
)
print(
    "For the second problem, we need to consider each bank weighted by discount factor for all three separately,\n"
    "since we could put our money got from bank on any other's account. "
    "so we will be encountering 3x3 matrix."
)

results = [(my_simple_varying(i, j)) for j in [a, b, c] for i in [a, b, c]]
# print(matrix)
# for i in matrix:
#     print(f"{matrix[i]} {i:.4f}")


print(f"{my_simple_varying(a, a):.3f}")
print(f"{my_simple_varying(a, b):.3f}")
print(f"{my_simple_varying(a, c):.3f}")
print(f"{my_simple_varying(b, a):.3f}")
print(f"{my_simple_varying(b, b):.3f}")
print(f"{my_simple_varying(b, c):.3f}")
print(f"{my_simple_varying(c, a):.3f}")
print(f"{my_simple_varying(c, b):.3f}")
print(f"{my_simple_varying(c, c):.3f}")
print(results.index(max(results)))

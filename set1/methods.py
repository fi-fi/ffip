from sympy import exp


def simple_interest(y, t):
    return 1 + t * y


def compound_interest(y, t, n):
    return (1 + y / n) ** (n * t)


def cont_interest(y, t):
    return exp(y * t)

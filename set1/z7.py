import numpy as np

x = 10000
y = 0.1
n = 4
r = y / n


def my_nsolve(f, c, n=int(1e5), a=30, b=10e-5):
    x = 0
    for i in range(n):
        x += a / n
        if abs(f(x) - c) < b:
            return x


def payments_principal(
    n,
    r,
    x,
):

    payments = [0]
    left = x
    for i in range(n):
        payments.append(x / n + left * r)
        left -= x / 4
    return payments


def annuity_payments(initial, n, y1):
    return initial * ((1 - (1 + y1 / n) ** (-n)) / (y1 / n)) ** (-1)


def interest(x, y, n):
    return x * y


def annuity_pv_payments(x, n, y1):
    return annuity_payments(x, n, y1) - interest(x, y1 / n, n)


def pv(CF, n, T, r):
    list1 = [i / (1 + r / n) ** (T / r) for i in CF]
    return sum(list1)


print("Annuity Payments:")
print([a := annuity_payments(x, n, y) for i in range(4)])
print("Principal equal Payments:")
p = payments_principal(n, y / n, x)
print(p[1:])


# print(annuity_pv_payments(x, n, r))
currentpv = [x]
interestlist = []
for i in range(1, 5):
    interestlist.append(interest(currentpv[i - 1], y / n, n))
    currentpv.append(
        currentpv[i - 1]
        - annuity_payments(x, n, y)
        + interest(currentpv[i - 1], y / n, n)
    )
# print(currentpv)

# print(interestlist)

print("PRINCIPAL EQUAL PAYMENTS")
print("-" * 70)
for i in range(1, 5):
    print(
        f"| PV: {[x*(1-j/n) for j in range(1,5)][i-1]} | Payment: {p[i]:^08.3f} | Interest: {p[i]-x/n:^08.3f} | PV payment: {x/n:^08.3f} |"
    )
    print("-" * 70)

print("ANNUAL PAYMENTS")
print("-" * 70)
for i in range(1, 5):
    print(
        f"| PV: {currentpv[i]:^08.3f} | Payment: {a:^08.3f} | Interest: {interestlist[i-1]:^08.3f} | PV payment: {currentpv[i-1]-currentpv[i]:^08.3f} |"
    )
    print("-" * 70)


print(f"TOTAL - EQUAL PRINCIPAL: {sum([p[i]-x/n for i in range(1,5)]):.3f}")
print(f"TOTAL - ANNUITY: {sum(interestlist):.3f}")


def effective_ir(CF, y):
    DCF = []
    for i in range(4):
        DCF.append(CF[i] / ((1 + y) ** ((i + 1) / n)))
    return sum(DCF)


# Principal

print(f" Effective interest rate (Equal PV Payments):{
    my_nsolve(
        lambda y: effective_ir([p[i + 1] for i in range(4)], y),
        10000,
        n=1000000,
        a=1,
        b=0.001,
    ):.4f}")


# Annuity

CF = [a for i in range(4)]

print(f" Effective interest rate (Annuity):{
    my_nsolve(
        lambda y: effective_ir([a for i in range(4)], y),
        10000,
        n=1000000,
        a=1,
        b=0.001,
    ):.4f}")

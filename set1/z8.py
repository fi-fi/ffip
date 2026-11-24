from methods import *

x = 500000
n = 12
y1 = 0.05
T1 = 30


def annuity_payments(initial, n, y1, T):
    return initial * ((1 - (1 + y1 / n) ** (-n * T)) / (y1 / n)) ** (-1)


def interest(x, y, n=12):
    return x * y


currentpv = [x]
# print(x, n, y1, T1)
print(annuity_payments(x, n, y1, T1))
for i in range(1, 4):
    currentpv.append(
        currentpv[i - 1]
        - annuity_payments(x, n, y1, T1)
        + interest(currentpv[i - 1], y1 / n)
    )

# print("ANNUITY")
# for i in range(1, len(currentpv)):
#     print(f"{"-"* 100}")
#     print(
#         f"|Principal value: {currentpv[i]:.3f} |"
#         f"Interest: {interest(currentpv[i-1],r):.3f} |"
#         f"Principal payment: {annuity_payments(x, n, y1, T1) - interest(currentpv[i-1],r):.3f} |"
#     )
# print(f"{"-"* 100}")

x = currentpv[-1]
print(x)
T1 -= 1 / 4
y1 = 0.055

print(annuity_payments(x, n, y1, T1))

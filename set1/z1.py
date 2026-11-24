#  Set 1, Problem 1
#  16.10.26


def compute_interest(month, b, y: float, d):
    if d == None:
        return b * (1 + days * y / 365)
    balance = b
    partial = 0
    counter1 = 0
    counter2 = 0
    if month == "October":
        days = 31
    if month == "November":
        days = 30
    d[days] = 0
    for k, v in d.items():
        counter2 = k
        partial += b * (1 + (counter2 - counter1) / 365 * y) - b
        b += v
        counter1 = k
    return partial, b


oct = {5: 17, 12: 35, 21: -55}
nov = {9: -25, 30: 100}
balance = 100
y = 0.05
newbalance = (
    compute_interest("October", balance, y, oct)[0]
    + compute_interest("October", balance, y, oct)[1]
)
print(compute_interest("October", balance, y, oct)[0] * 1e3)
newbalance2 = compute_interest("November", newbalance, y, nov)
print(compute_interest("November", newbalance, y, nov)[0] * 1e3)

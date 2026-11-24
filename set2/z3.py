def duration(pv, cflist, y):
    # cf = [*cflist.keys()]
    # cftime = [*cflist.values()]
    dcf = 0
    for item in cflist:
        dcf += item[1] * item[0] / (1 + y) ** item[1]
    return dcf / pv


def modified_duration(pv, cflist, y):
    return duration(pv, cflist, y) / (1 + y)


import QuantLib as ql


def my_nsolve(f, c, n=int(1e5), a=30, b=10e-5):
    x = 0
    for i in range(n):
        x += a / n
        if abs(f(x) - c) < b:
            return x


x = 1000
dictionary = {
    "DS0727": (0.025, 99.2, [25, 7, 2027]),
    "OK0128": (0, 94.95, [25, 1, 2028]),
    "PS0728": (0.075, 104.55, [25, 7, 2028]),
    "PS0729": (0.0475, 98.79, [25, 7, 2029]),
    "PS0730": (0.045, 96.47, [25, 7, 2030]),
}

spotdate = [2, 11, 2026]
spotdateql = ql.Date(*spotdate)
actact = ql.ActualActual(ql.ActualActual.ISMA)
# actactdc = ql.DayCounter(actact)
cashflow = []
time = []
for i in dictionary.values():
    a = i[2][2] - 2026
    l = []
    t = []
    l.append(i[0] * x)
    t0 = actact.yearFraction(
        spotdateql,
        ql.Date(i[2][0], i[2][1], 2027),
        ql.Date(i[2][0], i[2][1], 2026),
        ql.Date(i[2][0], i[2][1], 2027),
    )
    t.append(t0)
    for j in range(a - 1):
        l.append(i[0] * x)
        t.append(t0 + 1 + j)
    l.append(x)
    t.append(t0 + a - 1)
    cashflow.append(l)
    time.append(t)

print(cashflow)
# print(time)

lista = [[0 for i in range(len(cashflow[j]))] for j in range(len(cashflow))]
# print(lista)
for i in range(len(cashflow)):
    for j in range(len(cashflow[i])):
        lista[i][j] = (cashflow[i][j], time[i][j])
# print(lista)


def make_pairs(cfdict):
    cf = []
    for k, v in cfdict.items():
        for i in v:
            cf.append([k, i])
    return cf


def acc_interest(r, fv, spot, tm):
    dcf = actact.yearFraction(ql.Date(tm[0] + 1, tm[1], 2025), ql.Date(*spot))
    return fv * r * dcf


def pv(cflist, y):
    dcf = 0
    for item in cflist:
        # print(item[0] / (1 + y) ** item[1])
        dcf += item[0] / (1 + y) ** item[1]
        # print(item[0], item[1])
    return dcf


ytm = [0.036236, 0.043024, 0.046740, 0.052281, 0.055677]
i = 0
for k, v in dictionary.items():

    print(k)
    print("Duration: {:.3f}".format(duration(pv(lista[i], ytm[i]), lista[i], ytm[i])))
    print(
        "Modified duration: {:.3f}".format(
            modified_duration(pv(lista[i], ytm[i]), lista[i], ytm[i])
        )
    )
    i += 1

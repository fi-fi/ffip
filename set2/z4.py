def my_nsolve(f, c, n=int(1e5), a=30, b=10e-5):
    x = 0
    for i in range(n):
        x += a / n
        if abs(f(x) - c) < b:
            return x


def make_pairs(cfdict):
    cf = []
    for k, v in cfdict.items():
        for i in v:
            cf.append([k, i])
    return cf


def duration(pv, cflist, y):
    # cf = [*cflist.keys()]
    # cftime = [*cflist.values()]
    dcf = 0
    for item in cflist:
        dcf += item[1] * item[0] / (1 + y) ** item[1]
    return dcf / pv


def modified_duration(pv, cflist, y):
    return duration(pv, cflist, y) / (1 + y)


def pv(cflist, y):
    dcf = 0
    for item in cflist:
        dcf += item[0] / (1 + y) ** item[1]
    return dcf


T = 2.5
FV = 1000
r = 0.05
y = 0.06

cf = {FV * r: (0.5, 1.5), FV * (1 + r): (2.5,)}
cflist = make_pairs(cf)
# print(cflist)
print(pv(cflist, y))
print(modified_duration(pv(cflist, y), cflist, y))

delta_y = [0.001, -0.001, 0.005, -0.005]

for delta in delta_y:
    print(
        f"Exact: {(pv(cflist, y +delta) - pv(cflist, y)):>8.4f} | Modified duration approximation:{-(pv(cflist,y)*modified_duration(pv(cflist,y),cflist,y)*delta):>8.4f}"
    )

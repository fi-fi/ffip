def my_nsolve(f, c, n=int(1e5), a=30, b=10e-5):
    x = 0
    for i in range(n):
        x += a / n
        if abs(f(x) - c) < b:
            return x


def make_pairs(assetdict):
    assetlist = []
    for k, v in assetdict.items():
        for i in v:
            assetlist.append([k, i])
    return assetlist


def md(assets):
    md = [i[0] * i[1] for i in assets]
    return sum(md)


a1, a2 = 10e9, 10e9
mda1, mda2 = 1, 3
l1 = 20e9
mdl1 = 1.5

assets = {a1: (mda1, mda2), -l1: (mdl1,)}
assetslist = make_pairs(assets)

print(f"{my_nsolve(
        lambda x: a1 * mda1 + a1 * mda2 - x * 10 + x * 1 - l1 * mdl1,
        0,
        n=int(10e8),
        a=20e10,
        b=10e3,
    ):.2E}")

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


def convexity(pv, cflist, y):
    dcf = 0
    for item in cflist:
        dcf += item[1] * (item[1] + 1) * item[0] / (1 + y) ** item[1]
    return dcf / (pv * (1 + y) ** 2)


def pv(cflist, y):
    dcf = 0
    for item in cflist:
        dcf += item[0] / (1 + y) ** item[1]
    return dcf


cf_constcb = {4: (1, 2, 3), 104: (4,)}
cf_zerocb = {100: (3.75,)}
y = 0.0929

constcb = make_pairs(cf_constcb)
zerocb = make_pairs(cf_zerocb)

# print(constcb)
# print(zerocb)

pv_constcb = pv(constcb, y)
pv_zerocb = pv(zerocb, y)

# print(pv_constcb)
# print(pv_zerocb)

print("Modified duration (const cp): ", modified_duration(pv_constcb, constcb, y))
print("Modified duration: (zero cp)", modified_duration(pv_zerocb, zerocb, y))

print("Convexity (const cp): ", convexity(pv_constcb, constcb, y))
print("Convexity (zero cp): ", convexity(pv_zerocb, zerocb, y))

newy = [0.0429, 0.1429]

pv_constcb_new = [pv(constcb, i) for i in newy]
pv_zerocb_new = [pv(zerocb, i) for i in newy]

# print(pv_constcb_new)
# print(pv_zerocb_new)

for i in range(len(newy)):
    print(f"Constant coupon bond:{(pv_constcb_new[i] - pv_constcb)/pv_constcb}")
    print(f"Zero coupon bond:{(pv_zerocb_new[i] - pv_zerocb)/pv_zerocb}")

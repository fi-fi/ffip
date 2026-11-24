# a) Value of coupons:

import QuantLib as ql


def daycountfactorf30_360(tf, ti):
    return (360 * (tf[2] - ti[2]) + 30 * (tf[1] - ti[1]) + (tf[0] - ti[0])) / 360


def namestr(obj, namespace):
    return [name for name in namespace if namespace[name] is obj]


# def daycountfactor(tf, ti):
#     fy,fm,fd = tf
#     iy,im,id = ti
#     yd, md, dd = fy-iy,fm-im,fd-id
#     dict = {1: 31, 2: 28, 3: 31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
#     days = 0
#     if iy == fy & iy % 4 == 0:
#         if im == fm:
#             return fd-id
#         else

#     for i in range(iy+1,fy):
#         if i % 4 == 0:
#             dict[2] = 29


FV = 10000
r = 0.1
cp = 99.8

US1 = [30, 2, 2024]
US2 = [30, 2, 2025]
US3 = [30, 2, 2026]

in0 = ql.Date(28, 2, 2023)
in1 = ql.Date(29, 2, 2024)
in2 = ql.Date(28, 2, 2025)
in3 = ql.Date(28, 2, 2026)

print("30/360 US:")
print(f"Coupons, 2024: {FV * r*daycountfactorf30_360([30,2,2024],[30,2,2023]):8.3f}")
print(f"Coupons, 2025: {FV * r*daycountfactorf30_360([30,2,2025],[30,2,2024]):8.3f}")
print(f"Coupons, 2026: {FV * r*daycountfactorf30_360([30,2,2026],[30,2,2025]):8.3f}")

print("30E/360:")
print(f"Coupons, 2024: {FV * r*daycountfactorf30_360([29,2,2024],[28,2,2023]):8.3f}")
print(f"Coupons, 2025: {FV * r*daycountfactorf30_360([28,2,2025],[29,2,2024]):8.3f}")
print(f"Coupons, 2026: {FV * r*daycountfactorf30_360([29,2,2026],[28,2,2025]):8.3f}")

print("ACT/ACT (ICMA):")
print(f"Coupons, 2024: {FV * r:8.3f}")
print(f"Coupons, 2025: {FV * r:8.3f}")
print(f"Coupons, 2026: {FV * r:8.3f}")

print("ACT/365 Fixed:")
print(f"Coupons, 2024: {FV * r*366/365:8.3f}")
print(f"Coupons, 2025: {FV * r:8.3f}")
print(f"Coupons, 2026: {FV * r:8.3f}")

# b) Calculate dirty price

US30_360 = ql.Thirty360(ql.Thirty360.USA)
E30_360 = ql.Thirty360(ql.Thirty360.European)
actact = ql.ActualActual(ql.ActualActual.ISMA)
act365 = ql.Actual365Fixed()

dcf1 = act365.yearFraction(in0, in1)
dcf2 = act365.yearFraction(in1, in2)
dcf3 = act365.yearFraction(in2, in3)

conv = [US30_360, E30_360, actact, act365]

startdate = ql.Date(28, 2, 2026)
enddate = ql.Date(3, 11, 2026)

for i in conv:
    print(
        f"Accrued interest {namestr(i,globals())[0]:8}: {i.yearFraction(startdate,enddate) * r* FV:8.4f}"
    )
    print(
        f"Dirty price {namestr(i,globals())[0]:8}: {(cp*100 + i.yearFraction(startdate,enddate) * r* FV)/100:8.4f}"
    )

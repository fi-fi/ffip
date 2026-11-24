import sympy as sp
import methods as mt

q, y, i, n, t = sp.symbols("q,y,i,n,t")

eq1 = sp.Eq(mt.compound_interest(q, 1, 1) ** n, 1 + y)
eq2 = sp.Eq(mt.cont_interest(q, 1), 1 + y)
sol1 = sp.solve(eq1, q)[0]
sol2 = sp.solve(eq2, q)[0]
effy1 = sp.lambdify((n, y), sol1)
effy2 = sp.lambdify((y), sol2)


periods = [4, 12, 52, 365]
y = 0.05
final = [effy1(n, y) for n in periods]
print(f"General formula for the interest rate per period for n periods:\n{sol1}\n")
print(f"General formula for the yearly continuous interest rate\n{sol2}\n")
for i in range(len(final)):
    print(
        f"Frequency: {periods[i]:<2}\nEffective periodwise interest rate: {final[i]*100:.3f} %\n"
    )
print(f"{effy2(y)*100:.3f} %")

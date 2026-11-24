from numpy import exp
import sympy as sp

from methods import simple_interest, compound_interest, cont_interest, my_nsolve


def simple_interest_fixed(t):
    return simple_interest(0.05, t)


def compound_interest_fixed(t):
    return compound_interest(0.05, t, 1)


def cont_interest_fixed(t):
    return cont_interest(0.05, t)


a = [1, 4, 12]

print("How many years we need to double the money assuming y =0.05?")
print("Simple interest: {:.3f} \n".format(my_nsolve(simple_interest_fixed, 2, b=10e-6)))
for i in a:
    print(
        "Compound interest, frequency: {}: {:.3f}".format(
            i, my_nsolve(lambda t: compound_interest(0.05, t, i), 2, b=10e-6)
        )
    )
print(
    "\nContinuous interest: {:.3f}".format(
        my_nsolve(lambda t: exp(0.05 * t), 2, b=10e-5)
    )
)

y, i, n, t = sp.symbols("y,i,n,t")

eq1 = sp.Eq(simple_interest(y, t), 1 + i)
eq2 = sp.Eq(compound_interest(y, t, n), 1 + i)
eq3 = sp.Eq(cont_interest(y, t), 1 + i)

sol1 = sp.solve(eq1, t)[0]
sol2 = sp.solve(eq2, t)[0]
sol3 = sp.solve(eq3, t)[0]

print(
    "\nGeneral formulas for simple, compound and continuous\nto be equal to fixed yield y:\n"
)
print("Simple: {}".format(sol1))
print("Compound: {}".format(sol2))
print("Continuous: {}".format(sol3))

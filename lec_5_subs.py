from sympy import symbols
from sympy import sin, cos, pi, exp

x, y, z = symbols("x y z")

expr = sin(x**2) - exp(-2*x) + cos(pi/x)

expr_new = expr.subs(x, y)
print(expr_new)

expr_new = expr.subs(x, pi)
print(expr_new)

expr_nuw = expr_new.evalf()
print(expr_nuw)

expr_new = expr.subs(x, x**2)
print(expr_nuw)

print(type(expr))

expr = x**3 + 4*x*y - z
expr_new = expr.subs([(x, 2), (y, 4), (z, 0)])
print(expr_new)


from sympy import symbols
from sympy import sin, cos, pi, exp
from sympy import simplify, expand, factor, trigsimp
from sympy import solveset, linsolve, nonlinsolve, Eq, solve
from sympy import Abs

x, y, z =symbols("x y z")
simp_expr = simplify((x*y**2)-(2*x*y*z)+(x*z**2)+(y**2)-(2*y*z)+(z**2))/((x**2)-1)
print(simp_expr)


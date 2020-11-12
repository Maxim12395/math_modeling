from sympy import symbols
from sympy import sin, cos, pi, exp
from sympy import simplify, expand, factor, trigsimp
from sympy import solveset, linsolve, nonlinsolve, Eq, solve

x, y, z = symbols("x y z")

expr = x**2 - 2
solve_expr = solve(expr, x)
print(solve_expr)

expr = sin(x**2) - exp(-2*x) + cos(pi/x)
solve_expr = solve(expr, x)
print(solve_expr)
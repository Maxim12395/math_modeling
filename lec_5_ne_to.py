from sympy import symbols
from sympy import sin, cos, pi, exp
from sympy import simplify, expand, factor, trigsimp
from sympy import solveset, linsolve, nonlinsolve, solve, Eq

system = [x + y + z - 1, x + y + 2*z - 3, x - 2*y + z]
solve_system = linsolve(system, (x, y, z))
print(solve_system)

system = [x**2 + x, x - y]
solve_system = nonlinsolve(system, [x, y])
print(solve_system)
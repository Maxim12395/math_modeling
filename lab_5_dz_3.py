from sympy import symbols
from sympy import sin,cos,pi,exp
from sympy import simplify,expand,factor,trigsimp
from sympy import Eq,solve,solveset,linsolve,nonlinsolve
from sympy.solvers.inequalities import reduce_abs_inequality
from sympy.solvers.inequalities import reduce_rational_inequalities
from sympy import Abs

x, E =symbols("x E")

solv_expr = (((x**2) + x + (1/x) + (1/(x**2))) -4)

solvset_expr = solveset(solv_expr, x)
print(solvset_expr)


e = 0.8
M = 9
solv_expr1 = E - e * sin (E) - M
solvset_expr = solveset(solv_expr1, E)
print(solvset_expr)
from sympy import sqrt
from sympy import symbols
from sympy import sin, cos, pi, exp
from sympy import simplify, expand, factor, trigsimp
from sympy import solveset, linsolve, nonlinsolve, Eq, solve
from sympy import Abs
from sympy.vector import CoordSys3D
from sympy import dot

N = CoordSys3D("N")

a, b, c, i, j, k  =symbols(" a b c i j k")

a = 4*N.i + 3*N.j + 8*N.k
b = -2*N.i + 8*N.j + 7*N.k
c = -5*N.i - 6*N.j + 12*N.k

a.dot(a, b)
a.dot(a, c)
a.dot(b, c)

print(a.dot)

from sympy.abc import a, b
from sympy import pprint

expr = b * a + -4 * a + b + a * b + 4 * a + (a + b) * 3

print(expr.subs([(a, 3), (b, 2)]))

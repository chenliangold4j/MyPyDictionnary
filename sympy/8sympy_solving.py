from sympy import Symbol, solve

x = Symbol('x')

sol = solve(x ** 2 - x, x)

print(sol)

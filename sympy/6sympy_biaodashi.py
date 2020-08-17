# SymPy 比较表达式
# SymPy 表达式与equals()而不是==运算符进行比较。

from sympy import pprint, Symbol, sin, cos, pi


x = Symbol('x')

a = cos(x) ** 2 - sin(x) ** 2
b = cos(2 * x)

print(a.equals(b))

# we cannot use == operator
print(a == b)

# 可以通过替换符号来求值表达式。
#
print(pi.evalf(30))


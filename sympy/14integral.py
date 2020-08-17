from sympy import *

x = Symbol('x')

y0 = x ** 2

y1 = x / (x ** 2 + 8)

y2 = 1 / (x * ln(x))

print(integrate(y0, (x, 0, 2)))  # 计算x^2关于x从0到2的积分

print(integrate(y1, (x, 0, x)))  # 计算x/(x^2+8)关于x从0到x的积分

print(integrate(y2, (x, 5, x)))  # 计算1/(xln(x))关于x从5到x的积分

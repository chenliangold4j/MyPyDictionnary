# SymPy 具有用于处理有理数的Rational。 有理数是可以表示为两个整数（分子 p 和非零分母 q）的商或分数 p / q 的任何数字

from sympy import Rational
r1 = Rational(1/10)
r2 = Rational(1/10)
r3 = Rational(1/10)

val = (r1 + r2 + r3) * 3
print(val.evalf())

# 注意，当不使用有理数时，输出中会有一个小错误
val2 = (1/10 + 1/10 + 1/10) * 3
print(val2)

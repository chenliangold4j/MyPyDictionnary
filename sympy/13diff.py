# 使用sympy.diff求导定义函数  ，求解其导数
from sympy import *

init_printing(use_unicode=True)
x = symbols("x")
f = log(x)
# 一阶导数
pprint(diff(f, x))
# 二阶导数可以传入第三个参数，表示阶数
pprint(diff(f, x, 2))

print("--------------------------------")

f2 = tan(x)
pprint(diff(f2, x))



# 使用expand()，我们可以扩展代数表达式； 即该方法尝试消除幂和乘法。
from sympy import expand,sin, cos, simplify, pprint
from sympy.abc import x

expr = (x + 1) ** 2

pprint(expr)

print('-----------------------')
print('-----------------------')

expr = expand(expr)
pprint(expr)

# 可以使用simplify()将表达式更改为更简单的形式。
expr = sin(x) / cos(x)

pprint(expr)

print('-----------------------')

expr = simplify(expr)
pprint(expr)
from sympy import Symbol, symbols
# 可以从sympy.abc模块导入符号。 它将所有拉丁字母和希腊字母导出为符号，因此我们可以方便地使用它们。
from sympy.abc import x, y

expr = 2 * x + 5 * y
print(expr)

# 可以用Symbol定义
a = Symbol('a')
b = Symbol('b')

expr2 = a * b + a - b
print(expr2)

# 可以使用symbols()方法定义多个符号。
i, j = symbols('i j')
expr3 = 2 * i * j + i * j
print(expr3)
# 该程序显示了三种在 SymPy 中定义符号的方法。


# SymPy 会自动将表达式转换为规范形式。 SymPy 仅执行廉价操作； 因此，表达式可能无法求值为最简单的形式。
expr = b*a + -4*a + b + a*b + 4*a + (a + b)*3

print(expr)


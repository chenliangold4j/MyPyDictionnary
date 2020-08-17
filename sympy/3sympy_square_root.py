# 平方根是一个数字，乘以它会产生指定的数量。
from sympy import sqrt, pprint, Mul

x = sqrt(2)
y = sqrt(2)

pprint(Mul(x, y, evaluate=False))
print('equals to ')
print(x * y)

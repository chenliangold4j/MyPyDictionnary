from sympy import *


def sympy_derivative():
    # 定义表达式的变量名称
    x1, x2 = symbols('x1 x2')
    # 定义表达式内容
    Y = x1 ** 2 + x2 ** 2
    # 计算 x2对应的偏导数
    return diff(Y, x2)


# sympy 带入值计算
func = sympy_derivative()
print(func)  # 输出结果2*x2
print(func.evalf(subs={'x2': 6}))  # 把x2 等于6 带入计算 结果 为12

# 其中 func.evalf(subs={}) 为特征值带入计算的api，需特殊说明的是，该函数运行结果，可能还只是表达式，其主要是求解已经给的特征值

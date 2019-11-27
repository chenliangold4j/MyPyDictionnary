L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[0:3]);
# L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素。
# 如果第一个索引是0，还可以省略：
print(L[:3]);
# 类似的，既然Python支持L[-1]取倒数第一个元素，那么它同样支持倒数切片，试试：
print(L[-2:])
L = list(range(100))
# 前10个数，每两个取一个：
print(L[:10:2])
# 甚至什么都不写，只写[:]就可以原样复制一个list：
# ，tuple也可以用切片操作，只是操作的结果仍是tuple：
# 字符串也可以用切片操作，只是操作结果仍是字符串：
print('ABCDEFG'[:3])

# 迭代
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)
# 那么，如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断：
from collections.abc import Iterable

print(isinstance('abc', Iterable))
print(isinstance([1, 2, 3], Iterable))

# Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

# 列表生成器
print(list(range(1, 11)));
print([x * x for x in range(1, 11)])
print([m + n for m in 'ABC' for n in 'XYZ'])
# 运用列表生成式，可以写出非常简洁的代码。例如，列出当前目录下的所有文件和目录名，可以通过一行代码实现：
import os

print([d for d in os.listdir('.')])

# for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value：
d = {'x': 'A', 'y': 'B', 'z': 'C'}
for k, v in d.items():
    print(k, '=', v)
L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])

# 在Python中，这种一边循环一边计算的机制，称为生成器：generator
L = [x * x for x in range(10)]
print(L)
g = (x * x for x in range(10))
print(g)
# 创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator。
print(next(g))
print(next(g))
print(next(g))
print(next(g))


# generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误

# 定义generator的另一种方法。如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator：
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


f = fib(6)
print(f)
# 。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。而变成generator的函数，
# 在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。

# 用for循环调用generator时，发现拿不到generator的return语句的返回值。如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中：
g = fib(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break
# 迭代器
# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
#
from collections.abc import Iterator

print(isinstance((x for x in range(10)), Iterator))  # true
print(isinstance((x for x in range(10)), Iterable))  # true
print(isinstance([], Iterator))  # false
print(isinstance([], Iterable))  # true
print(isinstance({}, Iterator))  # false
print(isinstance({}, Iterable))  # true
print(isinstance('abc', Iterator))  # false
print(isinstance('abc', Iterable))  # true

# 把list、dict、str等Iterable变成Iterator可以使用iter()
# 函数：
print(isinstance(iter([]), Iterator))
print(isinstance(iter('abc'), Iterator))
# Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration错误。
# 可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据，
# 所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。
#
# Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。
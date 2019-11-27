# python中 && || ！ 分别是 and or not
print(True and False)
print(True or False)
print(not True)

#空值是Python里一个特殊的值，用None表示。None不能理解为0，因为0是有意义的，而None是一个特殊的空值
a=123
print(a)
a='abc'
print(a)

#python还有一种除法是//，称为地板除，两个整数的除法仍然是整数

print(10 // 3)

#对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符：
print(ord('A'))
print(ord('中'))
print(chr(66))
print(chr(25991))
print(len('ABC'))
print(len('中文'))

#在Python中，采用的格式化方式和C语言是一致的，用%实现，举例如下：
# 如果你不太确定应该用什么，%s永远起作用，它会把任何数据类型转换为字符串：

print( 'Hello, %s' % 'world')
print('Hi, %s, you have $%d.' % ('Michael', 1000000))

# %d	整数
# %f	浮点数
# %s	字符串
# %x	十六进制整数
# 当str和bytes互相转换时，需要指定编码。最常用的编码是UTF-8
print( '中文'.encode('gb2312'))
print('中文'.encode('utf-8'))

#Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
# 如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引 以此类推，可以获取倒数第2个、倒数第3个：
print(classmates[-1])

#追加
classmates.append('Adam')
print(classmates)

#插入
classmates.insert(1, 'Jack')
print(classmates)

# 要删除指定位置的元素，用pop(i)方法，其中i是索引位置：
classmates.pop(1)
print(classmates)

#要把某个元素替换成别的元素
classmates[1] = 'Sarah'
print(classmates)
# list元素也可以是另一个list，比如：
s = ['python', 'java', ['asp', 'php'], 'scheme']
print(len(s))
# 因此s可以看成是一个二维数组，类似的还有三维、四维……数组

# 另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改

classmates = ('Michael', 'Bob', 'Tracy')
# classmates这个tuple不能变了，它也没有append()，insert()这样的方法。其他获取元素的方法和list是一样的，你可以正常地使用classmates[0]，classmates[-1]，但不能赋值成另外的元素。
# 最后来看一个“可变的”tuple：
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
print(t)

#注意缩进
age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

# 只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。
x=''
if x:
    print('True')

#输入与转换
# s = input('birth: ')
# birth = int(s)
# if birth < 2000:
#     print('00前')
# else:
#     print('00后')

sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)

# Python提供一个range()函数，可以生成一个整数序列，再通过list()函数可以转换为list。比如range(5)生成的序列是从0开始小于5的整数：
print(list(range(5)))

n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')

# Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d["Michael"])
d['Jack'] = 90
print(d)
# 如果key不存在，dict就会报错：有两种办法，一是通过in判断key是否存在：二是通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value：

print('Thomas' in d)
print(d.get('Thomas'))
print(d.get('Thomas', -1))
#要删除一个key，用pop(key)方法，对应的value也会从dict中删除：
# 要保证hash的正确性，作为key的对象就不能变。在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key：

# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
s = set([1, 1, 2, 2, 3, 3])
print(s)
# ?通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果：
# 通过remove(key)方法可以删除元素
# set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)
print(s1 | s2)

#可变不可变
a = ['c', 'b', 'a']
a.sort()
print(a)
a = 'abc'
b = a.replace('a', 'A')
print(b)
print(a)

#函数定义
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

print(my_abs(-99))

# 如果想定义一个什么事也不做的空函数，可以用pass语句：
def nop():
    pass
# 实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。
if age >= 18:
    pass
# 缺少了pass，代码运行就会有语法错误。

# 对参数类型做检查，只允许整数和浮点数类型的参数。数据类型检查可以用内置函数isinstance()实现：
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

# 返回多个值
import math
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
x, y = move(100,100,60,math.pi/6)
print(x, y)
# 但其实这只是一种假象，Python函数返回的仍然是单一值：
r = move(100, 100, 60, math.pi / 6)
print(r)

# 这个时候，默认参数就排上用场了。由于我们经常计算x2，所以，完全可以把第二个参数n的默认值设定为2：
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
# 这样，当我们调用power(5)时，相当于调用power(5, 2)：

def add_end(L=[]):
    L.append('END')
    return L
print(add_end([1, 2, 3]))
print(add_end())
print(add_end())
# Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，
# 因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时
# ，默认参数的内容就变了，不再是函数定义时的[]了
# 定义默认参数要牢记一点：默认参数必须指向不变对象！
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
print(add_end())
print(add_end())

# 可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc(1, 2))
# Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去：
nums = [1, 2, 3]
print(calc(*nums))

# 关键字参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

print(person('Michael', 30))
print(person('Adam', 45, gender='M', job='Engineer'))

# 命名关键字参数
# 如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下：
def person(name, age, *, city, job):
    print(name, age, city, job)





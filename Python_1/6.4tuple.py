# -*- coding: utf-8 -*-
# @Time    : 2018/12/2 15:06
# Todo
# @File    : 6.4tuple.py
# 1.定义只有一个元素的tuple
t0 = (1)
print(t0)
print(type(t0))  # <class 'int'>
t00 = (1,)
print(type(t00))

# 2.如果在tuple中定义一个list，那么list是否可以改变呢？
print("# 2.如果在tuple中定义一个list，那么list是否可以改变呢？")
t01 = (1, 2, 3, ["Apple", "pear"])
print(t01)
print(t01[0])
print(t01[1])
print(t01[2])
print(t01[3])
print(t01[3][0])
print(t01[3][1])
t01[3][0] = "banana"
print(t01)  # (1, 2, 3, ['banana', 'pear'])

# 3.tuple与各个数据结构类型的转换
print("# 3.tuple与各个数据结构类型的转换")
t1 = (1, 2, 3, 4)
# r = range(10)
# print(type(r))
# print(r)

t2 = tuple(range(10))
t3 = tuple([1, 2, 3, 4])  # list转tuple
t4 = tuple({1, 2, 3, 4, 1, 2, 3, 3, 4, 5})  # set转tuple,去重
t5 = tuple({1: "apple", 2: "banana", 3: "orange"})  # dict转tuple
print(t1)
print(t2)
print(t3)
print(t4)
print(t5)

# 4.切片操作
print("# 4.切片操作")
# (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(t2[::])
print(t2[::-1])  # 倒序
print(t2[1:5])
print(t2[1:5:])
print(t2[1:4:])  # (1, 2, 3)
print(t2[:8])  # (0, 1, 2, 3, 4, 5, 6, 7)
print(t2[::2])  # (0, 2, 4, 6, 8) 偶数
print(t2[1::2])  # (1, 3, 5, 7, 9) 奇数

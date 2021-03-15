# -*- coding: utf-8 -*-
# @Time    : 2018/12/2 15:31
# Todo
# @File    : 6.7set.py
# 集合-创建以及各个数据结构的转换
set1 = {1, 2, 3, 4, 5}
set2 = set(range(10))
set3 = set([1, 2, 3, 4])  # list转set
set4 = set((1, 2, 3, 4))  # tuple转set
set5 = set({"Apple": 1, "pear": 2})  # dict转set
print(set1)
print(set2)
print(set3)
print(set4)
print(set5)
# 集合的增加元素
set1.add(100)
print(set1)

# 集合的删除元素
set1.remove(100)
print(set1)

# 集合的更新操作
set1.update({100, 200, 300})
print(set1)

print(":" * 100)
# 集合的运算------交并补
s5 = {1, 2, 3, 4, 5}
s6 = {4, 5, 6, 7, 8}
s7 = {4, 5}

# 补集就是对于一个集合A和全集B来说，A的补集就是在全集B中所有不属于A的元素。
# 差集是对于两个集合来说的，假设两个集合A，B。A-B就是属于A但是不属于B的元素的集合。
print(s5 - s6)  # 集合的差集
print(s5.difference(s6))

print(s5 | s6)  # 集合的并集
print(s5.union(s6))

print(s5 & s6)  # 集合的交集
print(s5.intersection(s6))

print(s5 ^ s6)  # a 和 b 中不同时存在的元素

print(":" * 100)

# 集合和集合的包含运算
print(s7 < s5)
print(s6 < s5)

# list(列表)转set(集合)
l1 = [1, 2, 3, 4, 1, 2, 3, 4, 5, 6, 12, 3, 4]
print(set(l1))  # {1, 2, 3, 4, 5, 6, 12}

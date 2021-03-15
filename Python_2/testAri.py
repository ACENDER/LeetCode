# -*- coding: utf-8 -*-
# @Time    : 2018/12/2 21:01_抽象数据类型和面向对象编程

# Todo 
# @File    : testAri.py

from zML.Python_2.ArithMaticDemo import ArithMatic

x = int(input("please input your number:"))
y = int(input("please input your another number:"))
artical = ArithMatic(x, y)
print(artical.add())
print(artical.sub())
print(artical.mul())
print(artical.div())

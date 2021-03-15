# -*- coding: utf-8 -*-
# @Time    : 2018/12/2 21:01_抽象数据类型和面向对象编程

# Todo 
# @File    : ArithMaticDemo.py
class ArithMatic():
    def __init__(self, x, y):
        self.X = x
        self.Y = y

    def add(self):
        return self.X + self.Y

    def sub(self):
        return self.X - self.Y

    def mul(self):
        return self.X * self.Y

    def div(self):
        return self.X / self.Y

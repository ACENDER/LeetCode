# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File : 斐波那契数.py  @Time : PyCharm -lqj- 2021-1-4 0004
class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        a, b, c = 0, 0, 1
        for i in range(2, n + 1):
            a, b = b, c
            c = a + b
        return c

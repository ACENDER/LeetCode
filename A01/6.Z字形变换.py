# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File : 6. Z 字形变换.py  @Time : PyCharm -lqj- 2020-9-22 0022

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2: return s
        res = ["" for _ in range(numRows)]
        i, flag = 0, -1
        for c in s:
            res[i] += c
            if i == 0 or i == numRows - 1: flag = -flag
            i += flag
        return "".join(res)
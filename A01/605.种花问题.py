# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File : 605. 种花问题.py  @Time : PyCharm -lqj- 2021-1-4 0004
from typing import List


# https://leetcode-cn.com/problems/can-place-flowers/solution/chong-hua-wen-ti-by-leetcode-solution-sojr/
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        tmp = [0] + flowerbed + [0]
        for i in range(1, len(tmp) - 1):
            if tmp[i] == 0 and tmp[i - 1] == 0 and tmp[i + 1] == 0:
                tmp[i] = 1
                n -= 1
        return n <= 0


''':arg
两边补0
连续三个 0 就可以种花
'''

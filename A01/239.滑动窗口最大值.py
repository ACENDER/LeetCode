# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File : 239. 滑动窗口最大值.py  @Time : PyCharm -lqj- 2021-1-4 0004
# https://leetcode-cn.com/problems/sliding-window-maximum/
from typing import List
from collections import deque

''':arg
小于新加的 全部弹出

'''


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        win, ret = [], []
        for i, v in enumerate(nums):
            if i >= k and win[0] <= i - k:
                win.pop(0)
            while win and nums[win[-1]] <= v:
                win.pop()
            win.append(i)
            if i >= k - 1:
                ret.append(nums[win[0]])
        return ret

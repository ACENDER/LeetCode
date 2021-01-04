# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File : 349. 两个数组的交集.py  @Time : PyCharm -lqj- 2020-11-2 0002
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = set()
        for x in nums1:
            for y in nums2:
                if x == y:
                    result.add(x)
        return result

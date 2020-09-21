# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File : 1.py  @Time : PyCharm -lqj- 2020-9-20 0020

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        for i, num in enumerate(nums):

            if (target - num) in num_to_index:
                return [num_to_index[target - num], i]
            num_to_index[num] = i  # 先遍历nums 将
        return []

if __name__ == '__main__':
    for i, num in enumerate([1, 2, 3, 4, 5]):
        print(i, num)

# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File : 78.子集.py  @Time : PyCharm -lqj- 2020-9-20 0020
# Todo  :
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nb_subsets = 2 ** len(nums)  # 2的n次方 个子集数
        all_subsets = []

        for subset_nb in range(nb_subsets):  # 0 1 2 3
            subset = []
            for num in nums: # 1 2
                if subset_nb % 2 == 1:
                    subset.append(num)
                subset_nb //= 2
            all_subsets.append(subset)
        return all_subsets

# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File : 830. 较大分组的位置.py  @Time : PyCharm -lqj- 2021-1-5 0005
from typing import List


class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        l = list(s)
        res = []
        n, num = len(l), 1
        for i in range(n):
            if i == n - 1 or l[i] != l[i + 1]:
                if num >= 3:
                    res.append([i - num + 1, i])
                num = 1
            else:
                num += 1
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.largeGroupPositions("xxxxabc"))

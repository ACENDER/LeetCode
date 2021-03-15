# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File : 54. 螺旋矩阵.py  @Time : PyCharm -lqj- 2021-3-15 0015
# https://leetcode-cn.com/problems/spiral-matrix/
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        x, y, d, m, n = 0, 0, 0, len(matrix[0]), len(matrix)
        print( x, y, d, m, n)
        res = [None] * (m * n)
        # 定义方向
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        for i in range(m * n):
            print(i, '(', x, y, ')')
            print('matrix[x][y]',matrix[x][y])
            res[i] = matrix[x][y]
            print(res)
            matrix[x][y] = None
            nx, ny = x + direction[d][0], y + direction[d][1]
            print("-"*100)
            print(nx, ny)
            if nx < 0 or nx >= n or y < 0 or ny >= m or matrix[nx][ny] is None:
                d = (d + 1) % 4
                nx, ny = x + direction[d][0], y + direction[d][1]
            x, y = nx, ny

        return res


if __name__ == '__main__':
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    solution = Solution()
    print(solution.spiralOrder(matrix))

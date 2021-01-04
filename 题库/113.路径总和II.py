# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File : 113. 路径总和 II.py  @Time : PyCharm -lqj- 2020-9-26 0026


# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, total: int) -> List[List[int]]:
        ret = list()
        path = list()

        def dfs(root: TreeNode, total: int):
            if not root:
                return
            path.append(root.val)
            total -= root.val
            if not root.left and not root.right and total == 0:
                ret.append(path[:])
            dfs(root.left, total)
            dfs(root.right, total)
            path.pop()

        dfs(root, total)
        return ret

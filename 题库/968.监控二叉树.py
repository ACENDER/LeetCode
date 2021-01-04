# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File : 968. 监控二叉树.py  @Time : PyCharm -lqj- 2020-9-22 0022

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        def dfs(root: TreeNode) -> List[int]:
            if not root:
                return [float("inf"), 0, 0]

            la, lb, lc = dfs(root.left)
            ra, rb, rc = dfs(root.right)
            a = lc + rc + 1
            b = min(a, la + rb, ra + lb)
            c = min(a, lb + rb)
            return [a, b, c]

        a, b, c = dfs(root)
        return b

    # covered = {}
    #
    # def helper(node, parent):
    #     if not node:
    #         return 0
    #     result = helper(node.left, node) + helper(node.right, node)
    #     if node.left not in covered or node.right not in covered:
    #         covered.update({parent, node, node.left, node.right})
    #         result += 1
    #     return result
    #
    # cameras = helper(root, None)
    # return cameras if root in covered else cameras + 1

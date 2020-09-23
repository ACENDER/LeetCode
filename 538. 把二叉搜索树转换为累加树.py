# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File : 538. 把二叉搜索树转换为累加树.py  @Time : PyCharm -lqj- 2020-9-21 0021

# 二叉树节点的定义。

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.running_sum = 0

        def inorder(node: TreeNode):
            if not node:
                return

            inorder(node.right)

            node.val += self.running_sum
            self.running_sum = node.val

            inorder(node.left)

        inorder(root)
        return root

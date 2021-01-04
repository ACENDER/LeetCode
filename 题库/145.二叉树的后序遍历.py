# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File : 145. 二叉树的后序遍历.py  @Time : PyCharm -lqj- 2020-9-29 0029

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
1 递归
时间复杂度：O(n)，其中 nn 是二叉搜索树的节点数。每一个节点恰好被遍历一次。
空间复杂度：O(n)，为递归过程中栈的开销，平均情况下为 O(log n)，最坏情况下树呈现链状，为 O(n)
"""


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        def postorder(root: TreeNode):
            if not root:
                return
            postorder(root.left)
            postorder(root.right)
            res.append(root.val)

        res = list()
        postorder(root)
        return res


"""
2 迭代
"""


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return list()

        res = list()
        stack = list()
        prev = None

        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if not root.right or root.right == prev:
                res.append(root.val)
                prev = root
                root = None
            else:
                stack.append(root)
                root = root.right

        return res


"""
3 Morris 遍历
"""


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        def addPath(node: TreeNode):
            tmp = list()
            while node:
                tmp.append(node.val)
                node = node.right
            res.extend(tmp[::-1])

        if not root:
            return list()

        res = list()
        p1 = root

        while p1:
            p2 = p1.left
            if p2:
                while p2.right and p2.right != p1:
                    p2 = p2.right
                if not p2.right:
                    p2.right = p1
                    p1 = p1.left
                    continue
                else:
                    p2.right = None
                    addPath(p1.left)
            p1 = p1.right

        addPath(root)
        return res

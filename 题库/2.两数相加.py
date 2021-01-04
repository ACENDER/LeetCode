# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File : 2. 两数相加.py  @Time : PyCharm -lqj- 2020-9-20 0020

# 单链列表的定义。
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        prev = result = ListNode(None)  # 保存头结点,返回结果
        carry = 0  # 每一步的求和变量
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            prev.next = ListNode(carry % 10)
            prev = prev.next
            carry //= 10
        return result.next

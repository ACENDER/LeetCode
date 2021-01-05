# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File : 141. 环形链表.py  @Time : PyCharm -lqj- 2020-10-9 0009
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 遍历
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        seed = set()
        while head:
            if head in seed:
                return True
            seed.add(head)
            head = head.next
        return False


# 双指针 (一快一慢)
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True

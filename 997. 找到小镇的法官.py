# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File : 997. 找到小镇的法官.py  @Time : PyCharm -lqj- 2020-9-29 0029

"""

"""

"""
两个数组

思路

如果熟悉图的话，应该知道这是一道有向图问题。 并且法官👩‍⚖️ 实际上就是出度为0，入度为 N - 1的节点。
因此一个思路就是统计所有人的入度和出度信息，将满足出度为0，入度为 N - 1的节点输出。
这里用两个数组 in_degree 和 out_degree 分别记录入度和出度的信息，为了简单起见，我们初始化的数组长度为 N + 1，而不是 N。

具体算法如下：

遍历 trust，如果 trust[i] 为 [a, b] 说明 a 信任 b，那么更新 a 的出度 + 1，b 的入读 + 1。
遍历所有节点，将满足出度为0，入度为 N - 1的节点输出。

复杂度分析

时间复杂度：O(N)
空间复杂度：O(N)
"""


class Solution:
    def findJudge(self, N, trust):
        in_degree = [0] * (N + 1)  # 入度
        out_degree = [0] * (N + 1)  # 出度
        for a, b in trust:
            in_degree[b] += 1
            out_degree[a] += 1
        for i in range(1, N + 1):
            if in_degree[i] == N - 1 and out_degree[i] == 0:
                return i
        return -1


"""
一个数组
思路
上面的分析中指出了法官👩‍⚖️ 实际上就是出度为0，入度为 N - 1的节点。这固然没错，然而我们仍然可以换个角度来思考，法官👩‍⚖️ 同样是 入度 - 出度 == N - 1 的点，并且不是法官的人不可能是。

这样我们无需同时维护入度和出度的信息，转而维护入读和出度的差值即可。
"""


class Solution:
    def findJudge(self, N, trust):
        count = [0] * (N + 1)
        for i, j in trust:
            count[i] -= 1
            count[j] += 1
        for i in range(1, N + 1):
            if count[i] == N - 1:
                return i
        return -1

# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File : 834. 树中距离之和.py  @Time : PyCharm -lqj- 2020-10-8 0008
from typing import List


class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        tree = [[] for _ in range(N)]
        for baba, erza in edges:
            tree[baba].append(erza)
            tree[erza].append(baba)
        depth = [0 for _ in range(N)]
        count = [0 for _ in range(N)]


        def dfsForDepthAndCount(baba0, father):
            count[baba0] = 1
            for erza0 in tree[baba0]:
                if erza0 != father:
                    depth[erza0] = depth[baba0] + 1
                    dfsForDepthAndCount(erza0, baba0)
                    count[baba0] += count[erza0]


        dfsForDepthAndCount(0, -1)
        answer = [0 for _ in range(N)]
        answer[0] = sum(depth)


        def dfsForAnswer(baba1, father):
            for erza1 in tree[baba1]:
                if erza1 != father:
                    answer[erza1] = answer[baba1] + N - 2 * count[erza1]
                    dfsForAnswer(erza1, baba1)


        dfsForAnswer(0, -1)
        return answer


class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(N)]
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        dist_sum = [0 for _ in range(N)]
        node_num = [1 for _ in range(N)]

        def post_order(node, parent):
            for n in graph[node]:
                if n == parent:
                    continue
                post_order(n, node)
                node_num[node] += node_num[n]
                dist_sum[node] += dist_sum[n] + node_num[n]

        def pre_order(node, parent):
            for n in graph[node]:
                if n == parent:
                    continue
                dist_sum[n] = dist_sum[node] - node_num[n] + (N - node_num[n])
                pre_order(n, node)

        post_order(0, -1)
        pre_order(0, -1)
        return dist_sum


class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        d = [[] for _ in range(N)]
        for i, j in edges:
            d[i].append(j)
            d[j].append(i)
        ans, s = [0] * N, [1] * N

        def f(i, p):
            for j in d[i]:
                if j != p:
                    f(j, i)
                    s[i] += s[j]
                    ans[i] += ans[j] + s[j]

        f(0, -1)

        def g(i, p):
            for j in d[i]:
                if j != p:
                    ans[j] = N - s[j] * 2 + ans[i]
                    g(j, i)

        g(0, -1)
        return ans


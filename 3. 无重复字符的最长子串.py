# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File : 3. 无重复字符的最长子串.py  @Time : PyCharm -lqj- 2020-9-21 0021


class Solution:

    def lengthOfLongestSubstring(self, s: str):
        # 哈希集合，记录每个字符是否出现过
        # k, res, c_dict = -1, 0, {}
        # for i, c in enumerate(s):
        #     if c in c_dict and c_dict[c] > k:  # 字符c在字典中 且 上次出现的下标大于当前长度的起始下标
        #         k = c_dict[c]
        #     else:
        #         res = max(res, i-k)
        #     c_dict[c] = i
        # return res
        #
        c_dict = {}  # 记录每个字符是否出现过
        start = -1  # 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动
        longest = 0
        for index, char in enumerate(s):
            if char in c_dict and c_dict[char] > start:
                start = c_dict[char]
            else:
                longest = max(longest, index - start)  # 哪个大取值为哪个
            c_dict[char] = index  # 更新最后的目击索引
        return longest


if __name__ == '__main__':
    solution = Solution()
    substring = solution.lengthOfLongestSubstring("abcabcbb")
    print(substring)

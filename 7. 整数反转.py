# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File : 7. 整数反转.py  @Time : PyCharm -lqj- 2020-9-22 0022


class Solution:

    def reverse(self, x: int) -> int:

        ans = 0
        if x > 0:
            while x != 0:
                ans = ans * 10 + x % 10
                x //= 10
        if x < 0:
            x = 0 - x
            print(x)
            while x != 0:
                ans = ans * 10 + x % 10
                print(ans)
                x //= 10
            ans = 0 - ans
            print(ans)
        if (-2 ** 31) < ans < (2 ** 31 - 1):
            return ans
        return 0
        # ans = 0
        #
        # while (x != 0):
        #     tmp = x % 10
        #     if ans > 214748364 or ans == 214748364 and tmp > 7:
        #         return 0
        #
        #     if ans < -214748364 or ans == -214748364 and tmp < -8:
        #         return 0
        #
        #     ans = ans * 10 + tmp
        #     x /= 10
        # return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.reverse(-123))

# -*- coding: utf-8 -*-
# @Time    : 2018/12/2 11:29
# @Author : liqijia PyCharm  @Time : 2020/3/25
# Todo
# @File    : 3.0elemntType.py
a = 199.0
b = 199.0
print(id(199.0))  # 返回对象标识
print(id(a))
print(id(b))

print("hash值", hash("staring"))
print(type(a))  # <class 'float'>
print(isinstance(a, int))
print(isinstance(a, float))

print(":" * 100)
# 补充复数类型
c1 = complex(1, 2)  # 1+2j    j**2=-1
print(c1)  # (1+2j)(1+2j)=1-4+4j=-3+4j
print(c1 ** 2)  # (-3+4j)

print(":" * 100)
# 单目运算符+ - *乘法 /除法  //整除 **幂 %取模
a = 3
b = 7
print(a + b)
print(a - b)
print(a * b)
print(a ** b)
print(a % b)
print(a / b)
print(a // b)

print(":" * 100)

# 双目运算符---+= -=  *= /= %=  **= //=
print("before value is：", a)
a *= b
print("change value is：", a)
a **= b
print("change value is：", a)
a += b
print("change value is：", a)
a -= b
print("change value is：", a)
a //= b
print("change value is：", a)
print(":" * 100)
# & 按位与 | 按位或 ^按位异或 <<左移 >> 右移
a = 3  # 0011
b = 5  # 0101
# &     0001---------1
# |     0111---------7
# ^     0110---------6
# a>1  除以2   a<乘以2
# 8421  2**3   2**2  2**1 2**0
#
# &	按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0
# |	按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1
# ^	按位异或运算符：当两对应的二进位相异时，结果为1
# ~	按位取反运算符：对数据的每个二进制位取反,即把1变为0,把0变为1
# <<	左移动运算符：运算数的各二进位全部左移若干位，由"<<"右边的数指定移动的位数，高位丢弃，低位补0
# >>	右移动运算符：把">>"左边的运算数的各二进位全部右移若干位，">>"右边的数指定移动的位数
print(a & b)
print(a | b)
print(a ^ b)
print(~a)
print(a << 1)
print(a << 2)
print(a >> 1)

# -*- coding: utf-8 -*-
# @Time    : 2018/12/2 11:10

# Todo 
# @File    : 1.0Python2_3.py

print("hello")
# 编码方式
print("卢本伟牛逼！")
# 查看编码方式
import sys

print(sys.getdefaultencoding())
# python2-ascii
# python-utf-8-------unicode transform format 8bytes    Unicode
# 案例
str = "卢本伟牛逼"
print(str.encode("utf-8"))
print(str.encode("gbk"))
# b'\xe5\x8d\xa2\xe6\x9c\xac\xe4\xbc\x9f\xe7\x89\x9b\xe9\x80\xbc'
# b'\xc2\xac\xb1\xbe\xce\xb0\xc5\xa3\xb1\xc6'
print(b'\xe5\x8d\xa2\xe6\x9c\xac\xe4\xbc\x9f\xe7\x89\x9b\xe9\x80\xbc'.decode())
print(b'\xc2\xac\xb1\xbe\xce\xb0\xc5\xa3\xb1\xc6'.decode("GBK"))

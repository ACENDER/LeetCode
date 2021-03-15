# -*- coding: utf-8 -*-
# @Time    : 2018/12/2 11:44

# Todo 字符串
# @File    : 3.1stringConstant.py

# 科学计数法
print(3.14e2)
print(3.14e-2)

# " ""  '''
str1 = "卢本伟牛逼"
str2 = '卢本伟牛逼'
str3 = '''\
卢本伟牛逼1
卢本伟牛逼2
卢本伟牛逼3\
'''
print(str1)
print(str2)
print(str3)

print("=" * 100)

str4 = 'Lishisan'

print(str4)  # 输出字符串
print(str4[0:-1])  # 输出(第一个)到(倒数第二个)的所有字符
print(str4[0])  # 输出字符串第一个字符
print(str4[2:5])  # 输出从第三个开始到第五个的字符
print(str4[2:])  # 输出从第三个开始的后的所有字符
print(str4 * 3)  # 输出字符串两次，也可以写成 print (3 * str)
print(str4 + "TEST")  # 连接字符串

# Python 使用反斜杠 \ 转义特殊字符，如果你不想让反斜杠发生转义，可以在字符串前面添加一个 r，表示原始字符串：
print('Ru\noob')
print('Ru\toob')
print(r'Ru\noob')

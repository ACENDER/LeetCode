# -*- coding: utf-8 -*-
# @Time    : 2018/12/2 11:23

# Todo 
# @File    : 2.0import.py
import os

print(os.getcwd())
# E:\ProjectsPyCharm\learnPy\zML\Python_1
os.chdir("E:\ProjectsPyCharm\learnPy")
print(os.getcwd())

import requests

text_content = requests.get("https://www.baidu.com")
print(text_content.url)
print(text_content.text)
print(text_content.encoding)

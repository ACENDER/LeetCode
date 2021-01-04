# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File : 批量修改文件名.py  @Time : PyCharm -lqj- 2021-1-4 0004

import os

path = '../题库/'
file_names = os.listdir(path)
replaceStr = ' '
for name in file_names:
    # name.replace(replaceStr, '')
    os.renames(os.path.join(path, name), os.path.join(path, name.replace(replaceStr, '')))

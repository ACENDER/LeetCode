# -*- coding: utf-8 -*-
# @Time    : 2018/12/5 18:31

# Todo 
# @File    : 22.Scipy.py
from scipy.sparse import csc_matrix
import numpy as np
# from scipy.sparse.linalg import svds, eigs
from scipy.sparse import linalg

A = csc_matrix([[1, 0, 0], [5, 0, 2], [0, -1, 0], [0, 0, 3]], dtype=float)
u, s, vt = linalg.svds(A, k=2)
print(u)
# [[-1.73323831e-01_抽象数据类型和面向对象编程  1.56782328e-01_抽象数据类型和面向对象编程]
#  [-2.27856346e-01_抽象数据类型和面向对象编程  9.54078802e-01_抽象数据类型和面向对象编程]
#  [-7.09160926e-19  2.32081766e-19]
#  [ 9.58144214e-01_抽象数据类型和面向对象编程  2.55250744e-01_抽象数据类型和面向对象编程]]
print(s)
# [2.75193379 5.6059665 ]
print(vt)
# [[-4.76975707e-01_抽象数据类型和面向对象编程  1.95156391e-18  8.78916478e-01_抽象数据类型和面向对象编程]
# [ 8.78916478e-01_抽象数据类型和面向对象编程 -1.30104261e-18  4.76975707e-01_抽象数据类型和面向对象编程]]
# array([ 2.75193379,  5.6059665 ])
print(np.sqrt(linalg.eigs(A.dot(A.T), k=2)[0]).real)
# array([ 5.6059665 ,  2.75193379])

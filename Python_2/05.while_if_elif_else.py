# -*- coding: utf-8 -*-
# @Time    : 2018/12/2 20:31
# @File    : 04if_elif_else.py
# Todo      猜数字游戏

number = 100
flag = False
while flag == False:
    guessNumber = int(input("Please input your number:"))
    if guessNumber == number:
        print("Wow,you guess number is right!")
        flag = True
    elif guessNumber > number:
        print("Your guess number is larger than before!")
    else:
        print("Your guess number is smaller than before")

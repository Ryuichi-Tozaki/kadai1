# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 02:51:19 2019

@author: nicoy
"""
n = str(input("文章を入力してください："))
m = n[::-1]
if n==m:
    print("回文です")
else:
    print("回文ではありません")    
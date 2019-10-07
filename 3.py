# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 23:18:15 2019

@author: nicoy
"""
list = []
for n in range(10):
    list.append(int(input("num...")))
else:
        for n in range(10):
            if list[n]<0:
                print("負の数があります。")
            elif list[n]==5:
                print("boo")
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 03:13:11 2019

@author: nicoy
"""
a = [1,4,9,16,25,36,49,81,100]
b = []
for n in range(10):
    if int(a[n-1])%2 == 0:
        b.append(a[n-1])
    else:
            print(b)
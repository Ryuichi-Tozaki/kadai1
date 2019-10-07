# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 03:23:53 2019

@author: nicoy
"""
import math
n = 0
m = 0
s = int(input("借金..."))
s2=s
h = int(input("一月の返済額..."))
h2=h
b = int(input("ボーナス額..."))
while True:
    n = n+1
    s = s-h
    if s<0:
        print("期間..."+str(math.floor((n+12)/12))+"年")
        break
while True:
    m = m+1
    s2 = s2-h2 
    if m%6==0:
        s2 = s2-b
    elif s2<0:
        print("期間（ボーナスあり）..."+str(math.floor((m+12)/12))+"年")
        break
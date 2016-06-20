# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 16:58:21 2016

把之前跑到一半的資料拿出來
"""
import os
import pandas as pd


"""
with open("remain.txt", "r", encoding="utf-8") as load_f:
    temp = load_f.readline()
    for each.line() in temp:
        a.append(each)
"""
"""
下面這一段,是先讀取前面的結果,打出字數,剩餘字數,使用時間
"""

b4 = pd.read_csv("history.txt", encoding="utf-8")

count = len(b4.ix[:])

load_last = b4.loc[count-1]
load = []
for each in load_last:
    load.append(each)
"""
load 這個 list 存放的，就是上一次的打出字數,剩餘字數,所花時間 

"""
#print(load)

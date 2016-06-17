# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 16:58:21 2016

把之前跑到一半的資料拿出來
"""
import os
a = []
with open("remain.txt", "r", encoding="utf-8") as load_f:
    a = load_f.readline()

a = a[1:-1]

print(a)

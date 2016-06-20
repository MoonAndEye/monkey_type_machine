# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 16:58:21 2016

把之前跑到一半的資料拿出來
"""
import os
import pandas as pd
import random as rd
import time


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

下面是做出讀檔功能
"""

with open("remain.txt", "r", encoding="utf-8") as load_f:
    temp = load_f.readline()
    temp = temp[1:-1]
    temp = temp.replace("'", "")
    temp = temp.replace(" ", "")
last = temp.split(",")

"""
last 裡面的list 就是上次還剩下的字,還沒被猴子打出來
"""
#print(last[0])
#print(last[0][1:-1])
#print(load)

start_time = time.time()


def reloadAndRun(target = [],result = []):
    flag = 0
    m_text = []
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
            'u', 'v', 'w', 'x', 'y', 'z']
    rdTextLeng = rd.randint(1,14)
    while len(target) > 0:
        for i in range(rdTextLeng):
            alpha = rd.choice(alphabet)
            m_text.append(alpha)
            output = "".join(m_text)
        #print(output)
            if output in target:
                target.remove(output)
        if flag == 500000:
            timer = time.time() - start_time
            newFlag = flag + result[0]
            newTimer = timer + result[2]
            with open("history.txt", "a", encoding = "utf-8") as f:
                f.write(str(newFlag) + "," + str(len(target))+ ","+str(newTimer) + "\n")
    
            with open("remain.txt", "w", encoding = "utf-8") as rf:
                rf.write(str(target))
            flag = 0
        flag = flag + 1

reloadAndRun(last,load)

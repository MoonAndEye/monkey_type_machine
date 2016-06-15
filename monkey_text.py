# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 11:47:33 2016


"""
import random as rd
import time
start_time = time.time()

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
            'u', 'v', 'w', 'x', 'y', 'z']

rdTextLeng = rd.randint(1,14)
#火山矽肺症的長度是 45, 所以先定個45 字元

#print(rdTextLeng)

m_text = []
# m_text is monkey text, means this text was typed by a monkey.


with open('C:/3python/monkey_type_machine/aLover_Shakespeare.txt', "r", encoding = "UTF-8") as file:
    read_file = file.read()
    read_file = read_file.lower()
    read_file = read_file.strip()
    read_file = read_file.replace("'", " ")
    read_file = read_file.replace(",", " ")
    read_file = read_file.replace("!", " ")
    read_file = read_file.replace("?", " ")
    read_file = read_file.replace("/n", " ")
    read_file = read_file.replace(".", " ")
    read_file = read_file.replace(";", " ")
    read_file = read_file.replace("-", " ")
    read_file = read_file.replace(":", " ")


pre_target = read_file.split()
target = list(set(pre_target))
backup = target.copy()
print ("Origin string count  = " + str(len(target)) )
max_len = 0
"""
for i in target:
    temp = len(i)
    if temp > max_len:
        max_len = temp
"""
 
#print(max_len)
flag = 0

while len(target) > 0:
    for i in range(rdTextLeng):
        alpha = rd.choice(alphabet)
        m_text.append(alpha)
        output = "".join(m_text)
        #print(output)
        if output in target:
            target.remove(output)
    m_text = []
    if flag % 500000 == 0:
        timer = time.time() - start_time
        with open("history.txt", "a", encoding = "utf-8") as f:
            f.write(str(flag) + "," + str(len(target))+ ","+str(timer) + "\n")
    
        with open("remain.txt", "w", encoding = "utf-8") as rf:
            rf.write(str(target))
    flag = flag + 1
print ("After 1 try, string count  = " + str(len(target)) ) 
print("Run time --- %s seconds ---" % (time.time() - start_time))      

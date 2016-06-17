# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 11:36:40 2016


"""
import os
import matplotlib.pyplot as plt
import csv
import pandas as pd
import matplotlib.animation as anima


total = 1076

temp = []

history = pd.read_csv("history.csv")
print(history.ix[1])

for each in history.ix[1]:
    temp.append(each)

print(temp)

piChart = [temp[1], 1076 - temp[1]]
print(piChart)

labels = 'Remains', 'Typed'
sizes = [piChart[0], piChart[1]]
colors = ['yellowgreen', 'mediumpurple'] 
explode = (0, 0.05)    # proportion with which to offset each wedge

plt.pie(sizes,              # data
        explode=explode,    # offset parameters 
        labels=labels,      # slice labels
        colors=colors,      # array of colours
        autopct='%1.1f%%',  # print the values inside the wedges
        shadow=True,        # enable shadow
        startangle=90       # starting angle
        )
        
plt.axis('equal')

filename = 1
left, width = .25, 1
bottom, height = .25, 1
right = left + width
top = bottom + height
plt.text(right, top, 'first try',
        fontsize = 22,
        horizontalalignment='right',
        verticalalignment='top',
        )
#plt.show()
plt.savefig(str(filename) + ".jpg")
"""
with open("history.csv", newline="") as f:
    history = csv.DictReader(f)
    #temp.append(history)
    for row in history:
        print(row)
"""


#print(history)
#print(temp[0][1])


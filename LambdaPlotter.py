# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 10:40:20 2021

@author: KoethGroup
"""

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt


# Needs addresss of file
address = str(input("Please enter the path for the file: "))            ## NOTE BENNE: Must be already converted file (ie: wavelength,Default,Batch1,Batch2...)
dframe = pd.read_csv(address, delimiter=',', header = 0)

wavelengths = dframe["wavelength"].tolist()
names = dframe.columns.values.tolist()



# Input the wavelength used to make the plot (275 nm, 600 nm)
l = int(input("Please enter the desired wavelength: "))


#Finds what index the desired wavelength is at 
hit = False
while hit == False:
    for i in range(0,len(wavelengths)):
        if wavelengths[i] == l:
            x = i
            hit = True



#Creates a list of all values in the dataframe at the desired wavelength
lis = dframe.iloc[x].tolist()
lis.pop(0)

#Creates the proper labels for the plot
numbers = np.arange(0,len(lis),1)
columns = ["S","Pre","Post","1","2","3","4","5","6","7","8","9"]
columnids = [1,5,9,49,53,57,61,65,69,73,77,81]

yaxis = dframe.iloc[l-190].values.tolist()
xaxis = names



a = []
b = []
c = []
d = []
e = []
f = []
g = []
h = []
i = []
j = []
k = []



#This is a terrible way of doing this! Oh Well! 
for s in range(1,len(names)):
    t = names[s].split()
    if "Preheat" in t:
        a.append(s)

    if "Heat" in t:
        b.append(s)

    if "1" in t[2]:
        c.append(s)

    if "2" in t[2]:
        d.append(s)

    if "3" in t[2]:
        e.append(s)

    if "4" in t[2]:
        f.append(s)

    if "5" in t[2]:
        g.append(s)

    if "6" in t[2]:
        h.append(s)

    if "7" in t[2]:
        i.append(s)

    if "8" in t[2]:
        j.append(s)

    if "9" in t[2]:
        k.append(s)

mpoints = []
letters = [a,b,c,d,e,f,g,h,i,j]
for v in letters:
    mpoints.append(max(v))
    #finds the point where we want to split the line connecting the points
    
#Plot shenanigans 
#Had to rotate x labels to fit in pre and post heat 

fig,ax = plt.subplots(1)
ax.set_xticks(columnids)
ax.set_xticklabels(columns)
ax.set_xticklabels(columns,rotation=45)
ax.set_xlabel("Irradiation #", fontsize = 12)
ax.set_ylabel("Transmission (%)", fontsize = 12)
ax.set_title("Transmission vs. Irradiation at \u03BB", fontsize = 12)

#plots the split lines 
for v in range(0,len(mpoints)):
    if mpoints[v] == 4:
        low = 0
    else: 
        low = mpoints[v-1]
    yrang = yaxis[low:mpoints[v]]
    xrang = numbers[low:mpoints[v]]
    ax.plot(xrang,yrang,marker = "o")


#C:/Users/hobbe/transmittance.csv
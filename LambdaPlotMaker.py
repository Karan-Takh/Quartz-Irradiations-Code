# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 08:58:14 2021

@author: Koeth CMS Lab
"""

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt


# Needs addresss of file
address = str(input("Please enter the path for the file: "))
dframe = pd.read_csv(address, delimiter=',', header = 0)

wavelengths = dframe["wavelength"].tolist()

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
numbers = np.arange(0,81,1)
columns = ["S","Pre","Post","1","2","3","4","5","6","7","8","9"]
columnids = [1,5,9,49,53,57,61,65,69,73,77,81]


#Plot shenanigans 
#Had to rotate x labels to fit in pre and post heat 
fig,ax = plt.subplots(1)
ax.plot(numbers,lis)
ax.set_xticks(columnids)
ax.set_xticklabels(columns)
ax.set_xticklabels(columns,rotation=45)
ax.set_xlabel("Irradiation #", fontsize = 12)
ax.set_ylabel("Transmission (%)", fontsize = 12)
ax.set_title("Transmission vs. Irradiation at \u03BB", fontsize = 12)
ax.text(60,80,"\u03BB = {l} (nm)".format(l =l), fontsize = 12)
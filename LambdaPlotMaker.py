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
lis = lis[10:]
# lis.pop(0)
# lis.pop(4)

#Creates the proper labels for the plot
numbers = np.arange(1,63,1)
columns = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15"]
columnids = [1, 6, 10, 14, 18, 22, 26, 31, 35, 39, 43, 47, 51, 55, 59]
# columnids = [10,14,18,22,26,30,34,38,42,46,50,54,58,62,66]


#Plot shenanigans 
#Had to rotate x labels to fit in pre and post heat 
fig,ax = plt.subplots(1)
ax.plot(numbers,lis)
ax.set_xticks(columnids)
ax.set_xticklabels(columns)
ax.set_xticklabels(columns)
ax.set_xlabel("Irradiation #", fontsize = 20)
ax.set_ylabel("Transmission (%)", fontsize = 20)
ax.set_title("Transmission vs. Irradiation at \u03BB", fontsize = 20)
# The location of the text will probably need to be changed for different wavelengths
ax.text(12,30,"\u03BB = {l} (nm)".format(l =l), fontsize = 20)

plt.grid(linestyle = '--')
plt.show()

# C:\\Users\kdee2\Documents\GitHub\Quartz-Irradiations-Code\\S8 Transmittance.csv
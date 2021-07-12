# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 09:25:40 2021

@author: Koeth CMS Lab
"""

import numpy as np
import csv
import pandas as pd

# initializes arrays
fileNames = [-999]
Date = [-999]
hits = []
results = []
hits2 = []

# Create function to remove commas from data values in csv file. This function was created seperately from the much of the rest of the code. 
def comma_remover(sheet):
    # read the inputted data sheet into a pandas dataframe
    sheetdf = pd.read_csv(sheet+'.csv')
    # create a list of the column names and remove all the commas in the data values in the first column
    cols = list(sheetdf.columns)
    sheetdf[cols[0]] = sheetdf[cols[0]].str.replace(',', '')
    # set the index as the first column, wavelength
    new = sheetdf.set_index(cols[0])
    # turnt the new dataframe into a csv, overwriting the inputted shset.
    new.to_csv(sheet+'.csv')


# finds the points where the original data set contains no numbers ie: the break points
def NaNFinder(array, argument):
    i = 0
    k = 0
    while k < len(array):
        if float('-inf') < float(array[k]) < float('inf'):
            k += 1
        else:
            hits.append(k)
            i += 1
            k += 1
    results.append(hits)
    results.append(len(hits))
    return results


# Used when writing, not used in the actual program
def HitFinder(array, argument):
    i = 0
    k = 0
    while k < len(array):
        if array[k] != argument:
            k += 1
        else:
            hits2.append(k)
            i += 1
            k += 1
    return hits2


# Searches an array for the indicated value and provides the index where it is located
def Finder(array, value):
    k = 0
    hit = False
    while k < len(array):
        while hit == False:
            if array[k] >= value:
                hit = True
            else:
                k += 1
    return k


# data input
def Input(filename):
    ## adds information to each array
    fileNames.append(filename)


y = input(
    'Enter the name of the data sheet you want to convert. Must be .csv. Please omit file ending (ie, do no type .csv): ')

# Call comma remover function to remove the commas from the first column of the file. 
comma_remover(y)


Input(str(y))

fileNames.remove(-999)

# Trash labels are parts of the title that aren't used in the code
fileName = fileNames[0]
# Generates list 'name' made up of each word of the file name.
name = fileName.split(' ')
date = name[0]
trash1 = name[1]
Samplenum = name[2]
trash2 = name[3]
trash3 = name[4]
# Lamb is the wavelengths, read into the numpy array.
lamb = np.genfromtxt(str(y) + '.csv', delimiter=',', skip_header=3, usecols=np.arange(0, 1))
# Trans is the transmittivities, read into a separate array. 
Trans = np.genfromtxt(str(y) + '.csv', delimiter=',', skip_header=3, usecols=np.arange(2, 3))
NaNFinder(Trans, 'nan')
# The range of wavelengths is usually 190 - 1100. Probably won't work for other ranges we decide to use. However, for the irradiations we'll be sticking to that.
lamb = lamb[0:911]
print("lamb is \n", lamb) 
Range = 911

amount = results[1] / 5

obj = {}
NewTrans = []  # Transmission without blank spaces
i = 0
while i < len(Trans):
    if float('-inf') < float(Trans[i]) < float('inf'):
        NewTrans.append(Trans[i])

    i += 1

i = 0
for i in range(0, int(amount) + 1):
    if i == 0:
        j = 0
    else:
        j = 1
    obj['l' + str(i)] = NewTrans[i * 911:(i + 1) * 911]

fieldnames = []
# Creates labels for the new data sheet
i = 0
fieldnames.append('wavelength')
for i in range(1, int(amount) + 1):
    fieldnames.append('Batch ' + str(i))

# creates data set to put in new data sheet
from itertools import zip_longest

data = []
data.append(lamb)
i = 0
for i in range(0, int(amount)):
    data.append(obj['l' + str(i)])

# writes new data sheet
x = input('Please input the name you would want to save the new file as. ')
export_data = zip_longest(*data, fillvalue='')
with open(str(x)+".csv", 'w+', encoding="ISO-8859-1", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(fieldnames)
    writer.writerows(export_data)
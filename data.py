#!/usr/bin/python3.8

import numpy as np
import sys
out = sys.stdout
with open("dataset.csv", "r") as f:
    data = f.readlines()
array = np.empty((0,3), dtype = int )
#looping through data to create an integer array with date, precip, tmax, tin as columns)
i = 1 #starting at 1 because data[0] is headings
while i < len(data):
    data[i].strip()
    data[i]= data[i].split(',')
    #using string slicing to return just the month of date
    branch = data[i][0]
    a = np.array([branch, int(data[i][4]), int(data[i][12])])
    array = np.vstack([array, a])
    i+=1

def getJanuary(arr):
    #creating an array copy of just the January column
    column = arr[:, 1].copy()
    january = []
    #convert string array to integer list for simplicity
    for i in column:
        january.append(i)
    return january
def getSeptember(arr):
    #creating an array copy of just the September column
    column = arr[:, 2].copy()
    september = []
    #convert string array to integer list for simplicity
    for i in column: 
        september.append(i)
    return september
jan = getJanuary(array)
sept = getSeptember(array)
out = open("JanOutput.txt", 'w')
for term in jan:
    out.write(str(term))
    out.write('\n')
out.close()
out = open('SeptOutput.txt', 'w')
for term in sept:
    out.write(str(term))
    out.write('\n')
out.close()
